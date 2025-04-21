import asyncio
import websockets
import base64
import os
import json # <--- Añadido para parsear JSON
from datetime import datetime

# --- Configuración ---
HOST = '0.0.0.0'
PORT = 8181       # Puerto 8181
SAVE_DIR = 'received_images'

# --- Crear directorio si no existe ---
if not os.path.exists(SAVE_DIR):
    try:
        os.makedirs(SAVE_DIR)
        print(f"Directorio '{SAVE_DIR}' creado.")
    except OSError as e:
        print(f"Error al crear directorio '{SAVE_DIR}': {e}")
        # Considerar salir si no se puede crear
        # exit(1)

# --- MODIFICADO: Ahora espera un objeto JSON ---
async def image_handler(websocket, path):
    """
    Manejador para procesar mensajes JSON entrantes que contienen
    la dirección del cruce ('IN'/'OUT') y la imagen base64.
    """
    client_address = websocket.remote_address
    print(f"Cliente conectado desde: {client_address} (Path solicitado: {path})")

    try:
        async for message in websocket:
            # print(f"Mensaje RAW recibido (inicio): {message[:150]}...") # Log si es necesario
            try:
                # 1. Intentar parsear el mensaje como JSON
                data = json.loads(message)

                # 2. Validar que sea un diccionario y tenga las claves esperadas
                if not isinstance(data, dict) or 'direction' not in data or 'imageData' not in data:
                    print(f"Error: JSON recibido de {client_address} no tiene el formato esperado (requiere 'direction' y 'imageData'). Ignorando.")
                    continue

                direction = data.get('direction')
                image_data_url = data.get('imageData')

                # 3. Validar el contenido
                if direction not in ('IN', 'OUT'):
                    print(f"Error: Dirección inválida ('{direction}') recibida de {client_address}. Debe ser 'IN' o 'OUT'. Ignorando.")
                    continue

                if not isinstance(image_data_url, str) or not image_data_url.startswith('data:image/jpeg;base64,'):
                     print(f"Error: 'imageData' recibido de {client_address} no parece ser un Data URL JPEG base64 válido. Ignorando.")
                     continue

                print(f"Recibido: Dirección='{direction}', Imagen JPEG base64 de {client_address}. Procesando...")

                # 4. Extraer datos base64
                header, base64_data = image_data_url.split(',', 1)

                # 5. Decodificar base64 a bytes
                image_bytes = base64.b64decode(base64_data)

                # 6. Generar nombre de archivo CON dirección
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                # filename = f"img_{timestamp}.jpg" # Nombre antiguo
                filename = f"img_{timestamp}_{direction}.jpg" # <--- NUEVO NOMBRE DE ARCHIVO
                filepath = os.path.join(SAVE_DIR, filename)

                # 7. Guardar archivo
                with open(filepath, 'wb') as f:
                    f.write(image_bytes)

                print(f"Imagen guardada exitosamente como: {filepath}")
                # Opcional: Enviar confirmación al cliente
                # await websocket.send(f"Imagen {filename} guardada.")

            except json.JSONDecodeError:
                 print(f"Error: Mensaje recibido de {client_address} no es JSON válido. Ignorando. Inicio: {message[:100]}...")
            except base64.binascii.Error as e:
                print(f"Error al decodificar Base64 de {client_address}: {e}")
                # await websocket.send("Error: Datos Base64 inválidos.")
            except ValueError as e:
                # Podría ocurrir si split falla
                print(f"Error al procesar datos de imagen (formato inesperado?) de {client_address}: {e}")
            except Exception as e:
                print(f"Error general al procesar/guardar la imagen de {client_address}: {e}")
                # await websocket.send(f"Error en el servidor al procesar imagen: {e}")

    except websockets.exceptions.ConnectionClosedOK:
        print(f"Cliente {client_address} desconectado limpiamente.")
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Conexión cerrada con error para {client_address}: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado con el cliente {client_address}: {e}")
    finally:
        print(f"Finalizada conexión con {client_address}.")


async def main():
    """Función principal para iniciar el servidor."""
    if not os.path.isdir(SAVE_DIR):
         print(f"Error: El directorio de guardado '{SAVE_DIR}' no existe o no es un directorio.")
         return

    handler_to_use = image_handler

    print(f"\nIniciando servidor con handler: {handler_to_use.__name__}")
    async with websockets.serve(handler_to_use, HOST, PORT):
        print(f"Servidor WebSocket iniciado en ws://{HOST}:{PORT}")
        print(f"Esperando conexiones... Las imágenes se guardarán en '{os.path.abspath(SAVE_DIR)}'")
        print(f"Formato de nombre esperado: img_YYYYMMDD_HHMMSS_ffffff_[IN|OUT].jpg") # <--- Info formato
        print("Presiona Ctrl+C para detener el servidor.")
        await asyncio.Future() # Mantener corriendo

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServidor detenido manualmente.")
    except OSError as e:
         if "Address already in use" in str(e):
              print(f"Error: El puerto {PORT} ya está en uso.")
         else:
              print(f"Error al iniciar el servidor: {e}")
    except Exception as e:
        print(f"Error inesperado en la ejecución global: {e}")

# JavaScript People Counter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Demo - Probar Contador](https://img.shields.io/badge/Demo-Probar_Contador-brightgreen)](https://soyunomas.github.io/javascript-people-counter/)[![Demo - Probar Contador_para móvil](https://img.shields.io/badge/Demo-Probar_Contador_móvil-brightblue)](https://soyunomas.github.io/javascript-people-counter/index_movil.html)

Una aplicación web para contar personas que cruzan una línea virtual usando la webcam **o un stream HLS** y TensorFlow.js, con opciones avanzadas de configuración y layout adaptable. 🚶↔️

## 📝 Descripción Breve

Este proyecto utiliza la cámara web del navegador **o una URL de stream HLS (.m3u8)** y el modelo COCO-SSD de TensorFlow.js para detectar personas en tiempo real. Implementa una lógica de seguimiento básica basada en centroides para identificar cuándo una persona cruza una línea configurable (horizontal o vertical) en la pantalla, manteniendo contadores separados para "Entradas" y "Salidas". Ofrece un layout dividido (vídeo a la izquierda, controles a la derecha) y diversas opciones de personalización y ajuste para controlar el comportamiento de la detección y el conteo, incluyendo umbral de confianza, salto de frames y cooldown de cruce.

## 🖼️ Captura de Pantalla / Demo

*   Captura de pantalla mostrando el layout dividido, detección de personas, línea de cruce (vertical u horizontal) y los controles/ajustes:

    ![Captura de Pantalla del Contador de Personas](screenshot.png)

Puedes probar la demo en vivo aquí:

*   **[Demo - Probar Contador](https://soyunomas.github.io/javascript-people-counter/)**
*   **[Demo - Probar Contador para móvil](https://soyunomas.github.io/javascript-people-counter/index_movil.html)**
*   **[Demo - Probar Contador mascotas (POC)](https://soyunomas.github.io/javascript-people-counter/index_mascotas.html)**

## ✨ Características Principales

*   **📹 Selección de Fuente de Vídeo:**
    *   Utiliza `navigator.mediaDevices.getUserMedia` para acceder al flujo de la **Webcam**.
    *   **NUEVO:** Permite conectar a un **Stream HLS (.m3u8)** introduciendo su URL. Ideal para cámaras IP (requiere conversión RTSP->HLS previa) o streams públicos.
*   **🤖 Detección en Tiempo Real:** Emplea **TensorFlow.js** y el modelo **COCO-SSD** preentrenado.
*   ** เส้น Detección de Cruce de Línea Flexible:**
    *   Identifica cruces a través de una línea virtual.
    *   **Orientación Configurable:** Permite cambiar entre línea **Vertical** u **Horizontal** mediante un interruptor.
    *   **Posición Ajustable:** Modifica la posición de la línea usando un slider.
*   **🕵️ Seguimiento Básico:** Intenta asignar un ID único y seguir personas entre frames (basado en proximidad de centroide).
*   **📊 Contadores Detallados:**
    *   Contadores separados para **Entradas** y **Salidas**.
    *   Cálculo y display de **"Personas Dentro"** (neto).
    *   Indicador de **"Pistas Activas"** (personas rastreadas).
*   **⚙️ Ajustes Avanzados de Detección:**
    *   **Invertir Sentido:** Cambia fácilmente qué dirección cuenta como entrada o salida.
    *   **Umbral de Confianza:** Slider para filtrar detecciones por debajo de una confianza mínima.
    *   **Salto de Frames (Frame Skipping):** Slider para procesar la detección sólo cada N frames, optimizando rendimiento CPU.
    *   **Cooldown de Cruce:** Slider para definir un tiempo mínimo (ms) antes de re-contar a la misma persona si cruza repetidamente.
    *   **Ayuda Integrada:** Iconos de interrogación con popovers explicativos para cada ajuste.
*   **⏯️ Controles de Ejecución:**
    *   **Pausa/Reanudar:** Detiene/continúa el proceso de detección y seguimiento.
    *   **Resetear:** Pone a cero los contadores y limpia las pistas activas.
*   **💡 Feedback Visual:**
    *   Indicador claro de dirección Entrada/Salida (se adapta a orientación e inversión).
    *   El display de contadores parpadea brevemente al registrar un cruce.
*   **🖥️ Layout Dividido y Responsivo:**
    *   Interfaz organizada con el vídeo/canvas a la izquierda y los controles/ajustes a la derecha en pantallas grandes.
    *   Se adapta a pantallas más pequeñas gracias a Bootstrap Grid.
*   **🎨 Interfaz con Bootstrap:** Usa Bootstrap 5 para layout, componentes (botones, sliders, alerts, popovers, switch) y utilidades.
*   **🧩 Código Autónomo:** Aplicación completa en un único archivo HTML con CSS y JavaScript incrustados.

## 🛠️ Tecnologías Utilizadas

*   **HTML5:** Estructura semántica.
*   **CSS3:** Estilos personalizados, animaciones (flash), layout.
*   **Bootstrap 5.3.x:** Framework CSS/JS para layout, componentes y utilidades (cargado desde CDN).
*   **Bootstrap Icons:** Iconografía (cargado desde CDN).
*   **JavaScript (ES6+):** Lógica principal:
    *   Acceso a Webcam (`getUserMedia`).
    *   **NUEVO:** Reproducción de HLS con `hls.js`.
    *   Integración con TensorFlow.js (detección).
    *   Algoritmo de seguimiento y lógica de cruce.
    *   Manipulación del DOM y gestión de eventos.
    *   Manejo de estado.
*   **TensorFlow.js Core (`@tensorflow/tfjs`):** Librería base de ML (cargada desde CDN).
*   **TensorFlow.js COCO-SSD Model (`@tensorflow-models/coco-ssd`):** Modelo preentrenado (cargado desde CDN).
*   **NUEVO: hls.js:** Librería para reproducir streams HLS (cargada desde CDN).
*   **CDNs:** Todas las librerías externas se cargan desde CDNs.

## 🚀 Instalación / Visualización Local

Aplicación web estática 100% del lado del cliente.

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/soyunomas/javascript-people-counter.git
    ```
2.  **Navega al directorio:**
    ```bash
    cd javascript-people-counter
    ```
3.  **Abre el archivo HTML:**
    *   Abre `index.html` (o el nombre que le hayas dado) en tu navegador.
4.  **🌐 Conexión a Internet:** Necesaria para cargar librerías desde CDNs.
5.  **(Permisos):** Concede permiso para usar la cámara web si eliges esa opción.
6.  **(Sin Dependencias Adicionales):** No requiere Node.js, build, etc.

## 🕹️ Cómo Usar

1.  **Inicio:** Abre el archivo HTML. Por defecto, intentará usar la Webcam. Concede permisos y espera a que cargue el modelo (ver `status` abajo a la izquierda).
2.  **Cambiar a HLS (Opcional):**
    *   En la sección "Ajustes" -> "Fuente de Vídeo", selecciona "**Stream URL (HLS)**".
    *   Pega una URL válida de stream `.m3u8` en el campo que aparece. *(Nota: Los streams RTSP directos no funcionan; deben convertirse previamente a HLS. El stream HLS debe ser públicamente accesible o permitir CORS desde tu origen).*
    *   Pulsa "**Conectar**".
3.  **Visualización:** Verás el vídeo (webcam o HLS) a la izquierda. La línea roja es la zona de cruce. Las personas detectadas tendrán un cuadro verde y un ID.
4.  **Cruce:** Muévete (o espera movimiento en el stream) cruzando la línea. Los contadores (derecha) se actualizarán.
5.  **Controles Principales (Derecha):**
    *   **Pos. Línea:** Mueve el slider para cambiar la ubicación de la línea.
    *   **Switch H/V:** Cambia entre línea Horizontal o Vertical (reinicia pistas).
    *   **Invertir Sentido:** Cambia la dirección de entrada/salida.
    *   **Pausa/Reanudar:** Detiene/continúa la detección.
    *   **Resetear:** Borra contadores y pistas.
6.  **Ajustes de Detección (Derecha):**
    *   Modifica los sliders de **Confianza Mín.**, **Procesar cada (Frames)**, y **Cooldown Cruce**.
    *   Haz clic/hover en el icono <i class="bi bi-question-circle"></i> para ver qué hace cada ajuste.
7.  **Observar Información:** Abajo a la izquierda verás el número de `Pistas activas` y el `status` actual.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🧑‍💻 Contacto

Creado por **soyunomas** ([@soyunomas en GitHub](https://github.com/soyunomas))

---

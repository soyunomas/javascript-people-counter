# JavaScript People Counter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Demo - Probar Contador](https://img.shields.io/badge/Demo-Probar_Contador-brightgreen)](https://soyunomas.github.io/javascript-people-counter/) <!-- Asegúrate que esta URL sea correcta después de desplegar en GitHub Pages -->

Una aplicación web para contar personas que cruzan una línea virtual usando la webcam y TensorFlow.js. 🚶↔️

## 📝 Descripción Breve

Este proyecto utiliza la cámara web del navegador y el modelo COCO-SSD de TensorFlow.js para detectar personas en tiempo real. Implementa una lógica de seguimiento básica basada en centroides para identificar cuándo una persona cruza una línea vertical configurable en la pantalla, manteniendo contadores separados para "Entradas" y "Salidas". Ofrece diversas opciones de personalización y ajuste para controlar el comportamiento de la detección y el conteo.

## 🖼️ Captura de Pantalla / Demo

*   Captura de pantalla mostrando la detección de personas, la línea de cruce y los contadores:

    ![Captura de Pantalla del Contador de Personas](screenshot.png) <!-- REEMPLAZA ESTA IMAGEN -->

Puedes probar la demo en vivo aquí:

*   **[Demo - Probar Contador](https://soyunomas.github.io/javascript-people-counter/)**

## ✨ Características Principales

*   **📹 Acceso a Webcam:** Utiliza `navigator.mediaDevices.getUserMedia` para acceder al flujo de vídeo de la cámara.
*   **🤖 Detección en Tiempo Real:** Emplea **TensorFlow.js** y el modelo **COCO-SSD** preentrenado para detectar personas en cada frame procesado.
*   ** เส้น Detección de Cruce de Línea:** Identifica cuándo el centroide de una persona detectada cruza una línea vertical virtual.
*   **🕵️ Seguimiento Básico:** Intenta asignar un ID único a cada persona detectada y seguirla entre frames basándose en la proximidad del centroide.
*   **📊 Contadores:**
    *   Muestra contadores separados para **Entradas** y **Salidas**.
    *   Calcula y muestra el número neto de **"Personas Dentro"**.
    *   Muestra el número de **"Pistas Activas"** (personas siendo rastreadas actualmente).
*   **⚙️ Ajustes Configurables:**
    *   **Posición de la Línea:** Ajusta la ubicación horizontal de la línea de cruce mediante un slider.
    *   **Invertir Sentido:** Cambia la dirección que cuenta como entrada o salida.
    *   **Umbral de Confianza:** Establece la confianza mínima requerida para que una detección sea considerada válida.
    *   **Salto de Frames:** Configura cada cuántos frames se realiza el procesamiento de detección para optimizar el rendimiento.
    *   **Cooldown de Cruce:** Define un tiempo mínimo antes de volver a contar a la misma persona si cruza repetidamente.
*   **⏯️ Controles de Ejecución:**
    *   **Pausa/Reanudar:** Detiene y reinicia el proceso de detección y seguimiento.
    *   **Resetear:** Pone a cero los contadores de entradas/salidas y limpia las pistas activas.
*   **💡 Feedback Visual:**
    *   Indicador claro de qué dirección es Entrada/Salida.
    *   El contador principal parpadea brevemente cuando se registra un cruce.
    *   Popovers explicativos para los ajustes de configuración.
*   **🎨 Interfaz con Bootstrap:** Usa Bootstrap 5 para un layout responsivo y componentes de interfaz (botones, sliders, alerts, popovers).
*   **🧩 Código Autónomo:** Toda la aplicación (HTML, CSS, JavaScript) está contenida en un único archivo HTML para simplicidad.

## 🛠️ Tecnologías Utilizadas

*   **HTML5:** Estructura semántica de la página.
*   **CSS3:** Estilos personalizados para la interfaz y las visualizaciones (línea, bounding boxes, IDs).
*   **Bootstrap 5.3.x:** Framework CSS/JS para layout responsivo, componentes y utilidades (cargado desde CDN).
*   **Bootstrap Icons:** Iconografía para botones y ayudas (cargado desde CDN).
*   **JavaScript (ES6+):** Lógica principal de la aplicación:
    *   Acceso a la webcam.
    *   Integración y uso de TensorFlow.js (detección).
    *   Algoritmo de seguimiento por centroide y lógica de cruce de línea.
    *   Manipulación del DOM para actualizar la UI (canvas, contadores, ajustes).
    *   Gestión de eventos (botones, sliders).
    *   Manejo del estado (pausa, inversión, ajustes).
*   **TensorFlow.js Core (`@tensorflow/tfjs`):** Librería base para Machine Learning en el navegador (cargada desde CDN).
*   **TensorFlow.js COCO-SSD Model (`@tensorflow-models/coco-ssd`):** Modelo preentrenado para detección de objetos comunes, incluyendo personas (cargado desde CDN).
*   **CDNs:** Todas las librerías externas (Bootstrap, TF.js) se cargan desde CDNs.

## 🚀 Instalación / Visualización Local

Este proyecto es una aplicación web estática que se ejecuta completamente en el navegador del cliente.

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/soyunomas/javascript-people-counter.git
    ```
2.  **Navega al directorio del proyecto:**
    ```bash
    cd javascript-people-counter
    ```
3.  **Abre el archivo HTML principal:**
    *   Abre el archivo `index.html` (o el nombre que tenga tu archivo principal) directamente en tu navegador web (Chrome, Firefox, Edge, etc.).
4.  **🌐 Conexión a Internet:** Necesaria para cargar Bootstrap, Bootstrap Icons y TensorFlow.js desde sus CDNs.
5.  **(Permisos):** Deberás conceder permiso al navegador para acceder a tu cámara web cuando lo solicite.
6.  **(Sin Dependencias Adicionales):** No requiere Node.js, ni compilación, ni servidores complejos.

## 🕹️ Cómo Usar

1.  **Abrir la Aplicación:** Abre el archivo HTML en tu navegador.
2.  **Permiso de Webcam:** Concede permiso para usar la cámara cuando el navegador lo pida.
3.  **Carga Inicial:** Espera a que se cargue el modelo TensorFlow.js (puede tardar unos segundos la primera vez). El estado se indicará en la parte inferior.
4.  **Observar Detección:** Una vez listo, verás el vídeo de tu webcam en el área del canvas. Las personas detectadas (con suficiente confianza) tendrán un recuadro verde y un ID de seguimiento. La línea roja vertical indica la zona de cruce.
5.  **Cruzar la Línea:** Muévete (o pide a alguien que lo haga) para cruzar la línea roja. Observa cómo los contadores de "Entradas" o "Salidas" (según la dirección y la configuración de inversión) se incrementan y el display parpadea. El contador "Personas Dentro" se actualizará.
6.  **Ajustar la Línea:** Usa el slider "Posición Línea" para mover la línea roja horizontalmente.
7.  **Usar Controles:**
    *   **Resetear:** Borra los contadores y las pistas actuales.
    *   **Invertir Sentido:** Cambia qué dirección cuenta como entrada/salida (el indicador de texto se actualizará).
    *   **Pausa/Reanudar:** Detiene o continúa el proceso de detección y seguimiento.
8.  **Modificar Ajustes:**
    *   Expande la sección "Ajustes de Detección".
    *   **Confianza Mín.:** Ajusta el slider para requerir una mayor o menor confianza del modelo para detectar a una persona.
    *   **Procesar cada:** Aumenta el valor para procesar menos frames por segundo y reducir el uso de CPU (a costa de menor fluidez en el seguimiento).
    *   **Cooldown Cruce:** Ajusta el tiempo de espera antes de volver a contar a la misma persona.
    *   Pulsa el icono <i class="bi bi-question-circle"></i> para ver una explicación de cada ajuste.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🧑‍💻 Contacto

Creado por **soyunomas** ([@soyunomas en GitHub](https://github.com/soyunomas))

---

### Proyecto de Aprendizaje con Pygame

Este proyecto contiene una variedad de ejercicios y mini-proyectos desarrollados con 
**Pygame** para practicar conceptos de programación gráfica.

### Introducción a Pygame

### 'sesion1_ej1.py' – Cierre con tecla
- Muestra una ventana con fondo morado.
- Permite cerrar la ventana al presionar la tecla **ESC** o al hacer clic en el botón de cerrar.

### 'sesion1_ej2.py' – Contador de frames
- Imprime en consola el número de frame actual ('Frame: 1', 'Frame: 2', ...).
- El programa se cierra automáticamente después de **300 frames**.

### 'sesion1_mini.py' – Cambio de color con tecla
- Muestra una ventana con fondo blanco.
- Al presionar la tecla **C**, el fondo cambia entre blanco y azul.

## Sesión 2: Primitivas gráficas

### 'sesion2_ej1.py' – Tablero de ajedrez
- Dibuja un tablero de ajedrez **8x8** usando 'pygame.draw.rect'.
- Alterna colores blanco y negro usando bucles anidados.

### 'sesion2_ej2.py' – Diseño geométrico
- Dibuja **5 círculos concéntricos** con radios crecientes (20 a 100 px).
- Cada círculo tiene un color distinto y comparte el mismo centro.
  
### 'sesion2_mini.py' – Casa interactiva
- Dibuja una casa simple con:
  - Rectángulo (cuerpo)
  - Triángulo (techo)
  - Círculos (ventanas)
- Al presionar **R** o **B**, cambia el color del cuerpo de la casa a rojo o azul.

## Sesión 3: Transformaciones 2D

### 'sesion3_ej1.py' – Movimiento con límites
- Mueve un rectángulo con las flechas del teclado.
- Si toca los bordes de la ventana, cambia a color rojo.
- El rectángulo no puede salirse de la pantalla.

### 'sesion3_ej2.py' – Trayectoria circular
- El rectángulo se mueve automáticamente en una trayectoria circular.
- Usa funciones trigonométricas ('math.cos', 'math.sin') para calcular la posición.
- No requiere entrada del usuario.

### ✅ 'sesion3_mini.py' – Rastro de movimiento
- El usuario mueve un rectángulo con el teclado.
- El rectángulo deja un **rastro de círculos** en su trayectoria.
- Usa una lista para almacenar y dibujar las posiciones anteriores.

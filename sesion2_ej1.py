import pygame
pygame.init()

# Configuración de la ventana
ancho, alto = 800, 800
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Tablero de Ajedrez")

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)

# Tamaño de cada casilla
tam_casilla = ancho // 8

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Dibujar el tablero
    for fila in range(8):
        for columna in range(8):
            color = blanco if (fila + columna) % 2 == 0 else negro
            rect = pygame.Rect(columna * tam_casilla, fila * tam_casilla, tam_casilla, tam_casilla)
            pygame.draw.rect(ventana, color, rect)

    pygame.display.flip()

pygame.quit()
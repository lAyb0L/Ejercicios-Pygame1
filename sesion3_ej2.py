import pygame
import math
pygame.init()

# Configuración de la ventana
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Trayectoria circular")

# Centro de la trayectoria
centro_x, centro_y = 400, 300
radio = 100
angulo = 0
velocidad_angular = 0.02  # radianes por frame

# Rectángulo
rect_w, rect_h = 50, 50
color_rect = (0, 255, 255)

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Calcular posición circular
    rect_x = centro_x + math.cos(angulo) * radio - rect_w // 2
    rect_y = centro_y + math.sin(angulo) * radio - rect_h // 2
    angulo += velocidad_angular

    ventana.fill((30, 30, 30))
    pygame.draw.rect(ventana, color_rect, (rect_x, rect_y, rect_w, rect_h))
    pygame.display.flip()

pygame.quit()
import pygame
pygame.init()

# Configuración de la ventana
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Movimiento con límites")

# Rectángulo
rect_x, rect_y = 100, 100
rect_w, rect_h = 50, 50
velocidad = 5
color_rect = (0, 255, 0)  # verde

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Teclas presionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        rect_x -= velocidad
    if teclas[pygame.K_RIGHT]:
        rect_x += velocidad
    if teclas[pygame.K_UP]:
        rect_y -= velocidad
    if teclas[pygame.K_DOWN]:
        rect_y += velocidad

    # Limitar movimiento dentro de la ventana
    if rect_x < 0:
        rect_x = 0
    if rect_x + rect_w > ancho:
        rect_x = ancho - rect_w
    if rect_y < 0:
        rect_y = 0
    if rect_y + rect_h > alto:
        rect_y = alto - rect_h

    # Cambiar color si toca los bordes
    if rect_x == 0 or rect_x + rect_w == ancho or rect_y == 0 or rect_y + rect_h == alto:
        color_rect = (255, 0, 0)  # rojo
    else:
        color_rect = (0, 255, 0)  # verde

    ventana.fill((0, 0, 0))
    pygame.draw.rect(ventana, color_rect, (rect_x, rect_y, rect_w, rect_h))
    pygame.display.flip()

pygame.quit()
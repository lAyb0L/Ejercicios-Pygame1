import pygame
pygame.init()

# Configuración de la ventana
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Mini-proyecto: Rastro de movimiento")

# Rectángulo
rect_x, rect_y = 100, 100
rect_w, rect_h = 50, 50
velocidad = 5
color_rect = (0, 0, 255)

# Lista para almacenar posiciones del rastro
rastro = []

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Movimiento con teclado
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        rect_x -= velocidad
    if teclas[pygame.K_RIGHT]:
        rect_x += velocidad
    if teclas[pygame.K_UP]:
        rect_y -= velocidad
    if teclas[pygame.K_DOWN]:
        rect_y += velocidad

    # Limitar dentro de la ventana
    rect_x = max(0, min(ancho - rect_w, rect_x))
    rect_y = max(0, min(alto - rect_h, rect_y))

    # Agregar posición actual al rastro
    centro_rect = (rect_x + rect_w // 2, rect_y + rect_h // 2)
    rastro.append(centro_rect)

    # Limitar tamaño del rastro (opcional)
    if len(rastro) > 300:
        rastro.pop(0)

    ventana.fill((0, 0, 0))  # fondo negro

    # Dibujar rastro
    for pos in rastro:
        pygame.draw.circle(ventana, (83, 83, 236), pos, 5)

    # Dibujar rectángulo
    pygame.draw.rect(ventana, color_rect, (rect_x, rect_y, rect_w, rect_h))

    pygame.display.flip()

pygame.quit()
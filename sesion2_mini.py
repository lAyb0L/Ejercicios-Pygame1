import pygame
pygame.init()

# Configuración de la ventana
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Mini-proyecto: Casa con colores")

# Colores
rojo = (210, 46, 46)
azul = (17, 159, 212)
gris = (200, 200, 200)
negro = (138, 96, 43)
amarillo = (255, 255, 0)

# Color inicial de la casa
color_casa = gris

# Coordenadas base
centro_x = ancho // 2
base_y = alto // 2 + 100

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                corriendo = False
            elif evento.key == pygame.K_r:
                color_casa = rojo
            elif evento.key == pygame.K_b:
                color_casa = azul

    ventana.fill((135, 206, 235))  # fondo celeste

    # pared
    cuerpo_rect = pygame.Rect(centro_x - 100, base_y - 150, 200, 150)
    pygame.draw.rect(ventana, color_casa, cuerpo_rect)

    #techo
    puntos_techo = [
        (centro_x - 120, base_y - 150),
        (centro_x + 120, base_y - 150),
        (centro_x, base_y - 250)
    ]
    pygame.draw.polygon(ventana, negro, puntos_techo)

    #ventana
    pygame.draw.circle(ventana, amarillo, (centro_x - 50, base_y - 100), 20)
    pygame.draw.circle(ventana, amarillo, (centro_x + 50, base_y - 100), 20)

    pygame.display.flip()

pygame.quit()
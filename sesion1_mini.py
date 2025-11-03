import pygame
pygame.init()

# Dimensiones de la ventana
ancho, alto = 1000, 800
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("cambia el color con C")

# Colores
verde = (44, 92, 95)
azul = (83, 83, 236)

# Estado inicial
color_fondo = verde
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                corriendo = False
            elif evento.key == pygame.K_c:
                # Cambiar entre blanco y azul
                color_fondo = azul if color_fondo == verde else verde

    ventana.fill(color_fondo)
    pygame.display.flip()

pygame.quit()
import pygame
pygame.init()

ancho, alto = 1000, 800
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Esta NO es una ventana rosa")
morado = (214, 220, 255)

color_fondo = morado
corriendo = True
contador_frames = 0 

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                corriendo = False

    contador_frames += 1
    print(f"Frame: {contador_frames}")

    if contador_frames >= 300:
        corriendo = False

    ventana.fill(color_fondo)
    pygame.display.flip()

pygame.quit()
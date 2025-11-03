import pygame;
pygame.init()

ancho, alto = 1000, 800
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Esta NO es una ventana rosa")
morado = (214, 220, 255)

color_fondo = morado
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
            
         #llenar la ventana con el color
        ventana.fill(color_fondo)

        #actualizar la pantalla
        pygame.display.flip()
import pygame
pygame.init()

# Configuración de la ventana
ancho, alto = 600, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Diseño Geométrico")

# Centro de los círculos
centro = (ancho // 2, alto // 2)

# Colores para los círculos
colores = [
    (255, 0, 0),    # rojo
    (0, 255, 0),    # verde
    (0, 0, 255),    # azul
    (255, 255, 0),  # amarillo
    (255, 0, 255)   # magenta
]

# Radios crecientes
radios = [20, 40, 60, 80, 100]

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((0, 0, 0))  # fondo negro para contraste

    # Dibujar círculos concéntricos
    for i in range(5):
        pygame.draw.circle(ventana, colores[i], centro, radios[i], width=3)

    pygame.display.flip()

pygame.quit()
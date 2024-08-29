import pygame
import sys
from input_handler import manejar_entrada  # Importar el archivo de manejo de entrada

# Inicializar Pygame
pygame.init()

# Establecer dimensiones de la ventana
ventana_ancho = 800
ventana_alto = 600
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))

# Cargar imagen del personaje
personaje = pygame.image.load("personaje/gojo.png")
personaje = pygame.transform.scale(personaje, (300, 300))

# Cargar flechas
flecha_arriba = pygame.image.load("personaje/gojo2.png")
flecha_arriba = pygame.transform.scale(flecha_arriba, (100, 100))

# Establecer título de la ventana
pygame.display.set_caption("Ritmo Frenético")

# Cargar música
musica = pygame.mixer.music.load("musica/musica1.mp3")
pygame.mixer.music.play(-1)  # Repetir la música

# Posición inicial del personaje
personaje_rect = personaje.get_rect()
personaje_x = ventana_ancho / 2 - personaje_rect.width / 2    
personaje_y = ventana_alto / 2 - personaje_rect.height / 2 

# Posición inicial de la flecha
flecha_x = ventana_ancho / 2 - 50
flecha_y = 0

# Velocidad de la flecha
flecha_velocidad = 5

# Bucle principal del juego
while True:
    # Manejar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Lógica del juego
    resultado = manejar_entrada(personaje_rect)
    if resultado:
        print(resultado)


    # Mover la flecha
    flecha_y += flecha_velocidad
    
    # Reiniciar la flecha cuando sale de la pantalla
    if flecha_y > ventana_alto:
        flecha_y = 0

        
    
    # Dibujar fondo
    ventana.fill((255, 255, 255))

    # Dibujar personaje y flecha
    ventana.blit(personaje, (personaje_x, personaje_y))
    ventana.blit(flecha_arriba, (flecha_x, flecha_y))

    # Actualizar ventana
    pygame.display.flip()
    pygame.time.Clock().tick(60)




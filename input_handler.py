import pygame

def manejar_entrada(flecha_y, personaje_y, personaje_rect):
    keys = pygame.key.get_pressed()
    resultado = None


    if keys[pygame.K_UP]:
        if flecha_y > personaje_y and flecha_y < personaje_y + personaje_rect.height:
            resultado = "¡Correcto!"
    # Añadir lógica para las demás teclas

    return resultado

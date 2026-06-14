import pygame

def cargar_imagen(ruta):
    # Importamos anim aquí para evitar dependencias circulares
    from . import anim
    img = pygame.image.load(ruta).convert_alpha()
    anim.lista_frames.append(img)
    return img

# "Inyectamos" la función en el módulo pygame
pygame.imagen = cargar_imagen
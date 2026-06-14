import pygame

lista_frames = []
fps = 60
nombre = "Animacion"

def init():
    pygame.init()

def name(titulo):
    global nombre
    nombre = titulo
    pygame.display.set_caption(titulo)

class render:
    @staticmethod
    def fremis(f):
        global fps
        fps = f

def run(func):
    # 1. Ejecutamos la función para registrar las imágenes
    func(None)
    
    # 2. Bucle principal
    clock = pygame.time.Clock()
    screen = pygame.display.get_surface()
    idx = 0
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Renderizado
        if lista_frames:
            screen.fill((0, 0, 0)) # Limpiar fondo
            screen.blit(lista_frames[idx], (0, 0))
            idx = (idx + 1) % len(lista_frames)
            
        pygame.display.flip()
        clock.tick(fps)
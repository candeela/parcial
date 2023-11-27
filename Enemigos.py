import pygame

class Enemigos:
    def __init__(self,x,y,ancho,alto):
        self.path_imagen = "enemigo.png"
        self.imagen  = pygame.image.load("enemigo.png")
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
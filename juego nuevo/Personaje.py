import pygame
class Personaje:
    def __init__(self, x,y,ancho,alto):
        self.path_imagen = "perro.jpg"
        self.imagen  = pygame.image.load("perro.jpg")
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
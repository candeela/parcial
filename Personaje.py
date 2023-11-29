import pygame

class Personaje:
    def __init__(self, x,y,ancho,alto):
        self.path_imagen = "nave.png"
        self.imagen  = pygame.image.load("nave.png")
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y

    def moverse(self, lista_posicion):
        self.rect.x = lista_posicion[0]
        self.rect.y = lista_posicion[1]
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 795:
            self.rect.x = 795

        if self.rect.y <0:
            self.rect.y = 0
        elif self.rect.y > 575:
            self.rect.y = 575

    def mostrar_personaje(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
import pygame
from constantes import *

class Enemigos:
    def __init__(self,x,y,ancho,alto):
        self.path_imagen = "enemigo.png"
        self.imagen  = pygame.image.load("enemigo.png")
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.flag = True

    def mover_derecha(self, velocidad):
        self.rect.x += velocidad
        if self.rect.x >= ANCHO_VENTANA:
            self.rect.x = -10

    def mover_izquierda(self, velocidad):
        self.rect.y += velocidad
        if self.rect.y >= ANCHO_VENTANA:
            self.rect.y = -10

    def mostrar_enemigo(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
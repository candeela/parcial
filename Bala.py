import pygame
from constantes import *


class Bala:
    def __init__(self, x,y,ancho,alto):
        self.path_imagen = "disparo.png"
        self.imagen  = pygame.image.load("disparo.png")
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direccion = ''
        self.mostrar_bala = False
        self.sonido_explosion = pygame.mixer.Sound("laser.mp3")

    def disparar(self, direccion, posicion_personaje):
        self.direccion = direccion
        self.rect.x = posicion_personaje[0]  
        self.rect.y = posicion_personaje[1]
        self.mostrar_bala = True
        self.sonido_explosion.play()

    def mover(self):
        if self.mostrar_bala:
            if self.direccion == 'derecha':
                self.rect.x += 10
            elif self.direccion == 'izquierda':
                self.rect.x -= 10
            elif self.direccion == 'arriba':
                self.rect.y -= 10
            elif self.direccion == 'abajo':
                self.rect.y += 10

            if self.rect.y <= 0 or self.rect.y >= ALTO_VENTANA or self.rect.x <= 0 or self.rect.x >= ANCHO_VENTANA:
                self.mostrar_bala = False

    def blitear_bala(self, pantalla):
        if self.mostrar_bala:
            pantalla.blit(self.imagen, self.rect)
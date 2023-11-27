import pygame

class Widget:
    def __init__(self,x,y,ancho,largo,path_imagen):
        self.imagen = pygame.transform.scale(pygame.image.load(path_imagen),(ancho,largo))
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y


    def update(self,pantalla,lista_eventos):
        pantalla.blit(self.imagen,self.rectangulo)
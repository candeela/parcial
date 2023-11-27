import pygame
from Widget import Widget
from constantes import *

class TextBox1(Widget):
    def __init__(self, x, y, ancho, largo, fuente, path_imagen):
        super().__init__(x, y, ancho, largo, path_imagen)
        self.texto = ""
        self.place_holder_text = None
        self.esta_seleccionada = False
        self.imagen = pygame.transform.scale(pygame.image.load(path_imagen), (ancho, largo))
        self.fuente = pygame.font.SysFont(fuente, 50)
    
    def mostrar_texto(self, pantalla):
        if self.texto == "" and self.place_holder_text is not None and not self.esta_seleccionada:
            texto_a_renderizar = self.place_holder_text
        else:
            texto_a_renderizar = self.texto

        texto_renderizado = self.fuente.render(texto_a_renderizar, True, COLOR_BLANCO)
        rectangulo_texto = texto_renderizado.get_rect()
        rectangulo_texto.center = self.rectangulo.center
        pantalla.blit(texto_renderizado, rectangulo_texto)

    
    def obtener_texto(self):
        return self.texto

    def update(self, pantalla, lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if self.rectangulo.collidepoint(evento.pos):
                    self.esta_seleccionada = True
                else:
                    self.esta_seleccionada = False

            elif self.esta_seleccionada and evento.type == pygame.KEYDOWN:
                caracter = evento.unicode
                
                if evento.key == pygame.K_BACKSPACE:
                    self.texto = self.texto[:-1]
                    
                elif caracter.isalnum() or caracter == " ":
                    self.texto += caracter

        super().update(pantalla, lista_eventos)
        self.mostrar_texto(pantalla)

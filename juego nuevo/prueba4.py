import pygame
from constantes import *

pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("juego")

imagen = pygame.image.load("perro.jpg")
imagen = pygame.transform.scale(imagen, (100, 100))
rect_personaje = imagen.get_rect()
rect_personaje.x = 30
rect_personaje.y = 100

rect_x = rect_personaje.x 
rect_y = rect_personaje.y

imagen_2 = pygame.image.load("bala.jpg")
imagen_2 = pygame.transform.scale(imagen_2, (100, 100))

flag_correr = True
mostrar_imagen_2 = False
derecha = False
izquierda = False
arriba = False
abajo = False

def disparar(posicion_x, posicion_y):
    rect_2 = pygame.Rect(posicion_x, posicion_y, 100, 100)
    return rect_2

while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            lista_posicion = list(evento.pos)
            rect_personaje.x = lista_posicion[0]
            rect_personaje.y = lista_posicion[1]

    lista_teclas = pygame.key.get_pressed()
    if lista_teclas[pygame.K_RIGHT]:
        mostrar_imagen_2 = True
        derecha = True
    if lista_teclas[pygame.K_LEFT]:
        mostrar_imagen_2 = True
        izquierda = True
    if lista_teclas[pygame.K_UP]:
        mostrar_imagen_2 = True
        arriba = True
    if lista_teclas[pygame.K_DOWN]:
        mostrar_imagen_2 = True
        abajo = True

    # Limitar el movimiento del personaje
    if rect_personaje.x < 0:
        rect_personaje.x = 0
    elif rect_personaje.x > ANCHO_VENTANA - rect_personaje.width:
        rect_personaje.x = ANCHO_VENTANA - rect_personaje.width

    if rect_personaje.y < 0:
        rect_personaje.y = 0
    elif rect_personaje.y > ALTO_VENTANA - rect_personaje.height:
        rect_personaje.y = ALTO_VENTANA - rect_personaje.height

    pantalla.fill(COLOR_ROSA)

    pygame.draw.rect(pantalla, (0, 0, 255), rect_personaje)
    pantalla.blit(imagen, rect_personaje)

    if mostrar_imagen_2:
        rect_2 = disparar(rect_x, rect_y)
        if derecha:
            rect_x += 5
        if izquierda:
            rect_x -= 5
        if arriba:
            rect_y -= 5
        if abajo:
            rect_y += 5
        pantalla.blit(imagen_2, rect_2)

        if rect_x >= ANCHO_VENTANA or rect_x <= 0 or rect_y <= 0 or rect_y >= ALTO_VENTANA:
            mostrar_imagen_2 = False
            derecha = False
            izquierda = False
            arriba = False
            abajo = False

    pygame.display.flip()

pygame.quit()

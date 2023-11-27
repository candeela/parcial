import pygame
from constantes import *
from Personaje import Personaje

pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("juego")



flag_correr = True
flag_vivo = True
flag_vivo_2 = True
mostrar_imagen_2 = False
mostrar_bala = True
derecha = False
izquierda = False
arriba = False
abajo = False
posicion_imagen_enemigo = -100
posicion_imagen_enemigo_2 = -100
puntos = 0  


fuente = pygame.font.SysFont("Arial", 25)
texto_puntos = fuente.render("Score: "+ str(puntos),True, COLOR_GRIS)

imagen = pygame.image.load("perro.jpg")
imagen = pygame.transform.scale(imagen, (100, 100))
rect_personaje = imagen.get_rect()
rect_personaje.x = 368
rect_personaje.y = 389

personaje = Personaje( 368,389,100,100)


rect_x = rect_personaje.x 
rect_y = rect_personaje.y

imagen_2 = pygame.image.load("disparo.png")
imagen_2 = pygame.transform.scale(imagen_2, (50, 50))

imagen_enemigo = pygame.image.load("bala.jpg")
imagen_enemigo = pygame.transform.scale(imagen_enemigo, (100, 100))
rect_enemigo = imagen.get_rect()
rect_enemigo.x = 1000
rect_enemigo.y = 100


imagen_enemigo_2 = pygame.image.load("bala.jpg")
imagen_enemigo_2 = pygame.transform.scale(imagen_enemigo, (100, 100))
rect_enemigo_2 = imagen.get_rect()
rect_enemigo_2.x = 1000
rect_enemigo_2.y = 500

def disparar(posicion_x,posicion_y):
    rect_bala = pygame.Rect(posicion_x,posicion_y,100,100)
    print(rect_bala)
    return rect_bala



while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            lista_posicion = list(evento.pos)
            rect_personaje[0]= lista_posicion[0]
            rect_personaje[1]= lista_posicion[1]
            rect_x = rect_personaje[0]
            rect_y = rect_personaje[1]

            #print(lista_posicion)

    lista_teclas = pygame.key.get_pressed()
    if True in lista_teclas:
        if mostrar_bala:
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


    if rect_personaje.x < 0:
        rect_personaje.x = 0
    elif rect_personaje.x > ANCHO_VENTANA:
        rect_personaje.x = ANCHO_VENTANA

    if rect_personaje.y < 0:
        rect_personaje.y = 0
    elif rect_personaje.y > ALTO_VENTANA:
        rect_personaje.y = ALTO_VENTANA


    pantalla.fill(COLOR_ROSA)#blitear la pantalla
    pantalla.blit(texto_puntos,(100,100))#blitear los puntos  

    if flag_vivo == True:
        posicion_imagen_enemigo += 5  # velocidad de movimiento
        rect_enemigo.x = posicion_imagen_enemigo
        pantalla.blit(imagen_enemigo, rect_enemigo)

    # Cuando llega al borde de la pantalla, oculta la imagen 2
        if rect_enemigo.x >= ANCHO_VENTANA:
            rect_enemigo.x = -100  # Restablece la posición de la imagen 2
            posicion_imagen_enemigo = -100  # Restablece la posición progresiva

    if flag_vivo_2 == True:
        posicion_imagen_enemigo_2 += 5  # Ajusta la velocidad de movimiento
        rect_enemigo_2.x = posicion_imagen_enemigo_2
        pantalla.blit(imagen_enemigo_2, rect_enemigo_2)

    # Cuando llega al borde de la pantalla, oculta la imagen 2
        if rect_enemigo_2.x >= ANCHO_VENTANA:
            rect_enemigo_2.x = -100  
            posicion_imagen_enemigo_2 = -100  

    pygame.draw.rect(pantalla, (0, 0, 255), rect_personaje)
    pantalla.blit(personaje.imagen, rect_personaje)

    if mostrar_imagen_2 == True:
        rect_2 = disparar(rect_x,rect_y)
        if derecha:# Mueve la bala a la derecha
            rect_x += 10
            #print('problema if derecha')
        if izquierda:
            rect_x -= 10
            #print('problema if izquierda')
        if arriba:
            rect_y -= 10
            #print('problema if arriba')
        if abajo:
            rect_y += 10
            #print('problema if abajo')
        pantalla.blit(imagen_2, rect_2)

        rect_2_y = rect_2.y
        rect_2_x = rect_2.x

        if rect_2_y <= 0 :
            print("hola")
            bala = disparar(rect_x,rect_y)

        if rect_y <= 0 or rect_y >= ALTO_VENTANA or rect_x <= 0 or rect_x <= 0: #definir los limites del enemigo 1
            mostrar_imagen_2 = False
            arriba = False
            abajo = False
            derecha = False 
            izquierda = False

        if rect_2.colliderect(rect_enemigo) and flag_vivo:
            flag_vivo = False
            puntos = puntos + 10
            texto_puntos = fuente.render("Score: "+ str(puntos),True, COLOR_GRIS)


    pygame.display.flip()

pygame.quit()
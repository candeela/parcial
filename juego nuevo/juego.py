import pygame
from constantes import *



'''flag_vivo = True'''

pygame.init()#inicia el juego
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))#crear la pantalla
pygame.display.set_caption("juego")#nombre del juego 

imagen = pygame.image.load("perro.jpg")#carga la imagen
imagen_2 = pygame.image.load("bala.jpg")
imagen_2 = pygame.transform.scale(imagen_2,(100,100))
rect_2 = pygame.Rect((30,100,101,101))

'''imagen_2 = pygame.image.load("imagen.png")'''
imagen = pygame.transform.scale(imagen,(100,100))# cambiar el tamaño de la imagen
rect_personaje = pygame.Rect((30,100,101,101))#rect del personaje

'''imagen_2 = pygame.transform.scale(imagen_2,(50,50))'''
'''rect_2 = imagen_2.get_rect()
rect_2.x = 300
#arriba o abajo
rect_2.y = 300'''




flag_correr = True #variable
perro_2 = False

while flag_correr:#bucle para empezar
    lista_eventos = pygame.event.get()#lista de eventos
    for evento in lista_eventos:#for para ver que evento es 
        if evento.type == pygame.QUIT:#cierra
            flag_correr = False


        if evento.type == pygame.MOUSEBUTTONDOWN:#mueve la imagen a donde se hizo click 
            lista_posicion = list(evento.pos)
            rect_personaje[0]= lista_posicion[0]
            rect_personaje[1]= lista_posicion[1]

            posicion_click = list(evento.pos)
            print(posicion_click)

    
    lista_teclas = pygame.key.get_pressed()#devuelve lista de t y f donde dice q tecla se presiona
    if True in lista_teclas:
            if lista_teclas[pygame.K_RIGHT]:
                perro_2 = True

            if lista_teclas[pygame.K_UP]:
                perro_2 = True






    pantalla.fill((255, 192, 203))
    pygame.draw.rect(pantalla,(0,0,255),rect_personaje)
    pantalla.blit(imagen,rect_personaje)

#iria aca 
    if perro_2 == True:
        pantalla.blit(imagen_2,rect_2)
        while rect_2.x <800:
            rect_2.x = rect_2.x + 5
            if rect_2.x >=800:
                perro_2 = False

    if rect_personaje[0] <0:
        rect_personaje[0] = 0

    elif rect_personaje[0] >800:
        rect_personaje[0] = 800

    if rect_personaje[1]<0:
        rect_personaje[1] = 0

    elif rect_personaje[1] >600:
        rect_personaje[1] = 600

    pygame.display.flip()

pygame.quit()

''' if rect_personaje.colliderect(rect_2):
        flag_vivo = False

    if flag_vivo:
        rect_2.x += velocidad_x
        rect_2.y += velocidad_y

        # Si imagen_2 alcanza los bordes de la ventana, cambia de dirección
        if rect_2.left < 0 or rect_2.right > ANCHO_VENTANA:
            velocidad_x = -velocidad_x
        if rect_2.top < 0 or rect_2.bottom > ALTO_VENTANA:
            velocidad_y = -velocidad_y'''






'''pygame.draw.rect(pantalla,(0,0,255),rect_2)
    pantalla.blit(imagen,rect_2)'''
import pygame
from constantes import *
from Personaje import Personaje
from Enemigos import Enemigos
from TextBox import TextBox1
from Estado_juego import Estado_juego
import json


pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("juego")

def imagen_fondo():
    imagen_fondo = pygame.image.load("fondo.png")
    imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
    return imagen_fondo
def fin_juego(estado_juego):
    flag_ejecutar_fin_juego = True
    while flag_ejecutar_fin_juego:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                flag_ejecutar_fin_juego = False
        
        pygame.display.set_caption("JUEGO")
        imagen_fondo()
        fuente = pygame.font.SysFont("Arial", 100)
        texto_ganaste= fuente.render("Ganaste ",True, COLOR_AZUL)
        imagen = imagen_fondo()
        pantalla.blit(imagen,imagen.get_rect())
        pantalla.blit(texto_ganaste,(250,300))
        estado_juego.actualizar_progreso()
        estado_juego.guardar_progreso()
        pygame.display.flip()
    pygame.quit()

def fin_nivel_tres (estado_juego):
    pygame.display.set_caption("JUEGO")
    fuente = pygame.font.SysFont("Arial", 100)
    texto_perdiste = fuente.render("Game over ",True, COLOR_AZUL)
    imagen = imagen_fondo()
    pantalla.blit(imagen,imagen.get_rect())
    pantalla.blit(texto_perdiste,(250,300))
    estado_juego.actualizar_progreso()
    estado_juego.guardar_progreso()
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()

def siguiente_nivel(proximo_nivel,estado_juego):
    pygame.display.set_caption("JUEGO")
    imagen = imagen_fondo()
    fuente = pygame.font.SysFont("Arial", 50)
    texto_ganaste = fuente.render("Ganaste este nivel ",True, COLOR_AZUL)
    pantalla.blit(imagen,imagen.get_rect())
    pantalla.blit(texto_ganaste,(250,300))
    pygame.display.flip()
    pygame.time.delay(3000)
    proximo_nivel(estado_juego)

def fin_nivel (siguiente_nivel,estado_juego):
    pygame.display.set_caption("JUEGO")
    imagen = imagen_fondo()
    fuente = pygame.font.SysFont("Arial", 50)
    texto_perdiste = fuente.render("Perdiste este nivel ",True, COLOR_AZUL)
    pantalla.blit(imagen,imagen.get_rect())
    pantalla.blit(texto_perdiste,(250,300))
    pygame.display.flip()
    pygame.time.delay(3000)
    siguiente_nivel(estado_juego)

def jugar_nivel_3(estado_juego):
    flag_ejecutar_jugar_nivel_3 = True

    while flag_ejecutar_jugar_nivel_3:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                flag_ejecutar_jugar_nivel_3 = False

            imagen_fondo = pygame.image.load("noche5.jpg")
            imagen_fondo= pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
            pygame.display.set_caption("juego")

            flag_correr = True  # bandera inical del juego
            flag_vivo = True  #bandera enemigo 1
            flag_vivo_2 = True #bandera enemigo 2
            flag_vivo_3 = True  #bandera enemigo 3
            flag_vivo_4 = True
            mostrar_bala = False #bandera bala
            derecha = False
            izquierda = False
            arriba = False
            abajo = False
            fin_tiempo = False
            posicion_imagen_enemigo = -10
            posicion_imagen_enemigo_2 = -10
            posicion_imagen_enemigo_3 = -10
            posicion_imagen_enemigo_4 = -10
            segundos = 30
            lista_explosion = []
            i = 0 
            sonido_explosion = pygame.mixer.Sound("laser.mp3")

            timer = pygame.USEREVENT
            pygame.time.set_timer(timer,1000)

            fuente = pygame.font.SysFont("Arial", 25)
            texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_GRIS)

            personaje = Personaje( 368,389,100,100)

            rect_x = personaje.rect.x 
            rect_y = personaje.rect.y

            bala = pygame.image.load("disparo.png")
            bala = pygame.transform.scale(bala, (40, 40))

            enemigo_1 = Enemigos(90,100,90,80)
            enemigo_2 = Enemigos(100,500, 90,80)
            enemigo_3 = Enemigos(100,0, 90,80)
            enemigo_4 = Enemigos(600,0, 90,80)

            def disparar(posicion_x,posicion_y):
                rect_bala_funcion = pygame.Rect(posicion_x,posicion_y,50,50)
                return rect_bala_funcion

            while flag_correr:
                lista_eventos = pygame.event.get()
                for evento in lista_eventos:
                    #salir
                    if evento.type == pygame.QUIT:
                        flag_correr = False

                    if evento.type == pygame.USEREVENT:
                        if evento.type == timer:
                            if fin_tiempo == False:
                                segundos = segundos - 1
                                if segundos == 0:
                                    fin_tiempo = True

                    #movimiento del pesonaje
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        lista_posicion = list(evento.pos)
                        personaje.rect[0]= lista_posicion[0]
                        personaje.rect[1]= lista_posicion[1]
                        rect_x = personaje.rect[0]
                        rect_y = personaje.rect[1]

                lista_teclas = pygame.key.get_pressed()
                if True in lista_teclas:
                    rect_bala = disparar(personaje.rect.x, personaje.rect.y)

                    if lista_teclas[pygame.K_RIGHT]:
                            mostrar_bala = True
                            derecha = True
                            sonido_explosion.play()

                    if lista_teclas[pygame.K_LEFT]:
                            mostrar_bala = True
                            izquierda = True
                            sonido_explosion.play()

                    if lista_teclas[pygame.K_UP]:
                            mostrar_bala = True
                            arriba = True
                            sonido_explosion.play()

                    if lista_teclas[pygame.K_DOWN]:
                            mostrar_bala = True
                            abajo = True
                            sonido_explosion.play()

                # limites del personaje
                if personaje.rect.x < 0:
                    personaje.rect.x = 0
                elif personaje.rect.x > 795:
                    personaje.rect.x = 795

                if personaje.rect.y <0:
                    personaje.rect.y = 0
                elif personaje.rect.y > 575:
                    personaje.rect.y = 575

                texto_timer = fuente.render("Tiempo: "+ str(segundos),True, COLOR_GRIS)
                pantalla.blit(imagen_fondo,imagen_fondo.get_rect())#blitear la pantalla
                pantalla.blit(texto_puntos,(50,50))#blitear los puntos 
                pantalla.blit(texto_timer,(600,50))

                if flag_vivo == True:#enemigo 1
                    posicion_imagen_enemigo += 3 # velocidad de movimiento
                    enemigo_1.rect.x = posicion_imagen_enemigo
                    pantalla.blit(enemigo_1.imagen, enemigo_1.rect)

                # Cuando llega al borde de la pantalla vuelve a empezar
                    if enemigo_1.rect.x >= ANCHO_VENTANA:
                        enemigo_1.rect.x= -10 # Restablece la posición de la imagen 2
                        posicion_imagen_enemigo = -10  # Restablece la posición progresiva

                if flag_vivo_2 == True:
                    posicion_imagen_enemigo_2 += 3  # Ajusta la velocidad de movimiento
                    enemigo_2.rect.x = posicion_imagen_enemigo_2
                    pantalla.blit(enemigo_2.imagen, enemigo_2.rect)

                # Cuando llega al borde de la pantalla vuelve a empezar 
                    if enemigo_2.rect.x >= ANCHO_VENTANA:
                        enemigo_2.rect.x = -10 
                        posicion_imagen_enemigo_2 = -10 

                if flag_vivo_3 == True:#enemigo 1
                    posicion_imagen_enemigo_3 += 3 # velocidad de movimiento
                    enemigo_3.rect.y = posicion_imagen_enemigo_3
                    pantalla.blit(enemigo_3.imagen, enemigo_3.rect)

                # Cuando llega al borde de la pantalla vuelve a empezar
                    if enemigo_3.rect.y >= ALTO_VENTANA:
                        enemigo_3.rect.y = -1 # Restablece la posición de la imagen 
                        posicion_imagen_enemigo_3 = -1 #  posición progresiva

                if flag_vivo_4 == True:#enemigo 1
                    posicion_imagen_enemigo_4 += 3 # velocidad de movimiento
                    enemigo_4.rect.y = posicion_imagen_enemigo_4
                    pantalla.blit(enemigo_4.imagen, enemigo_4.rect)

                    if enemigo_4.rect.y >= ALTO_VENTANA:
                        enemigo_4.rect.y = -1 
                        posicion_imagen_enemigo_4 = -1 

                pantalla.blit(personaje.imagen, personaje.rect)

                if mostrar_bala == True:
                    if derecha:# Mueve la bala a la derecha
                        rect_bala.x += 10
                    if izquierda:
                        rect_bala.x -= 10
                    if arriba:
                        rect_bala.y -= 10
                    if abajo:
                        rect_bala.y += 10

                    pantalla.blit(bala, rect_bala)
                    if rect_bala.y <= 0 or rect_bala.y >= ALTO_VENTANA or rect_bala.x <= 0 or rect_bala.x >= ANCHO_VENTANA:
                        mostrar_bala = False
                        arriba = False
                        abajo = False
                        derecha = False 
                        izquierda = False
                        rect_bala = disparar(personaje.rect.x, personaje.rect.y)

                    if rect_y <= 0 or rect_y >= ALTO_VENTANA or rect_x <= 0 or rect_x <= 0: #definir los limites del enemigo 1
                        mostrar_bala = False
                        arriba = False
                        abajo = False
                        derecha = False 
                        izquierda = False

                    for i in range (14):
                        path =  str(i) + ".png"
                        imagen_explosion = pygame.image.load(path)
                        imagen_explosion = pygame.transform.scale(imagen_explosion, (110, 110))
                        rect_explosion = imagen_explosion.get_rect()
                        rect_explosion.x = 200 #left en pixeles
                        rect_explosion.y = 400 #top en pixeles

                        dic_explosion = {"imagen": imagen_explosion, "rect": rect_explosion}
                        lista_explosion.append(dic_explosion)


                    if rect_bala.colliderect(enemigo_1.rect) and flag_vivo: #verifica si hay colicion con enemigo 1
                        flag_vivo = False
                        
                        for i in range(14):
                            lista_explosion[i]["rect"].x = enemigo_1.rect.x
                            lista_explosion[i]["rect"].y = enemigo_1.rect.y

                        for i in range(14):
                            pantalla.blit(lista_explosion[i]["imagen"], lista_explosion[i]["rect"])
                            pygame.display.flip()  
                            pygame.time.delay(25) 

                        estado_juego.puntaje += 10
                        texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_GRIS)

                    if rect_bala.colliderect(enemigo_2.rect) and flag_vivo_2: #verifica si hay colicion con enemigo 2
                        flag_vivo_2 = False

                        for i in range(14):
                            lista_explosion[i]["rect"].x = enemigo_2.rect.x
                            lista_explosion[i]["rect"].y = enemigo_2.rect.y
                        for i in range(14):
                            pantalla.blit(lista_explosion[i]["imagen"], lista_explosion[i]["rect"])
                            pygame.display.flip()  # Actualiza la pantalla para que se muestre la explosión
                            pygame.time.delay(25) 

                        estado_juego.puntaje += 10
                        texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_GRIS)

                    if rect_bala.colliderect(enemigo_3.rect) and flag_vivo_3: #verifica si hay colicion con enemigo 2
                        flag_vivo_3 = False

                        for i in range(14):
                            lista_explosion[i]["rect"].x = enemigo_3.rect.x
                            lista_explosion[i]["rect"].y = enemigo_3.rect.y
                        for i in range(14):
                            pantalla.blit(lista_explosion[i]["imagen"], lista_explosion[i]["rect"])
                            pygame.display.flip()  # Actualiza la pantalla para que se muestre la explosión
                            pygame.time.delay(25) 

                        estado_juego.puntaje +=  10
                        texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_GRIS)

                    if rect_bala.colliderect(enemigo_4.rect) and flag_vivo_4: #verifica si hay colicion con enemigo 3
                        flag_vivo_4 = False

                        for i in range(14):
                            lista_explosion[i]["rect"].x = enemigo_4.rect.x
                            lista_explosion[i]["rect"].y = enemigo_4.rect.y
                        for i in range(14):
                            pantalla.blit(lista_explosion[i]["imagen"], lista_explosion[i]["rect"])
                            pygame.display.flip()  # Actualiza la pantalla para que se muestre la explosión
                            pygame.time.delay(25) 

                        estado_juego.puntaje +=  10
                        texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_GRIS)

                if segundos == 0:
                    fin_nivel_tres(estado_juego)

                if flag_vivo == False and flag_vivo_2 == False and flag_vivo_3 == False and flag_vivo_4 == False:
                    fin_juego(estado_juego)

                pygame.display.flip()

            pygame.quit()

def  jugar_nivel_dos(estado_juego):
    flag_ejecutar_jugar_nivel_2 = True

    while flag_ejecutar_jugar_nivel_2:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                flag_ejecutar_jugar_nivel_2 = False

            imagen_fondo = pygame.image.load("noche3.jpg")
            imagen_fondo= pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
            pygame.display.set_caption("juego")

            flag_correr = True  # bandera inical del juego
            flag_vivo = True  #bandera enemigo 1
            flag_vivo_2 = True #bandera enemigo 2
            flag_vivo_3 = True  #bandera enemigo 3
            mostrar_bala = False #bandera bala
            derecha = False
            izquierda = False
            arriba = False
            abajo = False
            fin_tiempo = False
            posicion_imagen_enemigo = -10
            posicion_imagen_enemigo_2 = -10
            posicion_imagen_enemigo_3 = -10
            segundos = 30
            lista_explosion = []
            i = 0 
            sonido_explosion = pygame.mixer.Sound("laser.mp3")

            timer = pygame.USEREVENT
            pygame.time.set_timer(timer,1000)

            fuente = pygame.font.SysFont("Arial", 25)
            texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_GRIS)

            personaje = Personaje( 368,389,100,100)

            rect_x = personaje.rect.x 
            rect_y = personaje.rect.y

            bala = pygame.image.load("disparo.png")
            bala = pygame.transform.scale(bala, (40, 40))

            enemigo_1 = Enemigos(90,100,90,80)
            enemigo_2 = Enemigos(100,500, 90,80)
            enemigo_3 = Enemigos(100,350, 90,80)
            enemigo_3 = Enemigos(100,250, 90,80)

            def disparar(posicion_x,posicion_y):
                rect_bala_funcion = pygame.Rect(posicion_x,posicion_y,50,50)
                return rect_bala_funcion

            while flag_correr:
                lista_eventos = pygame.event.get()
                for evento in lista_eventos:
                    #salir
                    if evento.type == pygame.QUIT:
                        flag_correr = False

                    if evento.type == pygame.USEREVENT:
                        if evento.type == timer:
                            if fin_tiempo == False:
                                segundos = segundos - 1
                                if segundos == 0:
                                    fin_tiempo = True

                    #movimiento del personaje
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        lista_posicion = list(evento.pos)
                        personaje.rect[0]= lista_posicion[0]
                        personaje.rect[1]= lista_posicion[1]
                        rect_x = personaje.rect[0]
                        rect_y = personaje.rect[1]

                lista_teclas = pygame.key.get_pressed()
                if True in lista_teclas:
                    rect_bala = disparar(personaje.rect.x, personaje.rect.y)

                    if lista_teclas[pygame.K_RIGHT]:
                            mostrar_bala = True
                            derecha = True
                            sonido_explosion.play()

                    if lista_teclas[pygame.K_LEFT]:
                            mostrar_bala = True
                            izquierda = True
                            sonido_explosion.play()

                    if lista_teclas[pygame.K_UP]:
                            mostrar_bala = True
                            arriba = True
                            sonido_explosion.play()

                    if lista_teclas[pygame.K_DOWN]:
                            mostrar_bala = True
                            abajo = True
                            sonido_explosion.play()

                # limites del personaje
                if personaje.rect.x < 0:
                    personaje.rect.x = 0
                elif personaje.rect.x > 795:
                    personaje.rect.x = 795

                if personaje.rect.y <0:
                    personaje.rect.y = 0
                elif personaje.rect.y > 575:
                    personaje.rect.y = 575

                texto_timer = fuente.render("Tiempo: "+ str(segundos),True, COLOR_GRIS)
                pantalla.blit(imagen_fondo,imagen_fondo.get_rect())
                pantalla.blit(texto_puntos,(50,50))#blitear los puntos 
                pantalla.blit(texto_timer,(600,50))

                if flag_vivo == True:#enemigo 1
                    posicion_imagen_enemigo += 5 # velocidad de movimiento
                    enemigo_1.rect.x = posicion_imagen_enemigo
                    pantalla.blit(enemigo_1.imagen, enemigo_1.rect)

                
                    if enemigo_1.rect.x >= ANCHO_VENTANA:
                        enemigo_1.rect.x= -10 
                        posicion_imagen_enemigo = -10  

                if flag_vivo_2 == True:
                    posicion_imagen_enemigo_2 += 5  # velocidad de movimiento
                    enemigo_2.rect.x = posicion_imagen_enemigo_2
                    pantalla.blit(enemigo_2.imagen, enemigo_2.rect)

                # Cuando llega al borde de la pantalla vuelve a empezar 
                    if enemigo_2.rect.x >= ANCHO_VENTANA:
                        enemigo_2.rect.x = -10 
                        posicion_imagen_enemigo_2 = -10 

                if flag_vivo_3 == True:
                    posicion_imagen_enemigo_3 += 5 
                    enemigo_3.rect.y = posicion_imagen_enemigo_3
                    pantalla.blit(enemigo_3.imagen, enemigo_3.rect)

                    if enemigo_3.rect.y >= ALTO_VENTANA:
                        enemigo_3.rect.y = -1 
                        posicion_imagen_enemigo_3 = -1 

                pantalla.blit(personaje.imagen, personaje.rect)

                if mostrar_bala == True:
                    if derecha:# Mueve la bala a la derecha
                        rect_bala.x += 10
                    if izquierda:
                        rect_bala.x -= 10
                    if arriba:
                        rect_bala.y -= 10
                    if abajo:
                        rect_bala.y += 10

                    pantalla.blit(bala, rect_bala)
                    if rect_bala.y <= 0 or rect_bala.y >= ALTO_VENTANA or rect_bala.x <= 0 or rect_bala.x >= ANCHO_VENTANA:
                        mostrar_bala = False
                        arriba = False
                        abajo = False
                        derecha = False 
                        izquierda = False
                        rect_bala = disparar(personaje.rect.x, personaje.rect.y)

                    if rect_y <= 0 or rect_y >= ALTO_VENTANA or rect_x <= 0 or rect_x <= 0: #definir los limites del enemigo 1
                        mostrar_bala = False
                        arriba = False
                        abajo = False
                        derecha = False 
                        izquierda = False

                    for i in range (14):
                        path =  str(i) + ".png"
                        imagen_explosion = pygame.image.load(path)
                        imagen_explosion = pygame.transform.scale(imagen_explosion, (110, 110))
                        rect_explosion = imagen_explosion.get_rect()
                        rect_explosion.x = 200 #left en pixeles
                        rect_explosion.y = 400 #top en pixeles

                        dic_explosion = {"imagen": imagen_explosion, "rect": rect_explosion}
                        lista_explosion.append(dic_explosion)

                    if rect_bala.colliderect(enemigo_1.rect) and flag_vivo: #verifica si hay colicion con enemigo 1
                        flag_vivo = False
                        
                        for i in range(14):
                            lista_explosion[i]["rect"].x = enemigo_1.rect.x
                            lista_explosion[i]["rect"].y = enemigo_1.rect.y

                        for i in range(14):
                            pantalla.blit(lista_explosion[i]["imagen"], lista_explosion[i]["rect"])
                            pygame.display.flip()  
                            pygame.time.delay(25) 

                        estado_juego.puntaje += 10
                        texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_GRIS)

                    if rect_bala.colliderect(enemigo_2.rect) and flag_vivo_2: #verifica si hay colicion con enemigo 2
                        flag_vivo_2 = False

                        for i in range(14):
                            lista_explosion[i]["rect"].x = enemigo_2.rect.x
                            lista_explosion[i]["rect"].y = enemigo_2.rect.y
                        for i in range(14):
                            pantalla.blit(lista_explosion[i]["imagen"], lista_explosion[i]["rect"])
                            pygame.display.flip()  # Actualiza la pantalla para que se muestre la explosión
                            pygame.time.delay(25) 

                        estado_juego.puntaje += 10
                        texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_GRIS)

                    if rect_bala.colliderect(enemigo_3.rect) and flag_vivo_3: #verifica si hay colicion con enemigo 3
                        flag_vivo_3 = False

                        for i in range(14):
                            lista_explosion[i]["rect"].x = enemigo_3.rect.x
                            lista_explosion[i]["rect"].y = enemigo_3.rect.y
                        for i in range(14):
                            pantalla.blit(lista_explosion[i]["imagen"], lista_explosion[i]["rect"])
                            pygame.display.flip()  
                            pygame.time.delay(25) 

                        estado_juego.puntaje += 10
                        texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_GRIS)

                if segundos == 0:
                    fin_nivel(jugar_nivel_3,estado_juego)

                if flag_vivo == False and flag_vivo_2 == False and flag_vivo_3 == False:
                    siguiente_nivel(jugar_nivel_3,estado_juego)

                pygame.display.flip()

            pygame.quit()

def jugar_nivel_uno(estado_juego):
    flag_ejecutar_jugar = True

    while flag_ejecutar_jugar:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                flag_ejecutar_jugar = False

            pygame.init()
            pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
            imagen_fondo = pygame.image.load("noche1.jpg")
            imagen_fondo= pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
            pygame.display.set_caption("juego")

            flag_correr = True  # bandera inical del juego
            flag_vivo = True  #bandera enemigo 1
            flag_vivo_2 = True #bandera enemigo 2
            mostrar_bala = False #bandera bala
            derecha = False
            izquierda = False
            arriba = False
            abajo = False
            fin_tiempo = False
            posicion_imagen_enemigo = -10
            posicion_imagen_enemigo_2 = -10
            segundos = 20
            lista_explosion = []
            i = 0 
            sonido_explosion = pygame.mixer.Sound("laser.mp3")

            timer = pygame.USEREVENT #TIMER
            pygame.time.set_timer(timer,1000)

            fuente = pygame.font.SysFont("Arial", 25)
            texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_BLANCO)#PUNTOS

            personaje = Personaje( 368,389,100,100)
            rect_x = personaje.rect.x 
            rect_y = personaje.rect.y

            bala = pygame.image.load("disparo.png")
            bala = pygame.transform.scale(bala, (40, 40))

            enemigo_1 = Enemigos(90,100,90,80)
            enemigo_2 = Enemigos(100,500, 90,80)

            def disparar(posicion_x,posicion_y):
                rect_bala_funcion = pygame.Rect(posicion_x,posicion_y,50,50)
                return rect_bala_funcion

            while flag_correr:
                lista_eventos = pygame.event.get()
                for evento in lista_eventos:
                    #salir
                    if evento.type == pygame.QUIT:
                        flag_correr = False

                    if evento.type == pygame.USEREVENT:
                        if evento.type == timer:
                            if fin_tiempo == False:
                                segundos = segundos - 1
                                if segundos == 0:
                                    fin_tiempo = True

                    #movimiento del pesonaje
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        lista_posicion = list(evento.pos)
                        personaje.rect[0]= lista_posicion[0]
                        personaje.rect[1]= lista_posicion[1]
                        rect_x = personaje.rect[0]
                        rect_y = personaje.rect[1]

                lista_teclas = pygame.key.get_pressed()
                if True in lista_teclas:
                    rect_bala = disparar(personaje.rect.x, personaje.rect.y)

                    if lista_teclas[pygame.K_RIGHT]:
                            mostrar_bala = True
                            derecha = True
                            sonido_explosion.play()

                    if lista_teclas[pygame.K_LEFT]:
                            mostrar_bala = True
                            izquierda = True
                            sonido_explosion.play()

                    if lista_teclas[pygame.K_UP]:
                            mostrar_bala = True
                            arriba = True
                            sonido_explosion.play()

                    if lista_teclas[pygame.K_DOWN]:
                            mostrar_bala = True
                            abajo = True
                            sonido_explosion.play()

                # limites del personaje
                if personaje.rect.x < 0:
                    personaje.rect.x = 0
                elif personaje.rect.x > 795:
                    personaje.rect.x = 795

                if personaje.rect.y <0:
                    personaje.rect.y = 0
                elif personaje.rect.y > 575:
                    personaje.rect.y = 575

                texto_timer = fuente.render("Tiempo: "+ str(segundos),True, COLOR_BLANCO)
                pantalla.blit(imagen_fondo,imagen_fondo.get_rect())
                imagen_fondo = pygame.image.load("noche1.jpg")
                imagen_fondo= pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
                pantalla.blit(texto_puntos,(50,50))#blitear los puntos 
                pantalla.blit(texto_timer,(600,50))

                if flag_vivo == True:#enemigo 1
                    posicion_imagen_enemigo += 7 # velocidad de movimiento
                    enemigo_1.rect.x = posicion_imagen_enemigo
                    pantalla.blit(enemigo_1.imagen, enemigo_1.rect)

                # Cuando llega al borde de la pantalla vuelve a empezar
                    if enemigo_1.rect.x >= ANCHO_VENTANA:
                        enemigo_1.rect.x= -10 # Restablece la posición de la 
                        posicion_imagen_enemigo = -10  #  posición progresiva

                if flag_vivo_2 == True:
                    posicion_imagen_enemigo_2 += 7  #  velocidad de movimiento
                    enemigo_2.rect.x = posicion_imagen_enemigo_2
                    pantalla.blit(enemigo_2.imagen, enemigo_2.rect)

                    if enemigo_2.rect.x >= ANCHO_VENTANA:
                        enemigo_2.rect.x = -10 
                        posicion_imagen_enemigo_2 = -10 

                pantalla.blit(personaje.imagen, personaje.rect)

                if mostrar_bala == True:
                    
                    if derecha:# Mueve la bala a la derecha
                        rect_bala.x += 10
                    if izquierda:
                        rect_bala.x -= 10
                    if arriba:
                        rect_bala.y -= 10
                    if abajo:
                        rect_bala.y += 10

                    pantalla.blit(bala, rect_bala)
                    if rect_bala.y <= 0 or rect_bala.y >= ALTO_VENTANA or rect_bala.x <= 0 or rect_bala.x >= ANCHO_VENTANA:
                        mostrar_bala = False
                        arriba = False
                        abajo = False
                        derecha = False 
                        izquierda = False
                        rect_bala = disparar(personaje.rect.x, personaje.rect.y)

                    if rect_y <= 0 or rect_y >= ALTO_VENTANA or rect_x <= 0 or rect_x <= 0: #definir los limites del enemigo 1
                        mostrar_bala = False
                        arriba = False
                        abajo = False
                        derecha = False 
                        izquierda = False

                    for i in range (14):
                        path =  str(i) + ".png"
                        imagen_explosion = pygame.image.load(path)
                        imagen_explosion = pygame.transform.scale(imagen_explosion, (110, 110))
                        rect_explosion = imagen_explosion.get_rect()
                        rect_explosion.x = 200 #left en pixeles
                        rect_explosion.y = 400 #top en pixeles

                        dic_explosion = {"imagen": imagen_explosion, "rect": rect_explosion}
                        lista_explosion.append(dic_explosion)

                    if rect_bala.colliderect(enemigo_1.rect) and flag_vivo: #verifica si hay colicion 
                        flag_vivo = False
                        
                        for i in range(14):
                            lista_explosion[i]["rect"].x = enemigo_1.rect.x
                            lista_explosion[i]["rect"].y = enemigo_1.rect.y

                        for i in range(14):
                            pantalla.blit(lista_explosion[i]["imagen"], lista_explosion[i]["rect"])
                            pygame.display.flip()  # Actualiza la pantalla para que se muestre la explosión
                            pygame.time.delay(25) 

                        estado_juego.puntaje += 10
                        texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_BLANCO)

                    if rect_bala.colliderect(enemigo_2.rect) and flag_vivo_2: #verifica si hay colicion con enemigo 2
                        flag_vivo_2 = False

                        for i in range(14):
                            lista_explosion[i]["rect"].x = enemigo_2.rect.x
                            lista_explosion[i]["rect"].y = enemigo_2.rect.y
                        for i in range(14):
                            pantalla.blit(lista_explosion[i]["imagen"], lista_explosion[i]["rect"])
                            pygame.display.flip()  
                            pygame.time.delay(25) 

                        estado_juego.puntaje += 10
                        texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_BLANCO)

                if segundos == 0:
                    fin_nivel(jugar_nivel_dos,estado_juego)

                if flag_vivo == False and flag_vivo_2 == False: 
                    siguiente_nivel(jugar_nivel_dos,estado_juego) 

                pygame.display.flip()

            pygame.quit()

def cargar_nombre(estado_juego) :
    pygame.display.set_caption("Options")
    textbox = TextBox1(150,100,600,400,"Arial","boton.png")

    flag_ejecutar_opciones = True 

    while flag_ejecutar_opciones:
        lista_evento = pygame.event.get()
        for evento in lista_evento:
            if evento.type == pygame.QUIT:
                flag_ejecutar_opciones = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(evento.pos)

                if posicion_click[0] > 580 and posicion_click[0] < 780 and 500 < posicion_click[1] < 600:
                    estado_juego.nombre = textbox.obtener_texto()
                    estado_juego.guardar_progreso()
                    print(f"Texto ingresado: {estado_juego.nombre}")
                    jugar_nivel_uno(estado_juego)

        pantalla.fill(COLOR_AZUL)
        pygame.draw.rect(pantalla, COLOR_BOTONES, (580, 500, 200, 100))
        fuente = pygame.font.SysFont("Arial", 25)
        texto_jugar = fuente.render("Jugar", True, COLOR_BLANCO)
        pantalla.blit(texto_jugar, (620, 550))
        textbox.update(pantalla,lista_evento)
        pygame.display.flip()

    pygame.quit()

def ordenar_puntaje(lista: list, clave: str): 
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i][1][clave] < lista[j][1][clave]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista
def ranking():
    pygame.display.set_caption("Options")
    imagen = imagen_fondo()
    flag_ejecutar_ranking = True 

    with open('data.json', 'r') as file:
        datos_ranking = json.load(file)

        lista_ranking = list(datos_ranking.items())
        ranking_ordenado =  ordenar_puntaje(lista_ranking,"puntaje")

    while flag_ejecutar_ranking:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                flag_ejecutar_ranking = False

        pantalla.blit(imagen,imagen.get_rect())
        fuente = pygame.font.SysFont("Gabriola", 60)
        fuente_titulo = pygame.font.SysFont("Gabriola", 80)
        texto_ranking = fuente_titulo.render("Ranking", True, COLOR_NEGRO)
        pantalla.blit(texto_ranking,(350,100))
        y_pos = 250  

        # Mostrar los primeros 5 jugadores en el ranking
        for i in range(5):
            id = i + 1
            nombre = ranking_ordenado[i][0]
            jugador = ranking_ordenado[i][1]
            texto_jugador = fuente.render("{0}. {1}: {2}".format(id,nombre,jugador['puntaje']), True, COLOR_NEGRO)
            pantalla.blit(texto_jugador, (300, y_pos))
            y_pos += 50  

        pygame.display.flip()

    pygame.quit()

def menu():
    pygame.display.set_caption("menu")
    flag_ejecutar_menu = True
    imagen = imagen_fondo()
    pantalla.blit(imagen,imagen.get_rect())
    estado_juego = Estado_juego()

    while flag_ejecutar_menu:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                flag_ejecutar_menu = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(evento.pos)

                if posicion_click[0] > 580 and posicion_click[0] < 780 and 100 < posicion_click[1] < 200:
                    ranking()
                if posicion_click[0] > 580 and posicion_click[0] < 780 and 300 < posicion_click[1] < 400:
                    cargar_nombre(estado_juego)

                if posicion_click[0] > 580 and posicion_click[0] < 780 and 500 < posicion_click[1] < 600:
                    flag_ejecutar_menu = False
        
        pygame.draw.rect(pantalla, COLOR_BOTONES, (580, 100, 200, 100))
        pygame.draw.rect(pantalla, COLOR_BOTONES, (580, 300, 200, 100))
        pygame.draw.rect(pantalla, COLOR_BOTONES, (580, 500, 200, 100))
        fuente = pygame.font.SysFont("Arial", 25)
        fuente_titulo = pygame.font.SysFont("Gabriola", 70)
        texto_ranking = fuente.render("Ranking", True, COLOR_BLANCO)
        texto_jugar = fuente.render("Jugar", True, COLOR_BLANCO)
        texto_salir = fuente.render("Salir", True, COLOR_BLANCO)
        texto_nombre_juego = fuente_titulo.render("Galactic Labyrinth", True, COLOR_BLANCO)
        pantalla.blit(texto_ranking, (620, 150))
        pantalla.blit(texto_jugar, (620, 350))
        pantalla.blit(texto_salir, (620, 550))
        pantalla.blit(texto_nombre_juego, (100, 300))
        pygame.display.flip()

menu()
pygame.quit()
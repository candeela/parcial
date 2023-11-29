import pygame
from constantes import *
from Personaje import Personaje
from Enemigos import Enemigos
from TextBox import TextBox1
from Bala import Bala
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

def mostrar_explosion(lista_explosion, enemigo_rect):
    for i in range(14):
        lista_explosion[i]["rect"].x = enemigo_rect.x
        lista_explosion[i]["rect"].y = enemigo_rect.y

    for i in range(14):
        pantalla.blit(lista_explosion[i]["imagen"], lista_explosion[i]["rect"])
        pygame.display.flip()
        pygame.time.delay(25)

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
            fin_tiempo = False
            segundos = 30
            lista_explosion = []
            i = 0 

            timer = pygame.USEREVENT
            pygame.time.set_timer(timer,1000)

            fuente = pygame.font.SysFont("Arial", 25)
            texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_GRIS)

            personaje = Personaje( 368,389,100,100)
            bala = Bala(personaje.rect.x, personaje.rect.y,50,50)
            lista_posicion = [368,389]
            enemigo_1 = Enemigos(90,100,90,80)
            enemigo_2 = Enemigos(100,500, 90,80)
            enemigo_3 = Enemigos(100,0, 90,80)
            enemigo_4 = Enemigos(600,0, 90,80)

            while flag_correr:
                lista_eventos = pygame.event.get()
                for evento in lista_eventos: #salir
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
                        personaje.moverse(lista_posicion)

                lista_teclas = pygame.key.get_pressed()
                if True in lista_teclas:
                    if lista_teclas[pygame.K_RIGHT]:
                            bala.disparar('derecha',lista_posicion)

                    if lista_teclas[pygame.K_LEFT]:
                            bala.disparar('izquierda',lista_posicion)

                    if lista_teclas[pygame.K_UP]:
                            bala.disparar('arriba',lista_posicion)

                    if lista_teclas[pygame.K_DOWN]:
                            bala.disparar('abajo',lista_posicion)

                texto_timer = fuente.render("Tiempo: "+ str(segundos),True, COLOR_GRIS)
                pantalla.blit(imagen_fondo,imagen_fondo.get_rect())#blitear la pantalla
                bala.mover()
                bala.blitear_bala(pantalla)
                personaje.mostrar_personaje(pantalla)
                pantalla.blit(texto_puntos,(50,50))#blitear los puntos 
                pantalla.blit(texto_timer,(600,50))

                if enemigo_1.flag == True:
                    enemigo_1.mover_derecha(3)# velocidad
                    enemigo_1.mostrar_enemigo(pantalla)

                if enemigo_2.flag == True:
                    enemigo_2.mover_derecha(3)# velocidad
                    enemigo_2.mostrar_enemigo(pantalla)

                if enemigo_3.flag == True:
                    enemigo_3.mover_izquierda(3)# velocidad
                    enemigo_3.mostrar_enemigo(pantalla)

                if enemigo_4.flag == True:
                    enemigo_4.mover_izquierda(3)# velocidad
                    enemigo_4.mostrar_enemigo(pantalla)

                for i in range (14):
                        path =  str(i) + ".png"
                        imagen_explosion = pygame.image.load(path)
                        imagen_explosion = pygame.transform.scale(imagen_explosion, (110, 110))
                        rect_explosion = imagen_explosion.get_rect()
                        rect_explosion.x = 200 #left en pixeles
                        rect_explosion.y = 400 #top en pixeles

                        dic_explosion = {"imagen": imagen_explosion, "rect": rect_explosion}
                        lista_explosion.append(dic_explosion)


                if bala.rect.colliderect(enemigo_1.rect) and enemigo_1.flag: #verifica si hay colicion 
                        enemigo_1.flag = False
                        mostrar_explosion(lista_explosion, enemigo_1.rect)

                        estado_juego.puntaje += 10
                        texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_GRIS)

                if bala.rect.colliderect(enemigo_2.rect) and enemigo_2.flag: #verifica si hay colicion 
                        enemigo_2.flag = False
                        mostrar_explosion(lista_explosion, enemigo_2.rect)

                        estado_juego.puntaje += 10
                        texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_GRIS)

                if bala.rect.colliderect(enemigo_3.rect) and enemigo_3.flag: #verifica si hay colicion 
                        enemigo_3.flag = False
                        mostrar_explosion(lista_explosion, enemigo_3.rect)

                        estado_juego.puntaje +=  10
                        texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_GRIS)

                if bala.rect.colliderect(enemigo_4.rect) and enemigo_4.flag:
                        enemigo_4.flag = False
                        mostrar_explosion(lista_explosion, enemigo_4.rect)

                        estado_juego.puntaje +=  10
                        texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_GRIS)

                if segundos == 0:
                    fin_nivel_tres(estado_juego)

                if enemigo_1.flag == False and enemigo_2.flag == False and enemigo_3.flag == False and enemigo_4.flag == False:
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
            fin_tiempo = False
            segundos = 20
            lista_explosion = []
            i = 0 

            timer = pygame.USEREVENT
            pygame.time.set_timer(timer,1000)

            fuente = pygame.font.SysFont("Arial", 25)
            texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_GRIS)

            personaje = Personaje(368,389,100,100)
            bala = Bala(personaje.rect.x, personaje.rect.y,50,50)
            lista_posicion = [368,389]
            enemigo_1 = Enemigos(90,100,90,80)
            enemigo_2 = Enemigos(100,500, 90,80)
            enemigo_3 = Enemigos(100,350, 90,80)
            enemigo_3 = Enemigos(100,250, 90,80)

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
                        personaje.moverse(lista_posicion)

                lista_teclas = pygame.key.get_pressed()
                if True in lista_teclas:
                    if lista_teclas[pygame.K_RIGHT]:
                            bala.disparar('derecha',lista_posicion) 

                    if lista_teclas[pygame.K_LEFT]:
                            bala.disparar('izquierda',lista_posicion) 

                    if lista_teclas[pygame.K_UP]:
                            bala.disparar('arriba',lista_posicion)

                    if lista_teclas[pygame.K_DOWN]:
                            bala.disparar('abajo',lista_posicion) 

                texto_timer = fuente.render("Tiempo: "+ str(segundos),True, COLOR_GRIS)
                pantalla.blit(imagen_fondo,imagen_fondo.get_rect())
                bala.mover()
                bala.blitear_bala(pantalla)
                personaje.mostrar_personaje(pantalla)
                pantalla.blit(texto_puntos,(50,50))
                pantalla.blit(texto_timer,(600,50))

                if enemigo_1.flag == True:
                    enemigo_1.mover_derecha(3)# velocidad
                    enemigo_1.mostrar_enemigo(pantalla)

                if enemigo_2.flag == True:
                        enemigo_2.mover_derecha(3)
                        enemigo_2.mostrar_enemigo(pantalla)

                if enemigo_3.flag == True:
                        enemigo_3.mover_izquierda(3)
                        enemigo_3.mostrar_enemigo(pantalla)

                for i in range (14):
                        path =  str(i) + ".png"
                        imagen_explosion = pygame.image.load(path)
                        imagen_explosion = pygame.transform.scale(imagen_explosion, (110, 110))
                        rect_explosion = imagen_explosion.get_rect()
                        rect_explosion.x = 200 #left en pixeles
                        rect_explosion.y = 400 #top en pixeles

                        dic_explosion = {"imagen": imagen_explosion, "rect": rect_explosion}
                        lista_explosion.append(dic_explosion)

                if bala.rect.colliderect(enemigo_1.rect) and enemigo_1.flag: #verifica si hay colicion con enemigo 1
                        enemigo_1.flag = False
                        mostrar_explosion(lista_explosion, enemigo_1.rect)

                        estado_juego.puntaje += 10
                        texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_GRIS)

                if bala.rect.colliderect(enemigo_2.rect) and enemigo_2.flag: #verifica si hay colicion con enemigo 2
                        enemigo_2.flag= False
                        mostrar_explosion(lista_explosion, enemigo_2.rect)

                        estado_juego.puntaje += 10
                        texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_GRIS)

                if bala.rect.colliderect(enemigo_3.rect) and enemigo_3.flag: #verifica si hay colicion con enemigo 3
                        enemigo_3.flag = False
                        mostrar_explosion(lista_explosion, enemigo_3.rect)

                        estado_juego.puntaje += 10
                        texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_GRIS)

                if segundos == 0:
                    fin_nivel(jugar_nivel_3,estado_juego)

                if enemigo_1.flag == False and enemigo_2.flag == False and enemigo_3.flag == False:
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
            fin_tiempo = False
            segundos = 20
            lista_explosion = []
            i = 0 

            timer = pygame.USEREVENT #TIMER
            pygame.time.set_timer(timer,1000)

            fuente = pygame.font.SysFont("Arial", 25)
            texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_BLANCO)#PUNTOS

            personaje = Personaje( 368,389,100,100)
            bala = Bala(personaje.rect.x, personaje.rect.y,50,50)
            lista_posicion = [368,389]
            enemigo_1 = Enemigos(90,100,90,80)
            enemigo_2 = Enemigos(100,500, 90,80)

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
                        personaje.moverse(lista_posicion)

                lista_teclas = pygame.key.get_pressed()
                if True in lista_teclas:
                    if lista_teclas[pygame.K_RIGHT]:
                            bala.disparar('derecha',lista_posicion)

                    if lista_teclas[pygame.K_LEFT]:
                            bala.disparar('izquierda',lista_posicion) 

                    if lista_teclas[pygame.K_UP]:
                            bala.disparar('arriba',lista_posicion) 

                    if lista_teclas[pygame.K_DOWN]:
                            bala.disparar('abajo',lista_posicion) 

                texto_timer = fuente.render("Tiempo: "+ str(segundos),True, COLOR_BLANCO)
                pantalla.blit(imagen_fondo,imagen_fondo.get_rect())
                bala.mover()
                bala.blitear_bala(pantalla)
                personaje.mostrar_personaje(pantalla)
                pantalla.blit(texto_puntos,(50,50))#blitear los puntos 
                pantalla.blit(texto_timer,(600,50))

                if enemigo_1.flag == True:
                    enemigo_1.mover_derecha(5)# velocidad
                    enemigo_1.mostrar_enemigo(pantalla)

                if enemigo_2.flag == True:
                        enemigo_2.mover_derecha(5)
                        enemigo_2.mostrar_enemigo(pantalla)

                for i in range (14):
                        path =  str(i) + ".png"
                        imagen_explosion = pygame.image.load(path)
                        imagen_explosion = pygame.transform.scale(imagen_explosion, (110, 110))
                        rect_explosion = imagen_explosion.get_rect()
                        rect_explosion.x = 200 #left en pixeles
                        rect_explosion.y = 400 #top en pixeles

                        dic_explosion = {"imagen": imagen_explosion, "rect": rect_explosion}
                        lista_explosion.append(dic_explosion)

                if bala.rect.colliderect(enemigo_1.rect) and enemigo_1.flag: #verifica si hay colicion 
                        enemigo_1.flag = False
                        mostrar_explosion(lista_explosion, enemigo_1.rect)

                        estado_juego.puntaje += 10
                        texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_BLANCO)

                if bala.rect.colliderect(enemigo_2.rect) and enemigo_2.flag: #verifica si hay colicion con enemigo 2
                        enemigo_2.flag = False
                        mostrar_explosion(lista_explosion, enemigo_2.rect)
                        estado_juego.puntaje += 10
                        texto_puntos = fuente.render("Score: "+ str(estado_juego.puntaje),True, COLOR_BLANCO)

                if segundos == 0:
                    fin_nivel(jugar_nivel_dos,estado_juego)

                if enemigo_1.flag == False and enemigo_2.flag == False: 
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

            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(evento.pos)
                print(posicion_click)

                if  470  > posicion_click[0] > 347 and posicion_click[0] and 611 < posicion_click[1] < 645:
                    flag_ejecutar_ranking = False
                    menu()

        pantalla.blit(imagen,imagen.get_rect())
        fuente = pygame.font.SysFont("Gabriola", 60)
        fuente_titulo = pygame.font.SysFont("Gabriola", 80)
        texto_ranking = fuente_titulo.render("Ranking", True, COLOR_NEGRO)
        texto_volver = fuente.render("Volver", True, COLOR_NEGRO)
        pantalla.blit(texto_ranking,(350,100))
        pantalla.blit(texto_volver,(350, 600))
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
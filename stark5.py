from data_stark import lista_personajes
import os
import json
import csv


'''Recibe por parámetro un string que representa el nombre del archivo a leer. La funcion abre el archivo en modo 
lectura y devuelve la informacion que contiene ese archivo '''
def leer_archivo(nombre_archivo:str):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            retorno = archivo.read()
    except FileNotFoundError:
        retorno = False
        print("No existe el archivo")
    return retorno

'''Recibe por parámetro un string que reprenta el nombre con el que se va a guardar el archivo y un string con el 
contenido del archivo. La función crea el archivo en caso de que no exista y lo reescribe si existe.Si el archivo
se creo, retorna True, si no se creo retorna False, y en ambos casos se muestra por consola un mensaje indicando
la situacion.'''
def guardar_archivo(nombre_guardar:str, contenido_guardar:str):
        try:
            with open(nombre_guardar,"w+",encoding="utf-8") as archivo: 
                archivo.write(contenido_guardar)
            retorno = True
            print("Se creó el archivo:{0}".format(nombre_guardar))
        except FileNotFoundError:
            retorno = False
            print("Error al crear el archivo:{0}".format(nombre_guardar))
        return retorno

'''Reutilice la funcion de starks anteriores para sanitizar los datos'''
def stark_normalizar_datos(lista_personajes:list): 
    resultado = False
    if lista_personajes == []:
        print("Error. Lista vacía")
        return False
    else:
        for personaje in lista_personajes:
            if type(personaje["altura"]) == float or type(personaje["peso"]) == float or type(personaje["fuerza"]) == int:
                resultado = False
            else:
                personaje["altura"] = float(personaje["altura"])
                personaje["peso"] = float(personaje["peso"])
                personaje["fuerza"] = int(personaje["fuerza"])
                resultado = True
        if resultado == True:
            print("Datos normalizados")
    return resultado

'''Recibe la ruta del archivo y la lista de personajes. La función guardar la información y crea un archivo en 
formato csv. Si la lista está vacia retorna False y si se creo el archivo retorna True.'''
'''
    
        lista_claves = list(lista_personajes[0].keys())
        
        guardar_archivo(ruta_archivo,cabecera)
        with open(ruta_archivo, "a", encoding="utf-8") as archivo:
            for heroe in lista_personajes:
                lista_datos = list(heroe.values())
                datos = ",".join(lista_datos)
                archivo.write("{0}\n".format(datos))
        retorno = True
    else:
        retorno = False
    return retorno'''
def generar_csv(ruta_archivo:str, lista_personajes: list):
    if lista_personajes != []:
        lista_claves = list(map(str, lista_personajes[0].keys()))
        cabecera = ",".join(lista_claves)
        
        # Usar el modo 'w' en lugar de 'a' para escribir la cabecera
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("{0}\n".format(cabecera))
        
        # Continuar con el modo 'a' para agregar los datos
        with open(ruta_archivo, "a", encoding="utf-8") as archivo:
            for heroe in lista_personajes:
                lista_datos = list(map(str, heroe.values()))
                datos = ",".join(lista_datos)
                archivo.write("{0}\n".format(datos))
        retorno = True
    else:
        retorno = False
    return retorno

'''Recibe la ruta del cvs a leer. La función genera una lista de superhéroes con los datos del archivo que se le 
paso. Retorna la lista de superheroes y si el archivo no existe retorna False.'''

def leer_cvs(ruta_archivo:str):
    lista_heroes = []
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo,'r') as archivo:
            claves = archivo.readline().strip().split(',')
            for linea in archivo:
                heroe = {}
                valores = linea.strip().split(',')
                for i in range (len(claves)): 
                    heroe[claves[i]] = valores[i]
                lista_heroes.append(heroe)
        retorno = lista_heroes
    else: 
        retorno = False
    return retorno

'''Recibe la Ruta del archivo , la lista de los superhéroes y el nombre de la lista.
Si la lista no está vacía debería guardar en un diccionario de una sóla
clave la lista de superhéroes,el nombre de clave debería ser la del
tercer parámetro que sería el nombre de la lista.'''
def generar_json(ruta_archivo:str,lista_personajes: list, nombre_lista:str):
    if lista_personajes != []:
        stark_normalizar_datos(lista_personajes)
        diccionario = {}
        diccionario[nombre_lista] =[]
        for i in range(len(lista_personajes)):
            diccionario[nombre_lista].append(lista_personajes[i])
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                    json.dump(diccionario, archivo, indent=4)

'''Recibe la ruta del archivo y el nombre de la lista a leer.
Si el archivo existe leer el json y retornar la lista, si no existe retorna false.'''
def leer_json(ruta_archivo:str, nombre_lista:str):
    retorno = False 
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            diccionario = json.load(archivo) #carga el contenido del archivo JSON y lo convierte en un diccionario de Python.
            if nombre_lista in diccionario:#verificar si existe la clave en ese diccionario 
                lista = diccionario[nombre_lista]
                retorno = lista
    except FileNotFoundError:
        retorno = False
    return retorno

'''Recibe la lista de personajes y la clave por la que se los va a ordenar. Ordena la lista de héroes por 
la clave pasada por paramentro de manera ascendente. Devuelve la lista ordenada '''
def ordenar_clave_asc(lista_personajes:list, clave:str):
    stark_normalizar_datos(lista_personajes)
    if clave != "altura" and clave != "fuerza" and clave != "peso":
        retorno = False
    else: 
        for i in range(len(lista_personajes) - 1):
            for j in range(i + 1, len(lista_personajes)):
                if lista_personajes[i][clave] > lista_personajes[j][clave]:
                    aux = lista_personajes[i]
                    lista_personajes[i] = lista_personajes[j]
                    lista_personajes[j] = aux
        retorno = lista_personajes
    return retorno

'''Recibe la lista de personajes y la clave por la que se los va a ordenar. Ordena la lista de héroes por 
la clave pasada por paramentro de manera descendente. Devuelve la lista ordenada '''
def ordenar_clave_des(lista_personajes:list, clave:str):
    stark_normalizar_datos(lista_personajes)
    if clave != "altura" and clave != "fuerza" and clave != "peso":
        retorno = False
    else: 
        for i in range(len(lista_personajes) - 1):
            for j in range(i + 1, len(lista_personajes)):
                if lista_personajes[i][clave] < lista_personajes[j][clave]:
                    aux = lista_personajes[i]
                    lista_personajes[i] = lista_personajes[j]
                    lista_personajes[j] = aux
        retorno = lista_personajes
    return retorno

'''Recibe la lista de personajes y la clave por la que se los va a ordenar. Ordena la lista de héroes por 
la clave pasada por paramentro de manera descendente. Devuelve la lista ordenada '''
'''Recibe la lista de personajes y la clave por la que se los va a ordenar.La funcion pregunta si se quiere ordenar
de forma ascendente o descendente'''
def ordenar_clave_segun_parameto(lista_personajes:list, clave:str):
    flag = True
    while (flag):
        opcion = input("\n¿Quiere ordenar la lista de manera ascendente ('asc') o descendente ('desc'): ")
        if opcion == "asc":
            print(ordenar_clave_asc(lista_personajes,clave))
        elif opcion == "desc":
            print(ordenar_clave_des(lista_personajes, clave))
        else:
            print("Ingrese una opcion valida")
            opcion = input("\n¿Quiere ordenar la lista de manera ascendente ('asc') o descendente ('desc'): ")

#menu
flag_menu = True
flag_json = True
flag_opcion_normalizar = True
while flag_menu:
    print('''● 1-Normalizar datos
● 2-Generar CSV (Guardar la lista generada en otra variable)
● 3-Listar heroes del archivo CSV ordenados por altura ASC (Validar si el
mismo existe)
● 4-Generar JSON (Guardar la lista generada en otra variable)
● 5-Listar heroes del archivo JSON ordenados por peso DESC (Validar si
el mismo existe)
● 6-Ordenar Lista por fuerza (Se le tiene que preguntar al usuario si
ordenar de manera ASC o DESC
● 7-Salir''')
    
    opcion = input("Ingrese una opcion: ")
    '''while flag_opcion_normalizar == True:
            if opcion != '1':
                print("Hace falta normalizar los datos")
                opcion = print(''''''● 1-Normalizar datos 
● 2-Generar CSV 
● 3-Listar heroes del archivo CSV ordenados por altura ASC (Validar si el mismo existe)
● 4-Generar JSON (Guardar la lista generada en otra variable)
● 5-Listar heroes del archivo JSON ordenados por peso DESC (Validar si el mismo existe)
● 6-Ordenar Lista por fuerza
● 7-Salir''''''

                opcion = input("Ingrese una opcion: ")
            else:
                flag_opcion_normalizar = False'''

    if opcion == '1':
        print(stark_normalizar_datos(lista_personajes))
    elif opcion == '2':
        csv_generado = generar_csv('Opcion_2.cvs',lista_personajes)
        print('Archivo cvs generado')
    elif opcion == '3':
        try:
            lista_csv = leer_cvs('Opcion_2.cvs')
            if lista_csv:
                # Imprimir lista sin ordenar
                print("Lista sin ordenar:")
                print(lista_csv)

                # Ordenar y luego imprimir
                lista_ordenada = ordenar_clave_asc(lista_csv, 'altura')
                print("Lista ordenada por altura ASC:")
                print(lista_ordenada)
            else:
                print('El archivo CSV no existe.')
        except FileNotFoundError:
            print('El archivo CSV no existe.')

    elif opcion == '4':
        json_generado = generar_json('Opcion_4.json',lista_personajes,"lista_personajes ")
        print('Archivo json generado')
    elif opcion == '5':
        try:
            lista_json = leer_json('Opcion_4.json', 'lista_personajes')
            if lista_json != False: 
                lista_ordenada = ordenar_clave_des(lista_json, 'peso')
                print(lista_ordenada)
        except FileNotFoundError:
            print('El archivo JSON no existe.')

    elif opcion == '6':
        print(ordenar_clave_segun_parameto(lista_personajes,'fuerza'))
    elif opcion == '7':
        break
    else:
        print("Opcion no valida")
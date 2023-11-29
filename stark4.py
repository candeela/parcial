from data_stark import *
import re

'''Recibe un string que es el nombre del personaje, extrae las iniciales del nombre y devuelve las inciales'''
def extraer_iniciales(nombre_heroe:str):
    if nombre_heroe == "":
        respuesta = "N/A"
    else:
        if re.search("the", nombre_heroe) != None:
            cambio_nombre = re.sub("the", "",nombre_heroe)
            respuesta = cambio_nombre
        elif re.search("-", nombre_heroe) != None:
            cambio_nombre = re.sub("-", " ",nombre_heroe)
            respuesta = cambio_nombre
        else:
            cambio_nombre = nombre_heroe
        iniciales = re.sub("[a-z]+", "", cambio_nombre)
        espacios = re.sub(r"\s+", " ", iniciales)
        puntos = re.sub(" ","." ,espacios)
        respuesta = (puntos + ".")

    return respuesta

'''Recibe por parametro un string, la funcion lo convierte a minuscula y con formato snake_case
si el dato no es un str retorna false, si es lo devuelve en minuscula y snake_case '''

def obtener_dato_formato(dato:str):
    if type(dato) != str:
        respuesta = False
    else:
        minusculas = dato.lower()
        respuesta = re.sub(" ","_",minusculas)

    return respuesta

'''Recibe por parametro un diccionario de un personaje, verifica si es un diccionario y si tiene la clave nombre, en caso
de que eso ocurra te devuelve el nombre de una forma determinada, si no es diccionario o no tiene clave nombre devuelve
false'''
def imprimir_nombre_con_iniciales(nombre_personaje:dict): 
    if type(nombre_personaje) == dict:
        if "nombre" in nombre_personaje:
            nombre = nombre_personaje["nombre"]
            minuscula = obtener_dato_formato(nombre)
            iniciales = extraer_iniciales(nombre)
            respuesta =("* {0} ({1})".format(minuscula,iniciales)) 
    else:
        respuesta = False
    return respuesta

'''Recibe por parametro la lista de personajes, si no es una lista o si esta vacia retorna False, si la lista tiene
personajes devuelve los nombres de una manera especifica usando la funcion anterior'''

def stark_imprimir_nombres_con_iniciales(lista_heroes):
    if type(lista_heroes) == list:
        if lista_heroes != None: 
            for heroe in lista_heroes: 
                print( imprimir_nombre_con_iniciales(heroe))
    else:
        return False

'''Recibe por parametro un diccionario de un perssonaje y un id, segun el genero del personaje se le asigna un
determinado codigo y devuelve el género, a continuacion el código determinado seguido de ceros y finaliza con el
id correspondiente. Si el diccionario esta vacio o no tiene alguno de los generos especificados devuelve N/A '''

def generar_codigo_heroe(dic_heroe: dict, id:int): 
    if dic_heroe["genero"] == ' ' or dic_heroe["genero"] != 'M' and dic_heroe["genero"] != 'F' and dic_heroe["genero"] != 'NB': 
        respuesta = 'N/A'
    else:
        id= str(id)
        if dic_heroe["genero"] == 'M': 
            codigo = 1
            ceros = id.zfill(7)
        elif dic_heroe["genero"] == 'F': 
            codigo = 2
            ceros = id.zfill(7)
        elif dic_heroe["genero"] == 'NB': 
            codigo = 0
            ceros = id.zfill(6)
        respuesta = ("{0}-{1}{2}") .format(dic_heroe["genero"],codigo,ceros)
    return respuesta

'''Recibe como parametro una lista de personajes, si la lista esta vacia o un elemento de la lista no es de tipo
diccionario retorna false, sino recorre la lista y  genera el codigo de cada personaje utilizando las funciones
anteriores, devuelve un string con el nombre y el codigo del persoanje en un formato especifico'''
def stark_generar_codigos_heroes(lista_personaje:list): 
    id_heroe = 0
    if lista_personaje == []:
        respuesta = False
    else:
        for personaje in lista_personaje:
            if type(personaje) != dict:
                respuesta = False
            else:
                id_heroe += 1
                codigo_heroe = generar_codigo_heroe(personaje, id_heroe)
                nombre_heroe = imprimir_nombre_con_iniciales(personaje)
                print ("{0} | {1}".format(nombre_heroe,codigo_heroe))
                respuesta = "Codigos generados"
    return respuesta

'''Recibe por parámetro un string que representa un posible número.
La función analiza el string, le saca los espacios en blanco del principio y el final en caso de que tenga y 
si es un numero entero positivo lo devuelve casteado a str, si tiene carácteres no numéricos retornar -1,
si es un número negativo retorna -2 y si presenta otro carácter devuelve -3'''
def sanitizar_entero (numero_str: str):
    numero_str = numero_str.strip() #por los espacios en blanco
    if re.search('[A-Za-z]+',numero_str):
        respuesta = -1
    elif re.search('[0-9]+',numero_str):
        if re.search('^-',numero_str):
            respuesta = - 2
        else:
            respuesta = int(numero_str)
    else: 
        respuesta = -3
    return respuesta

''' Recibe por parámetro un string que representa un posible número decimal.
La función analiza el string, le saca los espacios en blanco del principio y el final en caso de que tenga y 
si es un numero flotante positivo lo devuelve casteado a float, si tiene carácteres no numéricos retornar -1,
si es un número negativo retorna -2 y si presenta otro carácter devuelve -3'''
def sanitizar_flotante(numero_str:str):
    numero_str = numero_str.strip() #por los espacios en blanco
    if re.search('[A-Za-z]+',numero_str):
        respuesta = -1
    elif re.search('\.',numero_str):
        if re.search('^-',numero_str):
            respuesta = - 2
        else:
            respuesta = float(numero_str)
    else: 
        respuesta = -3
    return respuesta

'''Recibe por parámetro un string que representa el texto a validar y un string opcional que representa un valor por
defecto. La función analiza el string le saca los espacios en blanco del principio y del final en caso de que tenga
si el string es solo de texto lo retorna en minuscula, si tiene numeros retorna “N/A”, si tiene una barra la
reemplaza por un espacio en blanco y en caso de que el string este vacio devuelve el valor por defecto en minuscula'''

def sanitizar_str(valor:str,valor_defecto:str):
    valor = valor.strip() #por los espacios en blanco
    valor_defecto = valor_defecto.strip()
    if re.search('[0-9]+',valor):
        respuesta = 'N/A'
    elif re.search('\/',valor):
        respuesta = re.sub("\/"," ",valor)
    elif valor == " ": 
        if type(valor_defecto) == str:
                respuesta= valor_defecto.lower()
    else:
        respuesta = valor.lower()
    return respuesta

'''Recibe por parámetros un diccionario de personaje, un string es el dato a sanitizar y el un string que es el 
tipo del dato. La función verifica que el tipo de dato este dentro de lo establecido y que exista la clave en el 
diccionario, si no devuelve un mensaje de error y retorna False. Si los datos estan correctos lo sanitiza y
retorna True '''
def sanitizar_dato(personaje:dict,clave:str,tipo_dato):
    tipo_dato = tipo_dato.lower()#para poder hacer la validacion
    dato_sanitizado = False
    if clave in personaje:
        if tipo_dato == "string":
            personaje[clave] = sanitizar_str(personaje[clave]," ") 
            dato_sanitizado = True
        elif tipo_dato == "entero":
            personaje[clave] = sanitizar_entero(personaje[clave])
            dato_sanitizado = True
        elif tipo_dato == "flotante":
            personaje[clave] = sanitizar_flotante(personaje[clave],)
            dato_sanitizado = True
        else:
            print("Tipo de dato no reconocido")
    else:
        print("La clave especificada no existe en el héroe")
    return dato_sanitizado

'''Recibe por parametro una lista de personajes.La función recorre la lista y sanitiza los valores especificados,
si todos los datos se normalizaron devuelve 'Datos normalizados', si no se normalizaron todos devuelve
"No se pudieron normalizar todos los datos" y si la lista esta vacía devuelve 'Error: Lista de héroes vacía'''
def stark_normalizar_datos(lista_personajes:list):
    if lista_personajes == []:
        print("Error: Lista de héroes vacía")
    else:
        for heroe in lista_personajes:
            altura = sanitizar_dato(heroe,'altura','flotante')
            peso = sanitizar_dato(heroe,'peso','flotante')
            color_ojos = sanitizar_dato(heroe,'color_ojos','string')
            color_pelo = sanitizar_dato(heroe,'color_pelo','string')
            fuerza = sanitizar_dato(heroe,'fuerza','entero')
            inteligencia = sanitizar_dato(heroe,'inteligencia','entero')
        if altura == True and peso == True and color_ojos == True and color_pelo == True and fuerza == True and inteligencia == True:
            print('Datos normalizados')
        else:
            print("No se pudieron normalizar todos los datos")

'''Recibe por parámetro una lista de personajes, la funcion ignora la palabra "the" en caso de que la tenga y
devuelve cada palabra de los nombres de los perosnajes unida por un "-" '''
def stark_imprimir_indice_nombre(lista_personajes):
    lista_nombres = []
    for personaje in lista_personajes:
        nombre = personaje["nombre"]
        nombre = re.sub("the","",nombre)
        nombre = re.sub(r"\s+","-",nombre)
        lista_nombres.append(nombre)
    unificador = "-"
    respuesta = unificador.join(lista_nombres)
    return respuesta

'''Recibe por parámetro un patron que es con le que se va a generar el separador, un numero que representa la
cantidad de veces que se va a repetir ese patron y un booleano que indica si se imprime o no la respuesta.
La funcion repite el patron tantas veces como el largo dado y devuelve esa cadena de texto, en caso de que no se
cumplan las indicaciones pedidad devuelve' N/A' '''
def generar_separador(patron:str, largo:int , imprimir = True):
    if len(patron) >= 1 and  len(patron) <= 2:
        if type(largo)== int and largo >=  1 or largo <= 235:
            respuesta = patron * largo
    else:
        respuesta = 'N/A'
    if imprimir:
        print(respuesta)
    return respuesta

'''Recibe por parámetro un titulo, la funcion genera un separador y devuelve el titulo en mayuscula entre medio de
los separadores'''
def generar_encabezado(titulo:str):
    palabra_encabezado = titulo.upper()
    separador_encabezado = generar_separador('*',151,False)
    encabezado = "{0}{1}\n{2}".format(separador_encabezado,palabra_encabezado,separador_encabezado)
    return encabezado

'''Recibe como parámetro un diccionario de un personaje, la funcion recorre los datos y los devuelve en un formato
especifico con un encabezado'''

def  imprimir_ficha_heroe(personaje:dict):
    encabezado_principal = generar_encabezado("principal")
    nombre = obtener_dato_formato(personaje["nombre"])
    iniciales = extraer_iniciales(personaje["nombre"])
    identidad = obtener_dato_formato(personaje["identidad"])
    consultora = obtener_dato_formato(personaje["empresa"]) 
    codigo = generar_codigo_heroe(personaje,2)
    encabezado_fisico = generar_encabezado("fisico")
    altura = (personaje["altura"] )
    peso = (personaje["peso"] )
    fuerza = (personaje["fuerza"] )
    encabezado_señas = generar_encabezado("señas particulares")
    ojos = (personaje["color_ojos"]) 
    pelo = (personaje["color_pelo"]) 
    respuesta = ('''{0}NOMBRE DEL HEROE: {1} ({2})\nIDENTIDAD SECRETA: {3}\nCONSULTORA: {4}\nCÓDIGO DE HÉROE: {5}
{6}ALTURA: {7}\nFUERZA: {8} \nPESO: {9}\n{10}\nCOLOR DE PELO: {11}\nCOLOR DE OJOS: {12} '''.format(encabezado_principal,nombre,iniciales,identidad,consultora,codigo,encabezado_fisico,altura,peso,fuerza,encabezado_señas,ojos,pelo))
    return respuesta

'''Recibe por parámetros una lista de personajes. La funcion imprime la primer ficha y pide que ingreses una opcion,
si es 1 muestra la ficha de la izquierda, si es 2 muestra la de la derecha, si es 3 sale del programa y si no es
ninguna de esas opciones vuelve a pedir un ingreso valido. Devuelve la ficha del personaje segun corresponda
'''
def stark_navegar_fichas(lista_personajes:list):
    indice = 0
    flag_navegar = True
    print(imprimir_ficha_heroe(lista_personajes[indice ]))
    while flag_navegar:
        opcion = input("Ingrese alguna de las siguientes opciones ([ 1 ] Ir a la izquierda, [ 2 ] Ir a la derecha, [ 3 ] Salir): ")
        if opcion == "1":
            if indice == 0:
                indice = len(lista_personajes) - 1
            else:
                indice -= 1
                if indice not in range (len(lista_personajes)):
                    indice = len(lista_personajes) 
        elif opcion == "2":
            indice += 1
            if indice not in range (len(lista_personajes)):
                indice = len(lista_personajes) - len(lista_personajes)
        elif opcion == "3":
            break
        else:
            opcion = input("Ingrese una opcion valida: ")
        print(imprimir_ficha_heroe(lista_personajes[indice ]))

#menu
flag_menu = True
while flag_menu:
    print('''1- Imprimir la lista de nombres junto con sus iniciales
2 - Imprimir la lista de nombres y el código del mismo
3 - Normalizar datos
4 - Imprimir índice de nombres
5 - Navegar fichas
6- Salir''')
    opcion = input("Ingrese una opcion: ")

    if opcion == '1':
        print(stark_imprimir_nombres_con_iniciales(lista_personajes))
    elif opcion == '2':
        print(stark_generar_codigos_heroes(lista_personajes))
    elif opcion == '3':
        print(stark_normalizar_datos(lista_personajes))
    elif opcion == '4':
        print(stark_imprimir_indice_nombre(lista_personajes))
    elif opcion == '5':
        stark_navegar_fichas(lista_personajes)
    elif opcion == '6':
        break
    else:
        print("Opcion no valida")
from data_stark import lista_personajes
import os
import json

#Función Normalizar Datos
def stark_normalizar_datos (superhero_list: list):
    retorno = None
    for superheroe in superhero_list:
        if (superheroe == {}):
            print("Hubo un error al normalizar los datos. Verifique que no haya algún dato faltante en la lista")
            retorno = False
    if (superhero_list == []):
        print("Hubo un error al normalizar los datos. Verifique que la lista no esté vacía")
        retorno = False
    else:
        for superheroe in superhero_list:
            if ((type(superheroe["fuerza"]) == int) or (type(superheroe["peso"]) == float) or (type(superheroe["altura"]) == float)):
                print("Hubo un error al normalizar los datos. Verifique que los datos ya no se hayan normalizado anteriormente")
                retorno = False
            else:
                superheroe["fuerza"] = int(superheroe["fuerza"])
                superheroe["peso"] = float(superheroe["peso"])
                superheroe["altura"] = float(superheroe["altura"])
        print("Datos Normalizados")
        retorno = True
    return retorno

#Función Formatear de Lista
def formatear_lista(list = list):
    for element in list:
        print(f"\nNombre: {element['nombre']}"
            f"\nIdentidad: {element['identidad']}"
            f"\nEmpresa: {element['empresa']}"
            f"\nAltura: {element['altura']}"
            f"\nPeso: {element['peso']}"
            f"\nGénero: {element['genero']}"
            f"\nColor de Ojos: {element['color_ojos']}"
            f"\nColor de Pelo: {element['color_pelo']}"
            f"\nFuerza: {element['fuerza']}"
            f"\nInteligencia: {element['inteligencia']}")

#Función Leer Archivo
def leer_archivo(file_extension = str):
    retorno = None
    if os.path.exists(file_extension):
        with open(file_extension, "r", encoding="utf-8") as file:
            retorno = file.read()
    else:
        print("Archivo Inexistente.")
        retorno = False
    return retorno

#Función Guardar Archivo
def guardar_archivo(file_extension = str, content = str):
    retorno = None
    with open(file_extension, "w+", encoding="utf-8") as file:
        retorno = file.write(f"{content}\n")
        if (retorno != ""):
            print(f"Se creó el archivo: {file.name}")
            retorno = True
        else:
            print(f"Error al crear el archivo: {file.name}.")
            retorno = False
    return retorno

#Función Generar CSV
def generar_csv(superhero_file = str, superhero_list = list):
    retorno = None
    if (superhero_list != []):
        for superheroe in superhero_list:
            superheroe["fuerza"] = str(superheroe["fuerza"])
            superheroe["peso"] = str(superheroe["peso"])
            superheroe["altura"] = str(superheroe["altura"])
        keys_list = list(superhero_list[0].keys())
        header = ",".join(keys_list)
        guardar_archivo(superhero_file, header)
        with open(superhero_file, "a", encoding="utf-8") as file:
            for element in superhero_list:
                values_list = list(element.values())
                main = ",".join(values_list)
                file.write(f"{main}\n")
    else:
        retorno = False
    return retorno

#Función Leer CSV
def leer_csv(file_extension = str):
    retorno = None
    superhero_list = []
    if os.path.exists(file_extension):
        with open(file_extension, "r", encoding="utf-8") as file:
            keys = file.readline()
            keys_list = keys.replace("\n", "").split(",")
            for line in file:
                element = {}
                element_list = line.replace("\n", "").split(",")
                for i in range(len(keys_list)):
                    key = keys_list[i]
                    element[key] = element_list[i]
                superhero_list.append(element)
        retorno = formatear_lista(superhero_list)
    else:
        retorno = False
    return retorno

#Función Generar JSON
def generar_json(file_extension = str, superhero_list = list, list_name = str):
    retorno = None
    if (superhero_list != []):
        for superheroe in superhero_list:
            if ((type(superheroe["fuerza"]) != int) or (type(superheroe["peso"]) != float) or (type(superheroe["altura"]) != float)):
                print("Datos no normalizados.")
                retorno = False
                break
            else:
                data = {}
                data[list_name] = []
                for i in range(len(superhero_list)):
                    data[list_name].append(superhero_list[i])
                with open(file_extension, "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=4)
    else:
        retorno = False
    return retorno

#Función Leer JSON
def leer_json(file_extension = str, list_name = str):
    retorno = None
    if (os.path.exists(file_extension)):
        with open(file_extension, "r", encoding="utf-8") as file:
            superhero_list = json.load(file)
            retorno = formatear_lista(superhero_list[list_name])
    else:
        retorno = False
    return retorno


#Función Ordenar Héroes por Clave Numérica Ascendente
def ordenar_heroes_asc(superhero_list = list, key = str):
    retorno = None
    flag = True
    if (key != "fuerza" and key != "altura" and key != "peso"):
        retorno = False
    else:
        for superheroe in superhero_list:
            if ((type(superheroe["fuerza"]) != int) or (type(superheroe["peso"]) != float) or (type(superheroe["altura"]) != float)):
                print("Datos no normalizados.")
                retorno = False 
                break
            else:
                while (flag):
                    flag = False
                    for i in range(len(superhero_list)-1):
                        if (superhero_list[i][key] > superhero_list[i+1][key]):
                            aux = superhero_list[i]
                            superhero_list[i] = superhero_list[i+1]
                            superhero_list[i+1] = aux
                            flag = True
                retorno = formatear_lista(superhero_list)
    return retorno

#Función Ordenar Héroes por Clave Numérica Descendente
def ordenar_heroes_desc(superhero_list = list, key = str):
    retorno = None
    flag = True
    if (key != "fuerza" and key != "altura" and key != "peso"):
        retorno = False
    else:
        for superheroe in superhero_list:
            if ((type(superheroe["fuerza"]) != int) or (type(superheroe["peso"]) != float) or (type(superheroe["altura"]) != float)):
                print("Datos no normalizados.")
                retorno = False 
                break
            else:
                while (flag):
                    flag = False
                    for i in range(len(superhero_list)-1):
                        if (superhero_list[i][key] < superhero_list[i+1][key]):
                            aux = superhero_list[i]
                            superhero_list[i] = superhero_list[i+1]
                            superhero_list[i+1] = aux
                            flag = True
                retorno = formatear_lista(superhero_list)
    return retorno

#Función Ordenar Héroes por Clave Numérica Ascendente o Descendente
def ordenar_heroes_asc_desc(superhero_list = list, key = str):
    flag = True
    while (flag):
        question = input("\n¿Desea ordenar la lista de manera ascendente ('asc'), descendente ('desc'), o desea salir ('salir')?: ")
        if (question == "asc"):
            ordenar_heroes_asc(superhero_list, key)
        elif (question == "desc"):
            ordenar_heroes_desc(superhero_list, key)
        elif (question == "salir"):
            flag = False
        else:
            print("Opción inexistente, vuelva a intentarlo")


#Menú Principal
menu_flag = True
normalize = False
csv = ""
read_csv = False
read_json = False

while (menu_flag):
    print("\n1 -Normalizar Datos. \n"
        "2 -Generar CSV. \n"
        "3 -Listar Héroes del CSV Ordenados por Altura ASC. \n"
        "4 -Generar JSON. \n"
        "5 -Listar Héroes del JSON Ordenados por Peso DESC. \n"
        "6 -Ordenar Lista por Fuerza. \n"
        "7 -Salir. \n")
    question = input("Ingrese la opción deseada (1, 2, 3, 4, 5, 6, 7): ")
    if (question == "1"):
        normalize = stark_normalizar_datos(lista_personajes)
    if (normalize == True):
        if (question == "2"):
            csv_file = generar_csv("Clase 7/superhero.csv", lista_personajes)
        elif (question == "3"):
            read_csv = leer_csv("Clase 7/superhero.csv")
            if (read_csv != False):
                ordenar_heroes_asc(lista_personajes, "altura")
            else:
                print("Archivo inexistente.")
        elif (question == "4"):
            json_file = generar_json("Clase 7/superhero.json", lista_personajes, "heroes")
        elif (question == "5"):
            read_json = leer_json("Clase 7/superhero.json", "heroes")
            if (read_json != False):
                ordenar_heroes_asc(lista_personajes, "peso")
            else:
                print("Archivo inexistente.")
        elif (question == "6"):
            ordenar_heroes_asc_desc(lista_personajes, "fuerza")
        elif (question == "7"):
            menu_flag = False
            print("Saliendo...")
    else:
        print("Error al normalizar los datos u opción inexistente.")

import pygame
import json

class Estado_juego:
    def __init__(self):
        self.puntaje = 0
        self.nombre = ''
        self.progreso = {}

    def guardar_progreso(self):
        try:
            with open('data.json', 'r') as archivo:
                datos_jugadores = json.load(archivo)
        except FileNotFoundError:
            datos_jugadores = {}

        datos_jugadores[self.nombre] = {"Nombre": self.nombre, "puntaje": self.puntaje}
        
        with open('data.json', 'w') as archivo:
            json.dump(datos_jugadores, archivo,indent=4)

    def cargar_progreso(self):
        try:
            with open('data.json', 'r') as archivo:
                jugadores = json.load(archivo)
            self.progreso = jugadores
        except FileNotFoundError:
            self.progreso = {}

    def actualizar_progreso(self):
        if self.nombre in self.progreso:
            self.puntaje = self.progreso[self.nombre]["puntaje"]
        else:
            self.progreso[self.nombre] = {"puntaje": self.puntaje}



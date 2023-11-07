"""importo los archivos necesarios"""
from datetime import datetime
import random


class Paciente:
    """calse paciente"""

    def __init__(self, nombre, edad, sintomas: [str]):
        self.nombre = nombre
        self.edad = edad
        self.clasificacion = ""
        self.importancia = 0
        self.tiempo_ingreso: datetime = 0  # tiempo en el que ingreso
        self.tiempo_max = 0
        self.sintomas = sintomas
        self.prueba = 0

    def tiempo_esperando(self) -> datetime:
        """funciones de tiempo"""
        tiempo_actual = datetime.now()
        tiempo_pasado: datetime = tiempo_actual-self.tiempo_ingreso
        return tiempo_pasado

    def significado_del_tiempo(self) -> int:
        """funciones de tiempo"""
        if self.clasificacion == "naranja":
            self.prueba = self.tiempo_max-random.randint(0, 10)
        elif self.clasificacion == "amarillo":
            self.prueba = self.tiempo_max-random.randint(0, 60)
        elif self.clasificacion == "verde":
            self.prueba = self.tiempo_max-random.randint(0, 120)
        elif self.clasificacion == "azul":
            self.prueba = self.tiempo_max-random.randint(0, 240)
        elif self.clasificacion == "rojo":
            self.prueba = self.tiempo_max
        return self.prueba

    def set_tiempo_max(self):
        """funciones de tiempo"""
        tiempo_naranja = 10
        tiempo_amarillo = 60
        tiempo_verde = 120
        tiempo_azul = 240

        if self.clasificacion == "naranja":
            self.tiempo_max = tiempo_naranja
            self.importancia = 4
        elif self.clasificacion == "amarillo":
            self.tiempo_max = tiempo_amarillo
            self.importancia = 3
        elif self.clasificacion == "verde":
            self.tiempo_max = tiempo_verde
            self.importancia = 2
        elif self.clasificacion == "azul":
            self.tiempo_max = tiempo_azul
            self.importancia = 1
        elif self.clasificacion == "rojo":
            self.tiempo_max = 0
            self.importancia = 5

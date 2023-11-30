"""importo los archivos necesarios"""
from datetime import datetime
import random


class Paciente:
    """calse paciente"""

    def __init__(self, nombre, edad, sintomas: [str]):
        self.nombre = nombre
        self.edad = edad
        self.color = ""
        self.tiempo_ingreso: datetime = 0  # tiempo en el que ingreso
        self.tiempo_max = 0
        self.sintomas = sintomas

    def tiempo_esperando(self) -> datetime:
        """funciones de tiempo"""
        tiempo_esperando = datetime.now()-self.tiempo_ingreso

        min_transcurridos = tiempo_esperando.total_seconds()/60

        prueba = self.tiempo_max-min_transcurridos
        return prueba

    def significado_del_tiempo(self) -> int:
        """funciones de tiempo"""
        if self.color == "naranja":
            self.prueba = self.tiempo_max-random.randint(0, 10)
        elif self.color == "amarillo":
            self.prueba = self.tiempo_max-random.randint(0, 60)
        elif self.color == "verde":
            self.prueba = self.tiempo_max-random.randint(0, 120)
        elif self.color == "azul":
            self.prueba = self.tiempo_max-random.randint(0, 240)
        elif self.color == "rojo":
            self.prueba = self.tiempo_max
        return self.prueba

"""importo los archivos necesarios"""
from datetime import datetime


class Paciente:
    """calse paciente"""

    def __init__(self, nombre, edad, sintomas: [str]):
        self.nombre = nombre
        self.edad = edad
        self.clasificacion = ""
        self.tiempo_ingreso: datetime = 0  # tiempo en el que ingreso
        self.tiempo_max = 0
        self.sintomas = sintomas

    def tiempo_esperando(self) -> datetime:
        """funciones de tiempo"""
        tiempo_actual = datetime.now()
        tiempo_pasado: datetime = tiempo_actual-self.tiempo_ingreso
        return tiempo_pasado

    def significado_del_tiempo(self) -> int:
        """funciones de tiempo"""
        minpasados: int = self.tiempo_esperando().seconds*5
        return (self.tiempo_max-minpasados)

    def set_tiempo_max(self):
        """funciones de tiempo"""
        tiempo_naranja = 10
        tiempo_amarillo = 60
        tiempo_verde = 120
        tiempo_azul = 240

        if self.clasificacion == "naranja":
            self.tiempo_max = tiempo_naranja
        elif self.clasificacion == "amarillo":
            self.tiempo_max = tiempo_amarillo
        elif self.clasificacion == "verde":
            self.tiempo_max = tiempo_verde
        elif self.clasificacion == "azul":
            self.tiempo_max = tiempo_azul
        elif self.clasificacion == "rojo":
            self.tiempo_max = 0

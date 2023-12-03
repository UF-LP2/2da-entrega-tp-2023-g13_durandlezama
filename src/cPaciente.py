"""importo los archivos necesarios"""
from datetime import datetime


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
        time_actual = datetime.now()
        timepassed: datetime = time_actual - self.tiempo_ingreso
        return timepassed

    def timeremaining(self) -> int:
        """devuelve el tiempo que le queda al paciente"""
        minpassed: int = self.tiempo_esperando().seconds
        return (self.tiempo_max - minpassed)

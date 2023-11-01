"""importamos la clase paciente"""
import csv
from cMedico import Medico
from cPaciente import Paciente


class Guardia:
    """Módulo que proporciona la funcionalidad para la gestión de pacientes en la guardia médica."""

    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.lista_pacientes = [Paciente]
        self.medicos_activos = [Medico]

    def leer_archivo(self):

        with open("src/Pacientes.csv") as file:
            reader = csv.reader(file, delimiter=',')
            next(file, None)

            for row in reader:
                nombre = row[0]
                edad = row[1]
                sintomas_1 = row[2]
                sintomas_2 = row[3]
                sintomas_3 = row[4]
                sintomas_4 = row[3]

                sintomas = [sintomas_1, sintomas_2, sintomas_3, sintomas_4]
                aux = Paciente(nombre, edad, sintomas)
                self.lista_pacientes.append(aux)

    def armar_lista(self, paciente):
        """funcion que arma la lista"""
        if paciente.clasificacion == "rojo":
            return "El paciente es prioridad 1"

        self.lista_pacientes.append(paciente)

        if len(self.lista_pacientes) <= 1:
            return self.lista_pacientes
        else:
            mitad = len(self.lista_pacientes) // 2
            izquierda = self.lista_pacientes[:mitad]
            derecha = self.lista_pacientes[mitad:]

        izquierda_ordenada = self.armar_lista(izquierda)
        derecha_ordenada = self.armar_lista(derecha)

        lista_ordenada = self.mayor(izquierda_ordenada, derecha_ordenada)
        return lista_ordenada

    def mayor(self, izquierda, derecha):
        """funcion para verificar quien es mayor"""
        resultado = []

        tiempo_izq = self.evaluar_tiempo(izquierda[0])
        tiempo_derecha = self.evaluar_tiempo(derecha[0])

        if tiempo_izq <= tiempo_derecha:
            resultado.append(izquierda)
            resultado.append(derecha)
        else:
            resultado.append(derecha)
            resultado.append(izquierda)

        return resultado

    def evaluar_tiempo(self, paciente):
        """funcion para verificar el tiemp"""
        tiempo_naranja = 10
        tiempo_amarillo = 60
        tiempo_verde = 120
        tiempo_azul = 240

        if paciente.clasificacion == "naranja":
            return tiempo_naranja - paciente.tiempo_espera
        elif paciente.clasificacion == "amarillo":
            return tiempo_amarillo - paciente.tiempo_espera
        elif paciente.clasificacion == "verde":
            return tiempo_verde - paciente.tiempo_espera
        elif paciente.clasificacion == "azul":
            return tiempo_azul - paciente.tiempo_espera

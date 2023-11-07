"""importamos la clase paciente"""
import csv
from src.cMedico import Medico
from src.cPaciente import Paciente
from src.cEnfermero import Enfermero


class Guardia:
    """Módulo que proporciona la funcionalidad para la gestión de pacientes en la guardia médica."""

    def __init__(self, nombre, capacidad, list_medicos: Medico):
        self.nombre = nombre
        self.capacidad = capacidad
        self.lista_archivo: Paciente = []
        self.lista_pacientes: Paciente = []
        self.medicos_activos = 0
        self.lista_medicos = list_medicos

    def leer_archivo(self):
        """leemos el archivo"""
        with open("src/Pacientes.csv", "r") as file:
            reader = csv.reader(file, delimiter=',')
            next(file, None)

            for row in reader:
                nombre = row[0]
                edad = row[1]
                sintomas_1 = row[2]
                sintomas_2 = row[3]
                sintomas_3 = row[4]
                sintomas_4 = row[5]

                sintomas = [sintomas_1, sintomas_2, sintomas_3, sintomas_4]
                aux = Paciente(nombre, edad, sintomas)
                self.lista_archivo.append(aux)

    def set_med_activos(self, cant):
        """set de medicos activos"""
        self.medicos_activos = cant

    def armar_lista(self, pacientes):
        """Función para clasificar y ordenar la lista de pacientes"""
        if len(pacientes) < 2:
            return pacientes

        # Dividir la lista en dos mitades
        mitad = len(pacientes) // 2

        izquierda = self.armar_lista(pacientes[:mitad])
        derecha = self.armar_lista(pacientes[mitad:])

        # Llamadas recursivas para ordenar las mitades
        # izquierda_ordenada = self.armar_lista(izquierda)
        # self.armar_listaderecha_ordenada = self.armar_lista(derecha)

        # Combinar las mitades ordenadas usando el algoritmo de Merge Sort
        return self.merge(izquierda, derecha)

    def merge(self, izquierda: Paciente, derecha: Paciente):
        """Función para combinar dos listas ordenadas"""
        if len(izquierda) < 1:
            return izquierda
        elif len(derecha) < 1:
            return derecha

        resultado = []
        i = j = 0
        total_len = len(izquierda)+len(derecha)

        # Comparar elementos y combinar las listas ordenadas
        while len(resultado) < total_len:

            if izquierda[i].clasificacion == "rojo":
                resultado.append(izquierda[i])
                i += 1
            elif derecha[j].clasificacion == "rojo":
                resultado.append(derecha[j])
                j += 1
            elif izquierda[i].importancia > derecha[i].importancia:
                if derecha[i].significado_del_tiempo() < 5:
                    resultado.append(derecha[j])
                    j += 1
                else:
                    resultado.append(izquierda[i])
                    i += 1
            else:
                if izquierda[i].significado_del_tiempo() < 5:
                    resultado.append(izquierda[i])
                    i += 1
                else:
                    resultado.append(derecha[j])
                    j += 1

            if i == len(izquierda) or \
                    j == len(derecha):
                resultado.extend(izquierda[i:] or derecha[j:])
                break

        return resultado

    def llamar(self):
        """funcion para llamar a los pacientes"""
        while len(self.lista_pacientes) != 0:
            for i in self.lista_medicos:
                if i.estado:
                    i.atender(self.lista_pacientes[0])
                    self.lista_pacientes.pop()

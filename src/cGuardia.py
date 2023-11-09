"""importamos la clase paciente"""
import csv
from src.cMedico import Medico
from src.cPaciente import Paciente


class Guardia:
    """Módulo que proporciona la funcionalidad para la gestión de pacientes en la guardia médica."""

    def __init__(self, nombre, capacidad, list_medicos: [Medico]):
        self.nombre = nombre
        self.capacidad = capacidad
        self.lista_archivo: Paciente = []
        self.lista_pacientes: Paciente = []
        self.medicos_activos = 0
        self.lista_medicos = list_medicos

    def leer_archivo(self):
        """leemos el archivo"""
        with open(r"src/Pacientes.csv") as file:
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
        if len(pacientes) == 1:
            return pacientes

        # Dividir la lista en dos mitades
        mitad = len(pacientes) // 2

        izquierda = self.armar_lista(pacientes[:mitad])
        derecha = self.armar_lista(pacientes[mitad:])

        # Combinar las mitades ordenadas usando el algoritmo de Merge Sort
        return self.merge(izquierda, derecha)

    def merge(self, izquierda: Paciente, derecha: Paciente):
        """ funcion de merge """

        if len(izquierda) < 1:
            return izquierda
        elif len(derecha) < 1:
            return derecha

        resultado = []
        i = j = 0

        # Comparar elementos y combinar las listas ordenadas
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i].tiempo_esperando() < derecha[j].tiempo_esperando():
                resultado.append(izquierda[i])
                i += 1
            elif izquierda[i].tiempo_esperando() > derecha[j].tiempo_esperando():
                resultado.append(derecha[j])
                j += 1
            else:
                if izquierda[i].importancia > derecha[j].importancia:
                    resultado.append(izquierda[i])
                    i += 1
                else:
                    resultado.append(derecha[j])
                    j += 1

        # Agregar los elementos restantes, si los hay
        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])

        return resultado

    def llamar(self):
        """Función para llamar a los pacientes y asignar a los médicos"""
        while self.lista_pacientes:
            for medico in self.lista_medicos:
                if medico.estado and self.lista_pacientes:
                    paciente = self.lista_pacientes.pop(0)
                    resultado_atencion = medico.atender(paciente)
                    mensaje = f"El paciente {paciente.nombre} está {resultado_atencion}. Fue atendido por el médico {medico.nombre}"
                    self.listar(mensaje)

    def listar(self, mensaje: str):
        """Función para imprimir mensajes"""
        print(mensaje)

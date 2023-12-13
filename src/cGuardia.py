"""importamos la clase paciente"""
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

    def armar_lista(self, pacientes: Paciente):
        """acomodamos la lista en el orden en como van a ser atendidos"""
        i: Paciente
        for i in range(1, len(pacientes)):
            tempTiempo = pacientes[i].tiempo_restarnte()
            temp = pacientes[i]
            pos = self.busqueda_optimo(pacientes, tempTiempo, 0, i) + 1

            for k in range(i, pos, -1):
                pacientes[k] = pacientes[k-1]

            pacientes[pos] = temp

    def busqueda_optimo(self, arr: list[Paciente], val, inicioLista: int, finLista: int):
        """acomodamos la lista en el orden en como van a ser atendidos"""

        tEsperaIniLista = arr[inicioLista].tiempo_restarnte()

        if ((finLista-inicioLista) <= 1):
            if (val < tEsperaIniLista):
                return inicioLista - 1
            else:
                return inicioLista
        # Caso base
        # Si la lista tiene un solo elemento, me fijo si val es mayor o menor y ahi lo agrego

        # compara tiempos de espera y devuelve posicion en la que se debe insertar el paciente
        medio = (inicioLista + finLista)//2
        tEsperaMedio = arr[inicioLista].tiempo_restarnte()

        if tEsperaMedio < val:
            return self.busqueda_optimo(arr, val, medio, finLista)
        elif tEsperaMedio > val:
            return self.busqueda_optimo(arr, val, inicioLista, medio)
        else:
            return medio

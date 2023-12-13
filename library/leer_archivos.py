import csv
from src.cMedico import Medico
from src.cPaciente import Paciente
from src.cEnfermero import Enfermero


def leer_archivo():
    """leemos el archivo del paciente"""

    lista = []

    with open(r"library/Archivo_pacientes .csv") as file:
        reader = csv.reader(file, delimiter=',')

        for row in reader:
            nombre = row[0]
            edad = row[1]
            sintomas_1 = row[2]
            sintomas_2 = row[3]
            sintomas_3 = row[4]
            sintomas_4 = row[5]

            sintomas = [sintomas_1, sintomas_2, sintomas_3, sintomas_4]
            aux = Paciente(nombre, edad, sintomas)
            lista.append(aux)

    return lista


def archivo_m():
    """leemos el archivo del medico"""

    lista_medicos = []
    with open(r"library/Archivo_medicosf.csv") as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            nombre = row[0]
            estado = row[1]

            aux = Medico(nombre, estado)
            lista_medicos.append(aux)
    return lista_medicos


def archivo_e():
    """leemos el archivo del enfermero"""
    lista_enfermeros = []
    with open(r"library/Archivo_enfermeros.csv") as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            nombre = row[0]
            estado = row[1]

            aux = Enfermero(nombre, estado)
            lista_enfermeros.append(aux)
    return lista_enfermeros

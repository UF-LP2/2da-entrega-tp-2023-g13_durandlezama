"""importo archivos necesarios"""
import random
from src.cGuardia import Guardia
from src.cEnfermero import Enfermero
from src.cMedico import Medico


def lista_medicos():
    """Crear instancias de la clase Medico"""
    lista_med = []
    medico1 = Medico("Santiago Martínez")
    medico2 = Medico("Isabel García")
    medico3 = Medico("Andrés López")
    medico4 = Medico("Valentina Torres")
    medico5 = Medico("Mateo Rodríguez")
    medico6 = Medico("Camila Fernández")
    medico7 = Medico("Sebastián González")
    medico8 = Medico("Mariana Díaz")
    medico9 = Medico("Alejandro Pérez")
    medico10 = Medico("Luna Castro")
    medico11 = Medico("Daniel Riccardo")
    medico12 = Medico("Emma Herrera")
    medico13 = Medico("Lucas Vargas")
    medico14 = Medico("Renata Sánchez")
    medico15 = Medico("David Mendoza")
    medico16 = Medico("Elena Reyes")
    medico17 = Medico("Javier Morales")
    medico18 = Medico("Olivia Cruz")
    medico19 = Medico("Carlos Rivera")
    medico20 = Medico("Victoria Ortiz")

    # Crear una lista y agregar los objetos Medico usando append()
    lista_med.append(medico1)
    lista_med.append(medico2)
    lista_med.append(medico3)
    lista_med.append(medico4)
    lista_med.append(medico5)
    lista_med.append(medico6)
    lista_med.append(medico7)
    lista_med.append(medico8)
    lista_med.append(medico9)
    lista_med.append(medico10)
    lista_med.append(medico11)
    lista_med.append(medico12)
    lista_med.append(medico13)
    lista_med.append(medico14)
    lista_med.append(medico15)
    lista_med.append(medico16)
    lista_med.append(medico17)
    lista_med.append(medico18)
    lista_med.append(medico19)
    lista_med.append(medico20)
    return lista_med


def main() -> None:
    """desarrollo del main"""
    lista = []

    guardia_sm = Guardia("Triage", 1000, lista_medicos())
    guardia_sm.leer_archivo()
    enfermero = Enfermero("Maria", "5/12")

    while guardia_sm.lista_archivo:

        guardia_sm.medicos_activos = random.randint(7, 10)

        for c in range(guardia_sm.medicos_activos):
            enfermero.clasificar(guardia_sm.lista_archivo[c])
            lista.append(guardia_sm.lista_archivo[c])
            guardia_sm.lista_archivo.pop()

        guardia_sm.lista_pacientes = guardia_sm.armar_lista(lista)
        guardia_sm.llamar()


if __name__ == "__main__":
    main()

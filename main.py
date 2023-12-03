"""importo archivos necesarios"""
import random
from datetime import datetime
from library.leer_archivos import leer_archivo
from library.leer_archivos import archivo_m
from library.leer_archivos import archivo_e
from src.cPaciente import Paciente
from src.cEnfermero import Enfermero
from src.cMedico import Medico
from src.cGuardia import Guardia


def main() -> None:

    lista_doc: Medico = archivo_m()
    lista_enf: Enfermero = archivo_e()
    lista_pac: Paciente = leer_archivo()
    lista_atencion = []
    lista_espera = []
    triage = Guardia("Triage", 1000, lista_doc)

    ahora = datetime.now().hour
    print("Son las: " + str(ahora) + " hs")

    npac = random.randint(0, 80)

    while npac > 1:

        # turno de 2 enfermeros
        if (datetime.now().hour >= 6 and datetime.now().hour < 10):

            pac = lista_pac.pop(0)
            lista_enf[0].clasificar(pac)
            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)
                # se le asigna un lugar en la lista
                lista_espera = triage.armar_lista(lista_espera)

            pac = lista_atencion.pop(0)
            lista_enf[1].clasificar(pac)
            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)
                # se le asigna un lugar en la lista
                lista_espera = triage.armar_lista(lista_espera)

            npac = npac-1

            # turno de 5 enfermeros
        elif (datetime.now().hour >= 10 and datetime.now().hour < 16):

            pac = lista_pac.pop(0)
            lista_enf[0].clasificar(pac)
            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)
                # se le asigna un lugar en la lista
                lista_espera = triage.armar_lista(lista_espera)

            pac = lista_atencion.pop(0)
            lista_enf[1].clasificar(pac)
            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)
                # se le asigna un lugar en la lista
                lista_espera = triage.armar_lista(lista_espera)

            pac = lista_atencion.pop(0)
            lista_enf[2].clasificar(pac)
            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)
                # se le asigna un lugar en la lista
                lista_espera = triage.armar_lista(lista_espera)

            pac = lista_atencion.pop(0)
            lista_enf[3].clasificar(pac)
            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)
                # se le asigna un lugar en la lista
                lista_espera = triage.armar_lista(lista_espera)

            pac = lista_atencion.pop(0)
            lista_enf[4].clasificar(pac)
            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)
                # se le asigna un lugar en la lista
                lista_espera = triage.armar_lista(lista_espera)

            npac = npac-1

            # turno de 3 enfermeros
        elif (datetime.now().hour >= 16 and datetime.now().hour < 23):

            pac = lista_pac.pop(0)
            lista_enf[0].clasificar(pac)
            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)
                # se le asigna un lugar en la lista
                lista_espera = triage.armar_lista(lista_espera)

            pac = lista_atencion.pop(0)
            lista_enf[1].clasificar(pac)

            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)
                # se le asigna un lugar en la lista
                lista_espera = triage.armar_lista(lista_espera)

            pac = lista_atencion.pop(0)
            lista_enf[2].clasificar(pac)
            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)
                # se le asigna un lugar en la lista
                lista_espera = triage.armar_lista(lista_espera)

            npac = npac-1

            # turno de 1 enfermeros
        elif (datetime.now().hour >= 23 and datetime.now().hour < 6):

            pac = lista_pac.pop(0)
            lista_enf[0].clasificar(pac)
            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)
                # se le asigna un lugar en la lista
                lista_espera = triage.armar_lista(lista_espera)
            npac = npac-1

    i = 0
    while i < lista_espera:
        paciente_actual = lista_espera.pop(0)  # Obtiene el paciente actual
        print("Atendiendo a: " + str(paciente_actual.nombre))
        lista_doc[0].atender(paciente_actual)

    if len(lista_pac) > 0:
        for j in range(0, lista_pac):
            print(lista_pac[j].nombre)
            print(lista_pac[j].edad)
            print("\n")
    else:
        print("ya se atendieron todos los pacientes!")


if __name__ == "__main__":
    main()

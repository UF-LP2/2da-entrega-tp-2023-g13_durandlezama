"""importo archivos necesarios"""
from datetime import datetime
import time
from library.leer_archivos import leer_archivo
from library.leer_archivos import archivo_m
from library.leer_archivos import archivo_e
from src.cPaciente import Paciente
from src.cEnfermero import Enfermero
from src.cMedico import Medico


def main() -> None:

    lista_doc: Medico = archivo_m()
    lista_enf: Enfermero = archivo_e()
    lista_pac: Paciente = leer_archivo()
    lista_atencion = []
    lista_espera = []

    Horario = datetime.now().hour
    print("Son las: " + str(Horario) + " hs")

    while len(lista_pac) > 1:

        # turno de 2 enfermeros
        if (datetime.now().hour >= 6 and datetime.now().hour < 10):

            pac = lista_pac.pop(0)
            lista_enf[0].clasificar(pac)
            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)

            pac = lista_atencion.pop(0)
            lista_enf[1].clasificar(pac)
            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)

            # turno de 5 enfermeros
        elif (datetime.now().hour >= 10 and datetime.now().hour < 16):

            pac = lista_pac.pop(0)
            lista_enf[0].clasificar(pac)
            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)

            pac = lista_atencion.pop(0)
            lista_enf[1].clasificar(pac)
            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)

            pac = lista_atencion.pop(0)
            lista_enf[2].clasificar(pac)
            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)

            pac = lista_atencion.pop(0)
            lista_enf[3].clasificar(pac)
            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)

            pac = lista_atencion.pop(0)
            lista_enf[4].clasificar(pac)
            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)

            # turno de 3 enfermeros
        elif (datetime.now().hour >= 16 and datetime.now().hour < 23):

            pac = lista_pac.pop(0)
            lista_enf[0].clasificar(pac)
            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)

            pac = lista_atencion.pop(0)
            lista_enf[1].clasificar(pac)

            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)

            pac = lista_atencion.pop(0)
            lista_enf[2].clasificar(pac)
            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)

        # turno de 1 enfermeros
        elif (datetime.now().hour >= 23 and datetime.now().hour < 6):

            pac = lista_pac.pop(0)
            lista_enf[0].clasificar(pac)
            if pac.color == "Rojo":
                lista_atencion.append(pac)
            else:
                lista_espera.append(pac)

        time.sleep(1)


if __name__ == "__main__":
    main()

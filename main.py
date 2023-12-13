"""importo archivos necesarios"""
import random
from datetime import datetime
import time
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

    npac = random.randint(40, 80)

    while len(lista_pac) > 1:
        while npac > 1:

            # turno de 2 enfermeros
            if (ahora >= 6 and ahora < 10):

                pac = lista_pac.pop(0)
                lista_enf[0].clasificar(pac)

                if pac.color == "Rojo":
                    lista_atencion.append(pac)
                    print("Atendiendo al Paciente: " + str(pac.nombre) +
                          "se encuentra en estado critico")
                else:
                    lista_espera.append(pac)
                    # se le asigna un lugar en la lista
                    print("el Paciente: " + str(pac.nombre) +
                          "es de color: "+pac.color)
                    triage.armar_lista(lista_espera)

                pac = lista_pac.pop(0)
                lista_enf[1].clasificar(pac)
                if pac.color == "Rojo":
                    lista_atencion.append(pac)
                    print("Atendiendo al Paciente: " + str(pac.nombre) +
                          "se encuentra en estado critico")
                else:
                    lista_espera.append(pac)
                    # se le asigna un lugar en la lista
                    print("el Paciente: " + str(pac.nombre) +
                          "es de color: "+pac.color)
                    triage.armar_lista(lista_espera)

                npac = npac-1

            # turno de 5 enfermeros
            elif (ahora >= 10 and ahora < 16):

                pac = lista_pac.pop(0)
                lista_enf[0].clasificar(pac)
                if pac.color == "Rojo":
                    lista_atencion.append(pac)
                    print("Atendiendo al Paciente: " + str(pac.nombre) +
                          "se encuentra en estado critico")
                else:
                    lista_espera.append(pac)
                    # se le asigna un lugar en la lista
                    print("el Paciente: " + str(pac.nombre) +
                          "es de color: "+pac.color)
                    triage.armar_lista(lista_espera)

                pac = lista_pac.pop(0)
                lista_enf[1].clasificar(pac)
                if pac.color == "Rojo":
                    lista_atencion.append(pac)
                    print("Atendiendo al Paciente: " + str(pac.nombre) +
                          "se encuentra en estado critico")
                else:
                    lista_espera.append(pac)
                    # se le asigna un lugar en la lista
                    print("el Paciente: " + str(pac.nombre) +
                          "es de color: "+pac.color)
                    triage.armar_lista(lista_espera)

                pac = lista_pac.pop(0)
                lista_enf[2].clasificar(pac)
                if pac.color == "Rojo":
                    lista_atencion.append(pac)
                    print("Atendiendo al Paciente: " + str(pac.nombre) +
                          "se encuentra en estado critico")
                else:
                    lista_espera.append(pac)
                    # se le asigna un lugar en la lista
                    print("el Paciente: " + str(pac.nombre) +
                          "es de color: "+pac.color)
                    triage.armar_lista(lista_espera)

                pac = lista_pac.pop(0)
                lista_enf[3].clasificar(pac)
                if pac.color == "Rojo":
                    lista_atencion.append(pac)
                    print("Atendiendo al Paciente: " + str(pac.nombre) +
                          "se encuentra en estado critico")
                else:
                    lista_espera.append(pac)
                    # se le asigna un lugar en la lista
                    print("el Paciente: " + str(pac.nombre) +
                          "es de color: "+pac.color)
                    triage.armar_lista(lista_espera)

                pac = lista_pac.pop(0)
                lista_enf[4].clasificar(pac)
                if pac.color == "Rojo":
                    lista_atencion.append(pac)
                    print("Atendiendo al Paciente: " + str(pac.nombre) +
                          "se encuentra en estado critico")
                else:
                    lista_espera.append(pac)
                    # se le asigna un lugar en la lista

                    print("el Paciente: " + str(pac.nombre) +
                          "es de color: "+pac.color)
                    triage.armar_lista(lista_espera)

                npac = npac-1

                # turno de 3 enfermeros
            elif (ahora >= 16 and ahora < 23):

                pac = lista_pac.pop(0)
                lista_enf[0].clasificar(pac)
                if pac.color == "Rojo":
                    lista_atencion.append(pac)
                    print("Atendiendo al Paciente: " + str(pac.nombre) +
                          "se encuentra en estado critico")
                else:
                    lista_espera.append(pac)
                    # se le asigna un lugar en la lista
                    print("el Paciente: " + str(pac.nombre) +
                          "es de color: "+pac.color)
                    triage.armar_lista(lista_espera)

                pac = lista_pac.pop(0)
                lista_enf[1].clasificar(pac)

                if pac.color == "Rojo":
                    lista_atencion.append(pac)
                    print("Atendiendo al Paciente: " + str(pac.nombre) +
                          "se encuentra en estado critico")
                else:
                    lista_espera.append(pac)
                    # se le asigna un lugar en la lista
                    print("el Paciente: " + str(pac.nombre) +
                          "es de color: "+pac.color)
                    triage.armar_lista(lista_espera)

                pac = lista_pac.pop(0)
                lista_enf[2].clasificar(pac)
                if pac.color == "Rojo":
                    lista_atencion.append(pac)
                    print("Atendiendo al Paciente: " + str(pac.nombre) +
                          "se encuentra en estado critico")
                else:
                    lista_espera.append(pac)
                    # se le asigna un lugar en la lista
                    print("el Paciente: " + str(pac.nombre) +
                          "es de color: "+pac.color)
                    triage.armar_lista(lista_espera)

                npac = npac-1

                # turno de 1 enfermeros
            elif (ahora == 23 or (ahora > 00 and ahora < 6)):

                pac = lista_pac.pop(0)
                lista_enf[0].clasificar(pac)
                if pac.color == "Rojo":
                    lista_atencion.append(pac)
                    print("Atendiendo al Paciente: " + str(pac.nombre) +
                          "se encuentra en estado critico")
                else:
                    lista_espera.append(pac)
                    # se le asigna un lugar en la lista
                    print("el Paciente: " + str(pac.nombre) +
                          "es de color: "+pac.color)
                    triage.armar_lista(lista_espera)
                npac = npac-1

        i: int = 0
        while i < len(lista_espera):
            paciente_actual = lista_espera.pop(0)  # Obtiene el paciente actual
            print("Atendido a: " + str(paciente_actual.nombre) +
                  ", esta: "+lista_doc[0].atender(paciente_actual))
            lista_atencion.append(paciente_actual)
            time.sleep(0.1)


if __name__ == "__main__":
    main()

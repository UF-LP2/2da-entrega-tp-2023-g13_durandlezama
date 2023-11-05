"""importo archivos necesarios"""
import random
from src.cGuardia import Guardia
from src.cEnfermero import Enfermero
from src.cPaciente import Paciente


def main() -> None:
    """desarrollo del main"""

    guardia_sm = Guardia("Triage", 1000)
    guardia_sm.leer_archivo()
    enfermero = Enfermero("Maria", "5/12")

    for i in range(len(guardia_sm.lista_archivo)):
        guardia_sm.medicos_activos = random.randint(1, 10)

        for c in range(guardia_sm.medicos_activos):
            enfermero.clasificar(guardia_sm.lista_archivo[c])
            guardia_sm.lista_pacientes.append(guardia_sm.lista_archivo[c])
            del guardia_sm.lista_archivo[0]

        guardia_sm.armar_lista(
            guardia_sm.lista_pacientes.append(guardia_sm.lista_archivo[c]))


if __name__ == "__main__":
    main()

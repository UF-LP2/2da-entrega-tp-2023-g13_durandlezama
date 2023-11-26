"""creamos nuestro arbol"""
import binarytree
from library.minode import node


def arbol_sintomas() -> binarytree:
    """arbol de sintomas"""

    dif_respiar = node(50, "dificultad para respirar")
    perdida_sangre = node(100, "perdida de sangre externa")
    inconciente = node(70, "inconciente")
    sudoracion = node(40, "sudoracion")
    espuma_boca = node(60, "espuma_boca")

    nauseas_vomitos = node(30, "nauseas y vomitos")
    dolor = node(20, "dolor")
    desmayo = node(25, "desmayo")
    perdida_fuerza = node(15, "perdida de fuerza")
    golpe = node(35, "golpe")
    psicologica = node(55, "psicologica")
    fiebre = node(45, "fiebre")
    picazon = node(10, "picazon")
    no_urgente = node(0, "no es urgente")

    dif_respiar.left = perdida_sangre
    dif_respiar.right = nauseas_vomitos
    perdida_sangre.left = inconciente
    perdida_sangre.right = sudoracion
    sudoracion.right = espuma_boca

    # lado izquirdo

    nauseas_vomitos.left = dolor
    nauseas_vomitos.right = golpe
    dolor.left = desmayo
    dolor.right = perdida_fuerza
    perdida_fuerza.right = psicologica
    golpe.right = fiebre
    fiebre.right = picazon
    picazon.right = no_urgente

    return dif_respiar

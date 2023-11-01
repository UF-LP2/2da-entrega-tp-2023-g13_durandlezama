from binarytree import Node


def arbol_sintomas():
    """arbol de sintomas"""
    dif_respiar = Node(5)

    perdida_sangre = Node(2)
    inconciente = Node(1)
    sudoracion = Node(3)
    espuma_boca = Node(4)

    nauseas_vomitos = Node(10)
    dolor = Node(7)
    desmayo = Node(6)
    perdida_fuerza = Node(8)
    golpe = Node(11)
    psicologica = Node(9)
    fiebre = Node(12)
    picazon = Node(13)
    no_urgente = Node(14)

    perdida_sangre.left = dif_respiar
    inconciente.left = perdida_sangre
    sudoracion.right = perdida_sangre
    espuma_boca.right = sudoracion

    nauseas_vomitos.left = dif_respiar
    dolor.left = nauseas_vomitos
    desmayo.left = dolor
    perdida_fuerza.right = dolor
    psicologica.right = perdida_fuerza

    golpe.right = nauseas_vomitos
    fiebre.right = golpe
    picazon.right = fiebre
    no_urgente.right = picazon

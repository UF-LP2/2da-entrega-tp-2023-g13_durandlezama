
class Node:
    """clase de arbol"""

    def __init__(self, nombre, left=None, right=None):
        self.nombre = nombre
        self.left = left
        self.right = right

    def _str_(self):
        return str(self.nombre)


def arbol_sintomas() -> Node:
    """arbol de sintomas"""

    dif_respiar = Node("dificultad para respirar")
    perdida_sangre = Node("perdida de sangre externa")
    inconciente = Node("inconciente")
    sudoracion = Node("sudoracion")
    espuma_boca = Node("espuma_boca")

    nauseas_vomitos = Node("nauseas y vomitos")
    dolor = Node("dolor")
    desmayo = Node("desmayo")
    perdida_fuerza = Node("perdida de fuerza")
    golpe = Node("golpe")
    psicologica = Node("psicologica")
    fiebre = Node("fiebre")
    picazon = Node("picazon")
    no_urgente = Node("no es urgente")

    rojo = Node("rojo")
    amarillo = Node("amarillo")
    naranja = Node("naranja")
    verde = Node("verde")
    azul = Node("azul")

    dif_respiar.left = perdida_sangre
    dif_respiar.right = nauseas_vomitos

    perdida_sangre.left = inconciente
    perdida_sangre.right = sudoracion

    inconciente.left = rojo
    inconciente.right = naranja

    sudoracion.left = naranja
    sudoracion.right = espuma_boca

    espuma_boca.left = naranja
    espuma_boca.right = amarillo

    # lado izquirdo

    nauseas_vomitos.left = dolor
    nauseas_vomitos.right = golpe

    dolor.left = desmayo
    dolor.right = perdida_fuerza

    desmayo.left = amarillo
    desmayo.right = amarillo

    perdida_fuerza.left = amarillo
    perdida_fuerza.right = psicologica

    psicologica.left = amarillo
    psicologica.right = verde

    golpe.left = verde
    golpe.right = fiebre

    fiebre.left = verde
    fiebre.right = picazon

    picazon.left = verde
    picazon.right = no_urgente

    no_urgente.left = azul
    no_urgente.right = azul

    return dif_respiar

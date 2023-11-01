class Paciente:
    """calse paciente"""

    def __init__(self, nombre, edad, sintomas: []):
        self.nombre = nombre
        self.edad = edad
        self.clasificacion = ""
        self.tiempo_espera = 0
        self.sintomas = sintomas

    def llamar(self):
        """hola"""

        return "hola"

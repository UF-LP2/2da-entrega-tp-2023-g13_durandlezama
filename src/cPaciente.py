class Paciente:
    "clase paciente"
    def __init__(self, nombre, clasificacion):
        self.nombre=nombre
        self.clasificacion=clasificacion
        self.tiempo_espera=0
        self.sintomas=""
        self.tiempo_promedio=0

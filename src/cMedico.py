from cPaciente import Paciente

class Medico:
    """clase medico"""
    def __init__(self, nombre, estado):
        self.nombre=nombre 
        self.estado=estado
    
    def atender(self, paciente=Paciente):
        if paciente.clasificacion == "naranja" or paciente.clasificacion == "amarillo":
            derivar(paciente)
            frenar_tiempo()
        elif paciente.clasificacion == "verde":
            if paciente.vitales == "grave":
                derivar(paciente)
            else:
                ir_a_casa()
            frenar_tiempo()
        else:
            ir_a_casa()
            frenar_tiempo()


def derivar(paciente=Paciente):
    paciente.clasificacion=0
    pass

def ir_a_casa():  
    pass

def frenar_tiempo():
    pass

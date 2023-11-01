from cPaciente import Paciente

class Medico:
    """clase medico"""
    def __init__(self, nombre, estado):
        self.nombre=nombre 
        self.estado=estado
    
    def atender(self, paciente=Paciente):
        """clase medico"""
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
    """clase medico"""
    paciente.clasificacion=0
    ##pass

def ir_a_casa():
    """clase medico"""  
    ##pass

def frenar_tiempo():
    """clase medico"""
    ##pass

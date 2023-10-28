"""importamos la clase paciente""" 
from cPaciente import Paciente
from cMedico import Medico

class Guardia:
    """Módulo que proporciona la funcionalidad para la gestión de pacientes en la guardia médica."""
    
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad 
        self.lista_pacientes = [Paciente]
        self.medicos_activos = [Medico]
    
    def armar_lista(self, paciente):
        """funcion que arma la lista"""
        if paciente.clasificacion == "rojo":
            return "El paciente es prioridad 1"
        
        self.lista_pacientes.append(paciente)
        
        if len(self.lista_pacientes) <= 1:
            return self.lista_pacientes
        else:
            mitad = len(self.lista_pacientes) // 2
            izquierda = self.lista_pacientes[:mitad]
            derecha = self.lista_pacientes[mitad:]

        izquierda_ordenada = self.armar_lista(izquierda)
        derecha_ordenada = self.armar_lista(derecha)
        
        lista_ordenada = self.mayor(izquierda_ordenada, derecha_ordenada)
        return lista_ordenada

    def mayor(self, izquierda, derecha):
        """funcion para verificar quien es mayor"""
        resultado = []

        while len(izquierda) > 0 and len(derecha) > 0:
            tiempo_izq = self.evaluar_tiempo(izquierda[0])
            tiempo_derecha = self.evaluar_tiempo(derecha[0])
            
            if tiempo_izq <= tiempo_derecha:
                resultado.append(izquierda[0])
                izquierda.pop(0)
            else:
                resultado.append(derecha[0])
                derecha.pop(0)

        if len(izquierda) != 0:
            resultado.extend(izquierda)
        elif len(derecha) != 0: 
            resultado.extend(derecha)

        return resultado
    
    def evaluar_tiempo(self, paciente):
        """funcion para verificar el tiemp"""
        tiempo_naranja = 10
        tiempo_amarillo = 60
        tiempo_verde = 120
        tiempo_azul = 240

        if paciente.clasificacion == "naranja":
            return tiempo_naranja - paciente.tiempo_espera
        elif paciente.clasificacion == "amarillo":
            return tiempo_amarillo - paciente.tiempo_espera
        elif paciente.clasificacion == "verde":
            return tiempo_verde - paciente.tiempo_espera
        elif paciente.clasificacion == "azul":
            return tiempo_azul - paciente.tiempo_espera
        
    def Llamar_paciente(self):
      while len(self.lista_pacientes) > 0:
        for i in range(len(self.medicos_activos)):
            if self.medicos_activos[i].estado == True:
                self.medicos_activos[i].atender(self.lista_pacientes[i])
                del self.lista_pacientes[i]

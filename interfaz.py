"""importo la libreria de interfaz"""
import tkinter as tk
from src.cGuardia import Guardia
from src.cEnfermero import Enfermero
from src.cMedico import Medico
from src.cPaciente import Paciente
from main import lista_medicos
from datetime import datetime

colores = {
    "rojo": "#FD3B3B",
    "naranja": "#FE7B07",
    "amarillo": "#FFBA49",
    "verde": "#41DB72",
    "azul": "#3066BE"
}


class InterfazHospital:
    """clase de interfaz"""

    def __init__(self, root, pacientes):
        self.root = root
        self.pacientes = pacientes
        self.enfermero = Enfermero(
            "Nombre del enfermero", "Turno del enfermero")
        self.hospital = Guardia("guardia", 100, lista_medicos())
        self.canvas = tk.Canvas(root, width=1500, height=700)
        self.canvas.pack()
        # Lista para almacenar referencias a los objetos gráficos
        self.pacientes_graficos = []
        self.boton_mostrar_pacientes = tk.Button(
            root, text="Mostrar Pacientes Clasificados", command=self.mostrar_pacientes)
        self.boton_mostrar_pacientes.pack(pady=10)
        self.boton_ordenar_lista = tk.Button(
            root, text="Orden de Lista de Atención", command=self.ordenar_lista)
        self.boton_ordenar_lista.pack(pady=10)

    def mostrar_pacientes(self):
        """metodo de mostar pacientes"""

        for _ in range(min(20, len(self.pacientes))):
            paciente = self.pacientes.pop(0)
            self.enfermero.clasificar(paciente)
            clasi = paciente.clasificacion
            color = colores.get(clasi)
            self.dibujar_paciente(paciente.nombre, color)

        if self.pacientes:
            self.root.after(1000, self.mostrar_pacientes)

        # Deshabilita el botón después de mostrar los pacientes
        self.boton_mostrar_pacientes.config(state=tk.DISABLED)

    def ordenar_lista(self):
        """Ordenar lista de pacientes y mostrarlos en la interfaz gráfica"""

        pacientes_clasificados = []
        pacientes_clasificados = self.clasificar(self.pacientes)
        self.pacientes = self.hospital.armar_lista(pacientes_clasificados)

        for paciente in self.pacientes[:min(20, len(self.pacientes))]:
            color = colores.get(paciente.clasificacion)
            self.dibujar_paciente(paciente.nombre, color)

        if self.pacientes:
            self.root.after(1, self.mostrar_pacientes)

        # Deshabilita el botón después de ordenar y mostrar los pacientes
        self.boton_ordenar_lista.config(state=tk.DISABLED)
        # Deshabilita también el botón de mostrar pacientes para evitar conflictos
        self.boton_mostrar_pacientes.config(state=tk.DISABLED)

        # Deshabilita el botón después de ordenar y mostrar los pacientes
        self.boton_ordenar_lista.config(state=tk.DISABLED)

    def clasificar(self, pac_lista):
        """clasificar"""
        lista = []
        c: Paciente

        for c in pac_lista:
            self.enfermero.clasificar(c)
            lista.append(c)

        return lista

    def dibujar_paciente(self, nombre, color):
        """metood de dibujar"""

        # Calcula la fila en la que se encuentra el paciente
        fila = len(self.pacientes_graficos) // 10
        # Calcula la columna en la que se encuentra el paciente
        columna = len(self.pacientes_graficos) % 10
        x = 50 + columna * 140  # Espaciado horizontal entre círculos
        y = 50 + fila * 100  # Espaciado vertical entre filas de círculos
        radio = 20
        circulo = self.canvas.create_oval(
            x - radio, y - radio, x + radio, y + radio, fill=color)
        texto = self.canvas.create_text(x, y, text=nombre)
        self.pacientes_graficos.append((circulo, texto))


guardia = Guardia("", 122, [])
guardia.leer_archivo()
pac = guardia.lista_archivo

# Configuración de la ventana
app = tk.Tk()
app.title("Simulación de Triage Hospitalario")

# Inicia la simulación
interfaz = InterfazHospital(app, pac)

# Iniciar el bucle principal de la interfaz gráfica
app.mainloop()

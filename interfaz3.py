import tkinter as tk
from src.cGuardia import Guardia
from src.cEnfermero import Enfermero
from src.cMedico import Medico
from src.cPaciente import Paciente
from datetime import datetime
from library.leer_archivos import leer_archivo
from library.leer_archivos import archivo_m
from library.leer_archivos import archivo_e

colores = {
    "Rojo": "#FD3B3B",
    "Naranja": "#FE7B07",
    "Amarillo": "#FFBA49",
    "Verde": "#41DB72",
    "Azul": "#3066BE"
}


class InterfazHospital:

    def __init__(self, root, pacientes):
        self.root = root
        self.pacientes = pacientes
        self.enfermero = Enfermero(
            "Nombre del enfermero", "Turno del enfermero")
        self.hospital = Guardia("guardia", 100, archivo_m())
        self.canvas = tk.Canvas(root, width=1500, height=700)
        self.canvas.pack()
        # Lista para almacenar referencias a los objetos gráficos
        self.pacientes_graficos = []
        self.boton_mostrar_pacientes = tk.Button(
            root, text="Mostrar Pacientes Clasificados", command=self.mostrar_pacientes)
        self.boton_mostrar_pacientes.pack(pady=20)
        self.etiqueta_info = tk.Label(root, text="")
        self.etiqueta_info.pack(pady=10)

    def mostrar_pacientes(self):
        """metodo de mostar pacientes"""

        if self.pacientes:
            paciente = self.pacientes.pop(0)
            self.enfermero.clasificar(paciente)
            clasi = paciente.color
            color = colores.get(clasi)
            self.dibujar_paciente(paciente.nombre, color)

            # Actualiza la etiqueta para mostrar la información
            info = f"{paciente.nombre}: {paciente.color}"
            self.etiqueta_info.config(text=info)

            # Actualiza la interfaz cada segundo
            self.root.after(100, self.mostrar_pacientes)
        else:
            # Deshabilita el botón después de mostrar todos los pacientes
            self.boton_mostrar_pacientes.config(state=tk.DISABLED)

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
pac = leer_archivo()

# Configuración de la ventana
app = tk.Tk()
app.title("Simulación de Triage Hospitalario")

# Inicia la simulación
interfaz = InterfazHospital(app, pac)

# Iniciar el bucle principal de la interfaz gráfica
app.mainloop()

"""importo la libreria de interfaz"""
import tkinter as tk
from cGuardia import Guardia

guardia = Guardia("gh", 100, [])
app = tk.Tk()
app.geometry("300x600")
app.configure(background="black")
tk.Wm.wm_title(app, "hola")


tk.Button(
    app,
    text="hola",
    font=("Arial", 14),
    bg="black",
    fg="white",

).pack(
    fill=tk.BOTH,
    expand=True,
)

tk
app.mainloop()

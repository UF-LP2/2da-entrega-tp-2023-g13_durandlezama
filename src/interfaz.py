"""importo la libreria de interfaz"""
import tkinter as tk

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
    command=lambda: print("hola"),
).pack(
    fill=tk.BOTH,
    expand=True,
)
app.mainloop()

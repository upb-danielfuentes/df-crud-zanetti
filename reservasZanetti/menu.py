import tkinter as tk
from gui_horario import VentanaCRUD

def abrir_ventana1():
    ventana = VentanaCRUD("Ventana 1")
    ventana.mostrar()

def crear_menu():
    root = tk.Tk()
    root.title("Menú con Botones")

    boton1 = tk.Button(root, text="Abrir Ventana 1", command=abrir_ventana1)

    boton1.pack()

    root.mainloop()

if __name__ == "__main__":
    crear_menu()

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ttkthemes as themes
import reserva as res
import horario as hor

class VentanaCRUD:


    def __init__(self, titulo):
        self.ventana = tk.Toplevel()
        self.ventana.title(titulo)
        
    # Crear la ventana principal
    window = themes.ThemedTk()
    window.get_themes()
    window.set_theme("blue")
    window.title("Gestión de Reservas Zanetti 0.0.1")

    # Declaración de las variables locales para capturar información
    txtcedula_residente = tk.StringVar()
    txtnombre_residente = tk.StringVar()
    txtapellido_residente = tk.StringVar()
    txtcelular_residente = tk.StringVar()
    txtapto_residente = tk.StringVar()
    txtarea_comun = tk.StringVar()
    txtfecha_reserva = tk.StringVar()
    txtdescripcion = tk.StringVar()
    txtid_horario = tk.StringVar()
    # Fin de la declaración

    # Crear una pestaña
    notebook = ttk.Notebook(window)
    notebook.pack(fill="both", expand=True)

    ############# LISTAR TODAS LAS RESERVAS ###################

    # Pestaña de Listado de Reservas
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text="Listado de Reservas 🗂️")

    # Botón para listar todas las reservas
    list_button1 = ttk.Button(tab1, text="Listar Todas las Reservas 🗂️", command=listar_todas_reservas)
    list_button1.pack(pady=10)

    # Crear una tabla para mostrar las reservas
    columns = ("ID Reserva", "Cédula Residente", "Nombre Residente", "Apellido Residente", "Celular Residente", "Apartamento", "Área Común", "Fecha Reserva")
    tree = ttk.Treeview(tab1, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
    tree.pack(padx=10, pady=10)

    ############# AGREGAR RESERVA ###################

    # Pestaña de Agregar Reserva
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text="Agregar Reserva 📆")

    # Entradas para agregar una nueva reserva
    cedula_label = ttk.Label(tab2, text="Cédula Residente:")
    cedula_label.pack()
    cedula_entry = ttk.Entry(tab2, textvariable=txtcedula_residente)
    cedula_entry.pack()

    nombre_label = ttk.Label(tab2, text="Nombre Residente:")
    nombre_label.pack()
    nombre_entry = ttk.Entry(tab2, textvariable=txtnombre_residente)
    nombre_entry.pack()

    apellido_label = ttk.Label(tab2, text="Apellido Residente:")
    apellido_label.pack()
    apellido_entry = ttk.Entry(tab2, textvariable=txtapellido_residente)
    apellido_entry.pack()

    celular_label = ttk.Label(tab2, text="Celular Residente:")
    celular_label.pack()
    celular_entry = ttk.Entry(tab2, textvariable=txtcelular_residente)
    celular_entry.pack()

    apartamento_label = ttk.Label(tab2, text="Apartamento:")
    apartamento_label.pack()
    apartamento_entry = ttk.Entry(tab2, textvariable=txtapto_residente)
    apartamento_entry.pack()

    area_comun_label = ttk.Label(tab2, text="Área Común:")
    area_comun_label.pack()
    area_comun_entry = ttk.Entry(tab2, textvariable=txtarea_comun)
    area_comun_entry.pack()

    fecha_label = ttk.Label(tab2, text="Fecha Reserva:")
    fecha_label.pack()
    fecha_entry = ttk.Entry(tab2, textvariable=txtfecha_reserva)
    fecha_entry.pack()

    # Botón para agregar una nueva reserva
    add_button = ttk.Button(tab2, text="Agregar Reserva", command=agregar_nueva_reserva)
    add_button.pack(pady=10)

    ############# ACTUALIZAR RESERVA ###################

    # Pestaña de Actualizar Reserva
    tab3 = ttk.Frame(notebook)
    notebook.add(tab3, text="Actualizar Reserva 📖")

    # Entrada para el ID del Residente a actualizar
    id_label = ttk.Label(tab3, text="Cedula Residente:")
    id_label.pack()
    id_entry = ttk.Entry(tab3, textvariable=txtcedula_residente)
    id_entry.pack()

    # Botón para listar una reserva por ID
    list_id_button = ttk.Button(tab3, text="Listar Reserva por Cedula", command=listar_reserva_por_id)
    list_id_button.pack(pady=10)

    # Entradas para actualizar una reserva
    update_cedula_label = ttk.Label(tab3, text="Cédula Residente:")
    update_cedula_label.pack()
    update_cedula_entry = ttk.Entry(tab3, textvariable=txtcedula_residente)
    update_cedula_entry.pack()

    update_nombre_label = ttk.Label(tab3, text="Nombre Residente:")
    update_nombre_label.pack()
    update_nombre_entry = ttk.Entry(tab3, textvariable=txtnombre_residente)
    update_nombre_entry.pack()

    update_apellido_label = ttk.Label(tab3, text="Apellido Residente:")
    update_apellido_label.pack()
    update_apellido_entry = ttk.Entry(tab3, textvariable=txtapellido_residente)
    update_apellido_entry.pack()

    update_celular_label = ttk.Label(tab3, text="Celular Residente:")
    update_celular_label.pack()
    update_celular_entry = ttk.Entry(tab3, textvariable=txtcelular_residente)
    update_celular_entry.pack()

    update_apartamento_label = ttk.Label(tab3, text="Apartamento:")
    update_apartamento_label.pack()
    update_apartamento_entry = ttk.Entry(tab3, textvariable=txtapto_residente)
    update_apartamento_entry.pack()

    update_area_comun_label = ttk.Label(tab3, text="Área Común:")
    update_area_comun_label.pack()
    update_area_comun_entry = ttk.Entry(tab3, textvariable=txtarea_comun)
    update_area_comun_entry.pack()

    update_fecha_label = ttk.Label(tab3, text="Fecha:")
    update_fecha_label.pack()
    update_fecha_entry = ttk.Entry(tab3, textvariable=txtfecha_reserva)
    update_fecha_entry.pack()

    # Botón para actualizar una reserva
    update_button = ttk.Button(tab3, text="Actualizar Reserva", command=actualizar_reserva)
    update_button.pack(pady=10)

    ############# ELIMINAR RESERVA ###################

    # Pestaña de Eliminar Reserva
    tab4 = ttk.Frame(notebook)
    notebook.add(tab4, text="Eliminar Reserva ❌")

    # Entrada para el ID de reserva a eliminar
    id_label_delete = ttk.Label(tab4, text="ID de Reserva:")
    id_label_delete.pack()
    id_entry_delete = ttk.Entry(tab4, textvariable=txtcedula_residente)
    id_entry_delete.pack()

    # Botón para eliminar una reserva
    delete_button = ttk.Button(tab4, text="Eliminar Reserva", command=eliminar_reserva)
    delete_button.pack(pady=10)

    def mostrar(self):
        self.ventana.mainloop()

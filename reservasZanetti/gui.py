import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ttkthemes as themes
import reserva as res
import horario as hor

def main():
    window.mainloop()

# Función para listar todas las reservas
def listar_todas_reservas():
    result = res.listar_todas_reservas()
    if result["Respuesta"]:
        reservas = result["Mensaje"]
        # Limpiar la tabla antes de actualizarla
        for i in tree.get_children():
            tree.delete(i)
        # Llenar la tabla con los datos de las reservas
        for reserva in reservas:
            tree.insert("", "end", values=reserva)
    else:
        messagebox.showerror("Información", result["Mensaje"])

# Función para listar una reserva por ID
def listar_reserva_por_id():
    ID_Reserva = id_entry.get()
    if ID_Reserva:
        result = res.listar_reserva_id(ID_Reserva)
        if result["Respuesta"]:
            reserva = result["Mensaje"]
            # Limpiar la tabla antes de actualizarla
            for i in tree.get_children():
                tree.delete(i)
            # Llenar la tabla con los datos de la reserva
            tree.insert("", "end", values=reserva)
        else:
            messagebox.showerror("Información", result["Mensaje"])
    else:
        messagebox.showerror("Información", "Por favor, ingrese un ID de reserva válido.")

# Función para agregar una nueva reserva
def agregar_nueva_reserva():
    if cedula_entry.get().isnumeric():
        reserva = {
            "cedula_residente": cedula_entry.get(),
            "nombre_residente": nombre_entry.get(),
            "apellido_residente": apellido_entry.get(),
            "celular_residente": int(celular_entry.get()),
            "apartamento_residente": int(apartamento_entry.get()),
            "area_comun_id": area_comun_entry.get(),
            "fecha_reserva": fecha_entry.get()
        }
        result = res.agregar_reserva(reserva)
        if result["Respuesta"]:
            messagebox.showinfo("Información", result["Mensaje"])
            # Limpiar los campos después de agregar la reserva
            cedula_entry.delete(0, tk.END)
            nombre_entry.delete(0, tk.END)
            apellido_entry.delete(0, tk.END)
            celular_entry.delete(0, tk.END)
            apartamento_entry.delete(0, tk.END)
            area_comun_entry.delete(0, tk.END)
            fecha_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error en el sistema", "La cédula no es un valor numérico")

# Función para actualizar una reserva
def actualizar_reserva():
    if cedula_entry.get().isnumeric():
        reserva = {
            "cedula_residente": cedula_entry.get(),
            "nombre_residente": nombre_entry.get(),
            "apellido_residente": apellido_entry.get(),
            "celular_residente": int(celular_entry.get()),
            "apartamento_residente": apartamento_entry.get(),
            "area_comun_id": area_comun_entry.get(),
            "fecha": fecha_entry.get()
        }
        result = res.actualizar_reserva(reserva)
        messagebox.showinfo("Función Actualizar", result.get("Mensaje"))
    else:
        messagebox.showerror("Información", "Por favor, ingrese un ID de reserva válido.")

# Función para eliminar una reserva
def eliminar_reserva():
    if cedula_entry.get() != "" and cedula_entry.get().isnumeric():
        id_reserva = cedula_entry.get()
        respuesta = res.eliminar_reserva(id_reserva)
        messagebox.showinfo("Función Eliminar", respuesta.get("Mensaje"))
    else:
        messagebox.showwarning("Error en el sistema", "Debe ingresar un valor numérico en el ID")

# Función para listar todas las horarios
def listar_todas_horarios():
    result = hor.listar_todos_horario()
    if result["Respuesta"]:
        horarios = result["Mensaje"]
        # Limpiar la tabla antes de actualizarla
        for i in tree.get_children():
            tree.delete(i)
        # Llenar la tabla con los datos de las horarios
        for horario in horarios:
            tree.insert("", "end", values=horario)
    else:
        messagebox.showerror("Información", result["Mensaje"])

# Función para listar una horario por ID
def listar_horario_por_id():
    ID_Horario = id_entry.get()
    if ID_Horario:
        result = hor.listar_horario_id(ID_Horario)
        if result["Respuesta"]:
            horario = result["Mensaje"]
            # Limpiar la tabla antes de actualizarla
            for i in tree.get_children():
                tree.delete(i)
            # Llenar la tabla con los datos de la horario
            tree.insert("", "end", values=horario)
        else:
            messagebox.showerror("Información", result["Mensaje"])
    else:
        messagebox.showerror("Información", "Por favor, ingrese un ID de horario válido.")

# Función para agregar un nuevo horario
def agregar_nueva_horario():
    if id.get().isnumeric():
        horario = {
            "id": id_horario_entry.get(),
            "descripcion": descripcion_entry.get(),
        }
        result = hor.agregar_horario(horario)
        if result["Respuesta"]:
            messagebox.showinfo("Información", result["Mensaje"])
            id_entry.delete(0, tk.END)
            descripcion_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error en el sistema", "El Id no es un valor numérico")

# Función para actualizar un Horario
def actualizar_horario():
    if id_entry.get().isnumeric():
        horario = {
            "id": id_entry.get(),
            "descripcion": descripcion_entry.get(),
        }
        result = hor.actualizar_horario(horario)
        messagebox.showinfo("Función Actualizar", result.get("Mensaje"))
    else:
        messagebox.showerror("Información", "Por favor, ingrese un ID de Horario válido.")

# Función para eliminar un Horario
def eliminar_horario():
    if id_entry.get() != "" and id_entry.get().isnumeric():
        id = id_horario_entry.get()
        respuesta = hor.eliminar_horario(id)
        messagebox.showinfo("Función Eliminar", respuesta.get("Mensaje"))
    else:
        messagebox.showwarning("Error en el sistema", "Debe ingresar un valor numérico en el ID")

# Crear la ventana principal
window = themes.ThemedTk()
window.get_themes()
window.set_theme("ubuntu")
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
list_button = ttk.Button(tab1, text="Listar Todas las Reservas 🗂️", command=listar_todas_reservas)
list_button.pack(pady=10)

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

############# LISTAR TODAS LAS HORARIOS ###################

# Pestaña de Listado de Horarios
tab5 = ttk.Frame(notebook)
notebook.add(tab5, text="Listado de Horarios 🗂️")

# Botón para listar todas las horarios
list_button = ttk.Button(tab5, text="Listar Todas los Horarios 🗂️", command=listar_todas_horarios)
list_button.pack(pady=10)

# Crear una tabla para mostrar las horarios
columns = ("ID", "Descripcion")
tree = ttk.Treeview(tab5, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack(padx=10, pady=10)

############# AGREGAR HORARIO ###################

# Pestaña de Agregar Horario
tab6 = ttk.Frame(notebook)
notebook.add(tab6, text="Agregar Horario 📆")

# Entradas para agregar un nuevo horario
descripcion_label = ttk.Label(tab6, text="Nombre Residente:")
descripcion_label.pack()
descripcion_entry = ttk.Entry(tab6, textvariable=txtdescripcion)
descripcion_entry.pack()

# Botón para agregar una nueva horario
add_button = ttk.Button(tab6, text="Agregar Horario", command=agregar_nueva_horario)
add_button.pack(pady=10)

############# ACTUALIZAR HORARIO ###################

# Pestaña de Actualizar Horario
tab7 = ttk.Frame(notebook)
notebook.add(tab7, text="Actualizar Horario 📖")

# Entrada para el ID del Residente a actualizar
id_label = ttk.Label(tab7, text="Id Horario:")
id_label.pack()
id_horario_entry = ttk.Entry(tab7, textvariable=txtid_horario)
id_horario_entry.pack()

# Botón para listar una horario por ID
list_id_button = ttk.Button(tab7, text="Listar Horario por ID", command=listar_horario_por_id)
list_id_button.pack(pady=10)

# Entradas para actualizar una horario
update_descripcion_label = ttk.Label(tab7, text="Id Horario:")
update_descripcion_label.pack()
update_descripcion_entry = ttk.Entry(tab7, textvariable=txtnombre_residente)
update_descripcion_entry.pack()

# Botón para actualizar una horario
update_button = ttk.Button(tab7, text="Actualizar Horario", command=actualizar_horario)
update_button.pack(pady=10)

############# ELIMINAR HORARIO ###################

# Pestaña de Eliminar Horario
tab8 = ttk.Frame(notebook)
notebook.add(tab8, text="Eliminar Horario")

# Entrada para el ID de horario a eliminar
id_label_delete = ttk.Label(tab8, text="ID de Horario:")
id_label_delete.pack()
id_horario_entry = ttk.Entry(tab8, textvariable=txtid_horario)
id_horario_entry.pack()

# Botón para eliminar una horario
delete_button = ttk.Button(tab8, text="Eliminar Horario", command=eliminar_horario)
delete_button.pack(pady=10)


############# INICIA LA APLICACION ###################

if __name__ == "__main__":
    main()

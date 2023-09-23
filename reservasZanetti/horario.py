import conexion_db as con

# Listar por Horario    
def listar_todos_horario():
    try:
        db = con.conectar()
        miCursor = db.cursor()

        sql = "SELECT * FROM tb_Horario"
        miCursor.execute(sql)
        reservas = miCursor.fetchall()
        db.commit()

        if reservas:
            miCursor.close()
            db.close()
            return {"Respuesta": True, "Mensaje": reservas}
        else:
            miCursor.close()
            db.close()
            return {"Respuesta": False, "Mensaje": "No existe información en la tabla tb_Horario"}

    except Exception as ex:
        miCursor.close()
        db.close()
        return {"Respuesta": False, "Mensaje": str(ex)}

# Listar un Horario por ID
def listar_horario_id(ID_Horario):
    try:
        db = con.conectar()
        miCursor = db.cursor()

        sql = "SELECT * FROM tb_Horario WHERE id="+ID_Horario
        miCursor.execute(sql)
        horario = miCursor.fetchone()
        db.commit()

        if horario:
            id, descripcion = horario
            DatoBusqueda = {
                "id": id,
                "descripcion": descripcion
               
            }
            miCursor.close()
            db.close()
            return {"Respuesta": True, "Mensaje": DatoBusqueda}
        else:
            miCursor.close()
            db.close()
            return {"Respuesta": False, "Mensaje": "No existe información en la base de datos"}

    except Exception as ex:
        return {"Respuesta": False, "Mensaje": str(ex)}

# Agregar una Horario
def agregar_horario(horario):
    try:
        db = con.conectar()
        miCursor = db.cursor()

        columnas = ", ".join(horario.keys())
        valores = tuple(horario.values())

        placeholders = ", ".join(["?"] * len(valores))

        sql = f"INSERT INTO tb_Horario ({columnas}) VALUES ({placeholders})"
        miCursor.execute(sql, valores)
        db.commit()

        if miCursor.rowcount > 0:
            db.close()
            return {"Respuesta": True, "Mensaje": "Reserva registrada en la base de datos"}
        else:
            db.close()
            return {"Respuesta": False, "Mensaje": "La reserva no fue agregada a la base de datos"}

    except Exception as ex:
        db.close()
        return {"Respuesta": False, "Mensaje": str(ex)}

# Actualizar un Horario
def actualizar_horario(Horario):
    try:
        db = con.conectar()
        miCursor = db.cursor()

        valores = tuple(Horario.values())
        id = Horario.get("id")

        sql = """UPDATE tb_Horario SET descripcion=? WHERE id={ID_HORARIO}""".format(ID_HORARIO= id) 

        miCursor.execute(sql,valores)
        db.commit()

        if miCursor.rowcount > 0:
            miCursor.close()
            db.close()
            return {"Respuesta": True, "Mensaje": "Reserva actualizada"}
        else:
            miCursor.close()
            db.close()
            return {"Respuesta": False, "Mensaje": "No existe la reserva en la base de datos"}

    except Exception as ex:
        miCursor.close()
        db.close()
        return {"Respuesta": False, "Mensaje": str(ex)}

# Eliminar un Horario
def eliminar_horario(ID_Horario):
    try:
        db = con.conectar()
        miCursor = db.cursor()

        sql = "DELETE FROM tb_Horario WHERE id={id}".format(id=ID_Horario)
        miCursor.execute(sql)
        db.commit()
        eliminado = miCursor.rowcount > 0

        if eliminado:
            miCursor.close()
            db.close()
            return {"Respuesta": True, "Mensaje": "Reserva eliminada"}
        else:
            miCursor.close()
            db.close()
            return {"Respuesta": False, "Mensaje": "No existe la reserva en la base de datos"}

    except Exception as ex:
        miCursor.close()
        db.close()
        return {"Respuesta": False, "Mensaje": str(ex)}

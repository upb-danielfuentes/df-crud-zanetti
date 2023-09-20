import conexion_db as con

# Listar todas las Reservas Existentes
def listar_todas_reservas():
    try:
        db = con.conectar()
        miCursor = db.cursor()

        sql = "SELECT * FROM tb_Reserva ORDER BY id_reserva ASC"
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
            return {"Respuesta": False, "Mensaje": "No existe información en la tabla tb_Reserva"}

    except Exception as ex:
        miCursor.close()
        db.close()
        return {"Respuesta": False, "Mensaje": str(ex)}

# Listar una Reserva por ID
def listar_reserva_id(ID_Reserva):
    try:
        db = con.conectar()
        miCursor = db.cursor()

        sql = "SELECT * FROM tb_Reserva WHERE cedula_residente="+ID_Reserva
        miCursor.execute(sql)
        reserva = miCursor.fetchone()
        db.commit()

        if reserva:
            id_reserva, cedula_residente, nombre_residente, apellido_residente, celular_residente, apartamento_residente, area_comun_id, fecha_reserva = reserva
            DatoBusqueda = {
                "id_reserva": id_reserva,
                "cedula_residente": cedula_residente,
                "nombre_residente": nombre_residente,
                "apellido_residente": apellido_residente,
                "celular_residente": celular_residente,
                "apartamento_residente": apartamento_residente,
                "area_comun_id": area_comun_id,
                "fecha_reserva": fecha_reserva
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

# Agregar una Reserva
def agregar_reserva(reserva):
    try:
        db = con.conectar()
        miCursor = db.cursor()

        columnas = ", ".join(reserva.keys())
        valores = tuple(reserva.values())

        placeholders = ", ".join(["?"] * len(valores))

        sql = f"INSERT INTO tb_Reserva ({columnas}) VALUES ({placeholders})"
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

# Actualizar una Reserva
def actualizar_reserva(Reserva):
    try:
        db = con.conectar()
        miCursor = db.cursor()

        valores = tuple(Reserva.values())
        cedula_residente = Reserva.get("cedula_residente")

        sql = """UPDATE tb_Reserva 
                 SET cedula_residente=?, nombre_residente=?, apellido_residente=?, 
                 celular_residente=?, apartamento_residente=?, area_comun_id=?, fecha_reserva=?
                 WHERE cedula_residente={CED_RESI}""".format(CED_RESI= cedula_residente)

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

# Eliminar una Reserva
def eliminar_reserva(ID_Reserva):
    try:
        db = con.conectar()
        miCursor = db.cursor()

        sql = "DELETE FROM tb_Reserva WHERE id_reserva={id_reserva}".format(id_reserva=ID_Reserva)
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
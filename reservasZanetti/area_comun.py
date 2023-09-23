import conexion_db as con

# Listar por Area Comun   
def listar_todas_area():
    try:
        db = con.conectar()
        miCursor = db.cursor()

        sql = "SELECT * FROM tb_AreaComun"
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
            return {"Respuesta": False, "Mensaje": "No existe información en la tabla tb_AreaComun"}

    except Exception as ex:
        miCursor.close()
        db.close()
        return {"Respuesta": False, "Mensaje": str(ex)}

# Listar un Area por ID
def listar_area_id(ID_Area):
    try:
        db = con.conectar()
        miCursor = db.cursor()

        sql = "SELECT * FROM tb_AreaComun WHERE id="+ID_Area
        miCursor.execute(sql)
        area = miCursor.fetchone()
        db.commit()

        if area:
            id, nombre_area,capacidad_area,horario_id = area
            DatoBusqueda = {
                "id": id,
                "nombre_area": nombre_area,
                'capacidad_area': capacidad_area,
                "horario_id": horario_id
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

# Agregar una Area
def agregar_area(area):
    try:
        db = con.conectar()
        miCursor = db.cursor()

        columnas = ", ".join(area.keys())
        valores = tuple(area.values())

        placeholders = ", ".join(["?"] * len(valores))

        sql = f"INSERT INTO tb_AreaComun ({columnas}) VALUES ({placeholders})"
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

# Actualizar un Area
def actualizar_area(Area):
    try:
        db = con.conectar()
        miCursor = db.cursor()

        valores = tuple(Area.values())
        id = Area.get("id")

        sql = """UPDATE tb_AreaComun SET nombre_area=?, capacidad_area=?, horario_id=? WHERE id={ID_AREA}""".format(ID_AREA= id) 

        miCursor.execute(sql,valores)
        db.commit()

        if miCursor.rowcount > 0:
            miCursor.close()
            db.close()
            return {"Respuesta": True, "Mensaje": "Area Comun Actualizada Correctamente"}
        else:
            miCursor.close()
            db.close()
            return {"Respuesta": False, "Mensaje": "No existe el Area Comun para actualizar en la base de datos"}

    except Exception as ex:
        miCursor.close()
        db.close()
        return {"Respuesta": False, "Mensaje": str(ex)}

# Eliminar un Area
def eliminar_area(ID_Area):
    try:
        db = con.conectar()
        miCursor = db.cursor()

        sql = "DELETE FROM tb_AreaComun WHERE id={id}".format(id=ID_Area)
        miCursor.execute(sql)
        db.commit()
        eliminado = miCursor.rowcount > 0

        if eliminado:
            miCursor.close()
            db.close()
            return {"Respuesta": True, "Mensaje": "Area Comun Eliminada"}
        else:
            miCursor.close()
            db.close()
            return {"Respuesta": False, "Mensaje": "No existe la reserva en la base de datos"}

    except Exception as ex:
        miCursor.close()
        db.close()
        return {"Respuesta": False, "Mensaje": str(ex)}
    
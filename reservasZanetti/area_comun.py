import conexion_db as con

# Listar por Area Comun    
def listar_todas_areas():
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
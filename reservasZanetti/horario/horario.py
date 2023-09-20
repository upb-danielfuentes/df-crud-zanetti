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


    
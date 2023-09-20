import sqlite3

DB_NAME = "db_ReservasZanetti.sqlite"

def conectar():
    try:
        conexion = sqlite3.connect(DB_NAME)
        print("✅ Conexión establecida con éxito ✅")
        return conexion
    except sqlite3.Error as ex:
        print("❌ Error al conectar con la base de datos: ❌", ex)
        return None

def crear_tablas(conexion):
    if not conexion:
        return
    
    try:
        cursor = conexion.cursor()
        
        # Definir las sentencias SQL en una lista para facilitar la lectura
        sql_statements = [
            """CREATE TABLE IF NOT EXISTS tb_Horario (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                descripcion TEXT NOT NULL
            );""",
            
            """CREATE TABLE IF NOT EXISTS tb_AreaComun (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                nombre_area TEXT NOT NULL,
                capacidad_area INTEGER NOT NULL,
                horario_id INTEGER NOT NULL,
                FOREIGN KEY (horario_id) REFERENCES tb_Horario (id)
            );""",
            
            """CREATE INDEX IF NOT EXISTS idx_horario_id ON tb_AreaComun (horario_id);""",
            
            """CREATE TABLE IF NOT EXISTS tb_Reserva (
                id_reserva INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                cedula_residente INTEGER NOT NULL,
                nombre_residente TEXT NOT NULL,
                apellido_residente TEXT NOT NULL,
                celular_residente INTEGER NOT NULL,
                apartamento_residente INTEGER NOT NULL,
                area_comun_id INTEGER NOT NULL,
                fecha_reserva DATE NOT NULL,
                FOREIGN KEY (area_comun_id) REFERENCES tb_AreaComun (id)
            );""",
            
            """CREATE INDEX IF NOT EXISTS idx_area_comun_id ON tb_Reserva (area_comun_id);""",
            
            """INSERT INTO tb_Horario (id, descripcion) VALUES (1, 'Manana');""",
            """INSERT INTO tb_Horario (id, descripcion) VALUES (2, 'Tarde');""",
            """INSERT INTO tb_Horario (id, descripcion) VALUES (3, 'Noche');""",
            
            """INSERT INTO tb_AreaComun (id, nombre_area, capacidad_area, horario_id) VALUES (1, 'Piscina', 50, 1);""",
            """INSERT INTO tb_AreaComun (id, nombre_area, capacidad_area, horario_id) VALUES (2, 'Piscina', 50, 2);""",
            """INSERT INTO tb_AreaComun (id, nombre_area, capacidad_area, horario_id) VALUES (3, 'Piscina', 50, 3);""",
            """INSERT INTO tb_AreaComun (id, nombre_area, capacidad_area, horario_id) VALUES (4, 'BBQ', 100, 1);""",
            """INSERT INTO tb_AreaComun (id, nombre_area, capacidad_area, horario_id) VALUES (5, 'BBQ', 100, 2);""",
            """INSERT INTO tb_AreaComun (id, nombre_area, capacidad_area, horario_id) VALUES (6, 'BBQ', 100, 3);""",
            
            """INSERT INTO tb_Reserva (id_reserva, cedula_residente, nombre_residente, apellido_residente, celular_residente, apartamento_residente, area_comun_id, fecha_reserva) VALUES (1, 1018436098, 'Daniel', 'Fuentes', 3013366588, 2624, 4, '1696032000000');""",
        ]
        
        for statement in sql_statements:
            cursor.execute(statement)
        
        print("✅ Tablas creadas con éxito ✅")
        conexion.commit()
    except sqlite3.Error as ex:
        print("❌ Error al crear las tablas: ❌", ex)
    finally:
        cursor.close()

if __name__ == "__main__":
    conexion = conectar()
    if conexion:
        crear_tablas(conexion)
        conexion.close()

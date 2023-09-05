class AreaComun:
    def __init__(self, nombre, capacidad, horario_disponibilidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.horario_disponibilidad = horario_disponibilidad
        self.reservas = []

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)

    def __str__(self): # str() es una función que retorna un string
        return f"Área común: {self.nombre}, Capacidad: {self.capacidad}, Disponibilidad Horaria desde las: {self.horario_disponibilidad}"

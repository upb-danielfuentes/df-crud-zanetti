class Reserva:
    def __init__(self, residente, area_comun, fecha, hora_inicio, hora_fin):
        self.residente = residente
        self.area_comun = area_comun
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def __str__(self):
        return f"Reserva de {self.residente} para {self.area_comun.nombre} el {self.fecha} de {self.hora_inicio} a {self.hora_fin}"
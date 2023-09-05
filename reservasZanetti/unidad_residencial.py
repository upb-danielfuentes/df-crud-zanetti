class UnidadResidencial:
    def __init__(self):
        self.areas_comunes = []

    def agregar_area_comun(self, area_comun):
        self.areas_comunes.append(area_comun)

    def __str__(self):
        return "Unidad Residencial Zanetti con áreas comunes: " + ", ".join(area.nombre for area in self.areas_comunes)

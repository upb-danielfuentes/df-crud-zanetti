from reserva import Reserva
from area_comun import AreaComun
from unidad_residencial import UnidadResidencial

class GestorReservas:
    def __init__(self):
        self.unidad_residencial = UnidadResidencial()

    def agregar_area_comun(self, nombre, capacidad, horario_disponibilidad):
        area_comun = AreaComun(nombre, capacidad, horario_disponibilidad)
        self.unidad_residencial.agregar_area_comun(area_comun)

    def agregar_reserva(self, nombre_residente, nombre_area, fecha, hora_inicio, hora_fin):
        area_seleccionada = next((area for area in self.unidad_residencial.areas_comunes if area.nombre == nombre_area), None) # next() retorna el primer elemento de un iterador
        
        if area_seleccionada:
            reserva = Reserva(nombre_residente, area_seleccionada, fecha, hora_inicio, hora_fin)
            area_seleccionada.agregar_reserva(reserva)
        else:
            print(f"El área común '{nombre_area}' no existe.")

    def mostrar_info_unidad_residencial(self):
        print("Areas disponibles:")
        print(self.unidad_residencial)

    def mostrar_info_areas_comunes(self):
        for area in self.unidad_residencial.areas_comunes:
            print("\n" + str(area))
            print("Reservas:")
            for reserva in area.reservas:
                print(reserva)

if __name__ == "__main__":
    gestor = GestorReservas()

    while True:
        print("----------------------------------------------")
        print("\nBienvenido al sistema de reservas de la unidad residencial Zanetti. 🏢")
        print("----------------------------------------------")
        print("\nSeleccione una de las siguientes opciones disponibles a la fecha:")
        print("1. Agregar área común del edificio 🏗️")
        print("2. Agregar reserva de área común 📅")
        print("3. Mostrar información de la unidad residencial Zanetti 🏢")
        print("4. Mostrar información de las áreas comunes 🏗️")
        print("5. Salir 🚪")
        print("----------------------------------------------")

        opcion = input("Seleccione una opción: ")
        print("----------------------------------------------")

        if opcion == "1":
            nombre = input("Ingrese el nombre del área común: ")
            capacidad = int(input("Ingrese la capacidad que le cabe al área común: "))
            horario = input(f"Ingrese el horario (HH:MM) de disponibilidad de {nombre} : ")
            gestor.agregar_area_comun(nombre, capacidad, horario)
        elif opcion == "2":
            nombre_residente = input("Ingrese el nombre del residente: ")
            nombre_area = input("Ingrese el nombre del área común: ")
            fecha = input("Ingrese la fecha de la reserva (YYYY-MM-DD): ")
            hora_inicio = input("Ingrese la hora de inicio (HH:MM): ")
            hora_fin = input("Ingrese la hora de finalización (HH:MM): ")
            gestor.agregar_reserva(nombre_residente, nombre_area, fecha, hora_inicio, hora_fin)
        elif opcion == "3":
            gestor.mostrar_info_unidad_residencial()
        elif opcion == "4":
            gestor.mostrar_info_areas_comunes()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

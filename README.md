**Daniel Fuentes Vargas**

**UPB**

**Actividad Evaluativa 20-09-23**

**Problemática: Gestión de Reservas de Áreas Comunes en la Unidad Residencial Zanetti**

**Diagrama UML**

<img width="805" alt="CleanShot 2023-09-05 at 16 55 13@2x" src="https://github.com/upb-danielfuentes/df-crud-zanetti/assets/141572206/fb397c24-37bb-48c7-bcae-6b86cb8f7cb4">


**Descripción del Problema:**
En la unidad residencial Zanetti se cuenta con varias áreas comunes, como salones de eventos, piscinas, canchas deportivas, etc., que los residentes pueden reservar para su uso. Actualmente, la gestión de estas reservas se lleva a cabo de manera manual, lo que genera ineficiencias, confusiones y conflictos de programación.

**Necesidad Tecnológica:**
Se requiere desarrollar un sistema de información que automatice y simplifique la gestión de reservas de áreas comunes en la unidad residencial. Este sistema debe permitir a los residentes:

1. **Crear Reservas:** Los residentes deben poder solicitar y crear reservas para las áreas comunes disponibles en fechas y horarios específicos.

2. **Consultar Reservas:** Debe ser posible consultar las reservas existentes para cada área común en cualquier momento.

3. **Actualizar Reservas:** Los residentes deben poder modificar o cancelar sus reservas existentes si surgen cambios en sus planes.

4. **Eliminar Reservas:** El sistema debe permitir la eliminación de reservas en caso de ser necesario.

**Solución Propuesta:**
Desarrollar una aplicación de gestión de reservas utilizando Python y programación orientada a objetos (POO) con un CRUD. La aplicación consistirá en las siguientes clases:

- **Clase Reserva:** Representa una reserva de área común con atributos como nombre del residente, área común, fecha, hora de inicio y hora de finalización.

- **Clase Área Común:** Representa una área común con atributos como nombre, capacidad, horario de disponibilidad y lista de reservas.

- **Clase Unidad Residencial:** Representa la unidad residencial y contiene una lista de todas las áreas comunes disponibles.

- **Funciones CRUD:** Se implementarán funciones para crear, leer, actualizar y eliminar reservas y áreas comunes.

Esta solución permitirá a la unidad residencial gestionar de manera eficiente las reservas de sus áreas comunes, evitando conflictos y mejorando la satisfacción de los residentes.


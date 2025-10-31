"""9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permití consultar qué actividad hay en cierto día y hora."""

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "12:00"): "Clase de inglés",
    ("miercoles", "12:30"): "Reunión semanal",
    ("jueves", "13:00"): "Almuerzo con el equipo",
    ("viernes", "16:00"): "Reunión con el cliente",
}

while True:
    print("Horarios cargados:")
    for (dia, hora), evento in agenda.items():
        print(f"  - {dia.capitalize()} a las {hora}.")

    dia_consulta = input("Ingrese un día para ver su agenda (o salir para terminar): ")

    if dia_consulta.lower() == 'salir':
        print("¡Hasta luego!")
        break
    
    hora_consulta = input(f"Ingrese la HORA para el {dia_consulta} (ej: 10:00): ")
    clave_consulta = (dia_consulta.lower(), hora_consulta)

    if clave_consulta in agenda:
        evento_encontrado = agenda[clave_consulta]
        print(f"La agenda para los días {dia_consulta} y hora {hora_consulta} es: {evento_encontrado}")
    else:
        print("No hay ningún evento programado en ese día y hora exactos.")
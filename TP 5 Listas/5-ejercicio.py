"""5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
• Mostrar la lista final actualizada."""

estudiantes = ["Emiliano", "Ariadna", "Javier", "Micaela", "Brenda", "Luis", "Carolina", "Flor"]

print("Lista de estudiantes original: ", estudiantes)

usuarioOpcion = input("¿Quieres agregar (escribir: a) o eliminar un estudiante? (escribir: b) ").lower()

if usuarioOpcion == 'a':
    nuevoEstudiante = input("Ingresa el nombre del nuevo estudiante: ")
    estudiantes.append(nuevoEstudiante)
    print("Estudiante agregado con éxito!")
elif usuarioOpcion == 'b':
    eliminarEstudiante = input("Ingresa el nombre del estudiante a eliminar: ")
    if eliminarEstudiante in estudiantes:
        estudiantes.remove(eliminarEstudiante)
        print("Estudiante eliminado con éxito!")
    else:
        print("El estudiante seleccionado no se encuentra en la lista")
else:
    print("Opción no válida, por favor ingrese: a o b")

print("Lista final de estudiantes: ", estudiantes)
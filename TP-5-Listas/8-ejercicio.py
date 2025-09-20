"""8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
• Mostrar el promedio de cada estudiante.
• Mostrar el promedio de cada materia."""

#cada fila es un estudiante y las 3 columnas son las notas
notas = [
    [8, 7, 7],
    [6, 7, 8],
    [9, 8, 8],
    [7, 5, 6],
    [10, 9, 8]
]

numEstudiantes = len(notas)
numMaterias = len(notas[0])

for i in range(numEstudiantes):
    promedioEst = sum(notas[i])/numMaterias
    print(f"Promedio de cada estudiante: Estudiante {i + 1}: {promedioEst:.2f}")

for j in range(numMaterias):
    sumaMaterias = 0
    for i in range(numEstudiantes):
        sumaMaterias += notas[i][j]
    promedioMateria = sumaMaterias/numEstudiantes
    print(f"Promedio de cada materia: materia {j + 1} promedio de: {promedioMateria:.2f}")


"""1) Crear una lista con las notas de 10 estudiantes.
• Mostrar la lista completa.
• Calcular y mostrar el promedio.
• Indicar la nota más alta y la más baja."""

notas = [8,7,6,10,4,5,7,7,9,5]
cantidad = len(notas)
suma_total = 0
promedio = 0
nota_alta = max(notas)
nota_baja = min(notas)
for numero in notas:
    suma_total += numero  # Es lo mismo que suma_total = suma_total + numero
    promedio = suma_total/cantidad
print(f"Las notas de los estudiantes eran {notas}, el promedio fue de {promedio}. La nota más alta fue de {nota_alta} y la más baja de {nota_baja}.")
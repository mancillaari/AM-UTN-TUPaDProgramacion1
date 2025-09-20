"""4) Dada una lista con valores repetidos:
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
• Crear una nueva lista sin elementos repetidos.
• Mostrar el resultado."""

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

sinDuplicados = []
for elemtentos in datos:
    if elemtentos not in sinDuplicados:
        sinDuplicados.append(elemtentos)

print("Lista de elementos sin duplicados: ", sinDuplicados)


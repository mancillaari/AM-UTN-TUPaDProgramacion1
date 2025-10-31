"""3) Generar una lista con 15 números enteros al azar entre 1 y 100.
• Crear una lista con los pares y otra con los impares.
• Mostrar cuántos números tiene cada lista."""

import random 

lista_numeros = 15
min_num = 1
max_num = 100
numeros_aleatorios = [random.randint(min_num, max_num) for _ in range(lista_numeros)]
print(f"Los números generados son: {numeros_aleatorios}.")

pares_list = []
impares_list = []

for numero in numeros_aleatorios:
    if numero%2 == 0:
        pares_list.append(numero)
    else:
        impares_list.append(numero)
print(f"La lista números pares: {len(pares_list)}. La lista de números impares es: {len(impares_list)}.")
#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

numero_entero = int(input("Por favor, ingrese un número entero: "))
numero_original = numero_entero
contador = 0

if numero_entero == 0:
    cantidad_digitos = 1
else:
    if numero_entero < 0:
        numero_entero = -numero_entero
    
    cantidad_digitos = 0
    while numero_entero > 0:
        numero_entero = numero_entero // 10
        cantidad_digitos += 1

print(f"El número {numero_original} tiene {cantidad_digitos} de dígitos.")
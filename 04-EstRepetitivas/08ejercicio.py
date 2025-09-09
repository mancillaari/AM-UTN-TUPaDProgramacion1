# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, 
# cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, 
# pero debe estar preparado para procesar 100 números con un solo cambio).

cantidad_numeros = 100
pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Por favor, ingrese {cantidad_numeros} números enteros.")

for i in range(cantidad_numeros):
    num = int(input(f"Número {i + 1}: "))

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\n--- Resultados del análisis ---")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")
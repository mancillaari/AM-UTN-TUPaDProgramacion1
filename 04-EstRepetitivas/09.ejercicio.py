# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa 
# con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

total_numeros = 5

suma_total = 0

print(f"Por favor, ingrese {total_numeros} números para calcular su media.")

for i in range(total_numeros):
    num = int(input(f"Número {i + 1}: "))
    suma_total += num

media = suma_total / total_numeros

print(f"La media de los {total_numeros} números ingresados es: {media}")
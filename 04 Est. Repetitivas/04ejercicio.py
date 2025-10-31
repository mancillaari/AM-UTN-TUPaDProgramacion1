#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

numero_user = int(input("Por favor, ingrese un número entero (o 0 para terminar): "))
sumatoria = 0

while numero_user != 0:
    numero_user = int(input("Por favor, ingrese otro número entero: "))
    sumatoria += numero_user
print("La suma total de los números es",sumatoria)
"""1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial 
de todos los números enteros entre 1 y el número que indique el usuario."""

def factorial(num):
    return 1 if num == 0 else num * factorial(num - 1)

num_user = int(input("Por favor, ingresa un número a calcular el factorial: "))

print(f"El factorial del número {num_user} es: {factorial(num_user)}")


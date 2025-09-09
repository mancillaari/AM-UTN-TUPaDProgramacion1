#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
num_user = int(input("Por favor, ingresa un número entre 0 y 9: "))
numero_random = random.randint(0,9)
contador_intentos = 0

if num_user % 2 != 0:
    print("Por favor, ingresar un número entre 0 y 9.")
else: 
    while numero_random != num_user:
        num_user = int(input("Por favor, ingresa otro número: "))
        contador_intentos += 1
print(f"El número random a adivinar era {numero_random} y los intentos fueron de {contador_intentos}")

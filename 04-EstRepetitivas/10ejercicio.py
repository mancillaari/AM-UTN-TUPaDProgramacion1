# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingrese un número para invertir sus dígitos: "))
numero_original = numero
numero_invertido = 0

signo = 1
if numero < 0:
    signo = -1
    numero = -numero

while numero > 0:
    ultimo_digito = numero % 10

    numero_invertido = (numero_invertido * 10) + ultimo_digito

    numero = numero // 10

numero_invertido = numero_invertido * signo

print(f"El número {numero_original} invertido es: {numero_invertido}")
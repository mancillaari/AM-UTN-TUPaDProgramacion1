#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

valor_uno = int(input("Por favor, ingrese el primer valor: "))
valor_dos = int(input("Por favor, ingrese el segundo valor: "))

suma = 0

if valor_uno>=valor_dos:
    print("El primer número debe ser menor que el segundo.")
else:
    suma = sum(range(valor_uno + 1, valor_dos))
    print(f"La suma de los números entre {valor_uno} y {valor_dos} excluyendolos es {suma}")
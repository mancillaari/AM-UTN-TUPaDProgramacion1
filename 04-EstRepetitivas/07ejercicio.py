#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

numero_limite = int(input("Ingrese un número entero positivo: "))
resultado_suma = 0

if numero_limite < 0:
        print("Por favor, el número debe ser positivo.")
else:
    resultado_suma = sum(range(numero_limite + 1))
    print(f"La suma de todos los números desde 0 hasta {numero_limite} es: {resultado_suma}")
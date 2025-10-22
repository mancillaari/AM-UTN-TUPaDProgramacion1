"""7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara."""

def operaciones_basicas(a, b):
    print(f"--- Suma, resta, multiplicación y división de los números {a, b} ---")
    resultado_suma = a + b
    print(f"{a} + {b} = {resultado_suma}")
    resultado_resta = a - b
    print(f"{a} - {b} = {resultado_resta}")
    resultado_multi = a * b
    print(f"{a} * {b} = {resultado_multi}")
    resultado_div = a // b
    print(f"{a} / {b} = {resultado_div}")


a_usuario = int(input("Por favor, ingrese el primer número: "))
b_usuario = int(input("Por favor, ingrese el primer número: "))
operaciones_basicas(a_usuario, b_usuario)
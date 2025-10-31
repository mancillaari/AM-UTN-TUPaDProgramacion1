"""10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta función."""

def calcular_promedio(a, b, c):
    promedio_suma = (a + b +c)
    promedio = promedio_suma // 3
    print(f"El promedio de las notas {a}, {b} y {c} es {promedio}")

nota_uno_usuario = int(input("Por favor, ingrese la primera nota: "))
nota_dos_usuario = int(input("Por favor, ingrese la segunda nota: "))
nota_tres_usuario = int(input("Por favor, ingrese la tercera nota: "))
calcular_promedio(nota_uno_usuario, nota_dos_usuario, nota_tres_usuario)
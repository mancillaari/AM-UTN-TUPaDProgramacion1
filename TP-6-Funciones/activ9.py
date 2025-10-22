"""9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función."""

def celsius_a_fahrenheit(celsius):
    if celsius == 0:
        return 0

    grados_Fahren = (celsius*9/5) + 32
    print(f"Los grados celsius ingresados: {celsius} son {grados_Fahren} en grados Fahrenheit.")

celsius_usuario = float(input("Por favor, ingrese la temperatura en grados Celsius: "))
celsius_a_fahrenheit(celsius_usuario)
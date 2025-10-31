"""4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados."""

import math

def calcular_area_circulo(radio):
    areaCirculo = math.pi*(radio**2)
    return areaCirculo
    
def calcular_perimetro_circulo(radio):
    perimetroCirculo = 2*math.pi*radio
    return perimetroCirculo

radio_num = float(input("Por favor, ingresar el radio del círculo: "))
print(f"El área del círculo es {calcular_area_circulo(radio_num)} y el perímetro es {calcular_perimetro_circulo(radio_num)}")
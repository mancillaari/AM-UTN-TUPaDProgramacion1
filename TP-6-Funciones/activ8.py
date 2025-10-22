"""8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales."""

def calcular_imc(peso, altura):
    if altura == 0:
        return 0
    
    masaCorporal = peso/(altura**2)
    return masaCorporal

kilo_usuario = float(input("Por favor, ingrese el peso en kilogramos: "))
altura_usuario = float(input("Por favor, ingrese la altura en metros: "))

resultado_imc = calcular_imc(kilo_usuario, altura_usuario)
print(f"Su Índice de Masa Corporal (IMC) es: {resultado_imc:.2f}")
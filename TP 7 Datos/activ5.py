"""5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra."""

from collections import Counter

datos_usuario = input("Por favor, ingrese una frase: ")

lista_usuario = datos_usuario.split(' ')

datos_limpios_usuario = set(lista_usuario)

recuento_datos = Counter(lista_usuario)
print(f"La frase ingresa sin repetidos es: {datos_limpios_usuario} y la cantidad de veces que aparece cada palabra es {recuento_datos}.")
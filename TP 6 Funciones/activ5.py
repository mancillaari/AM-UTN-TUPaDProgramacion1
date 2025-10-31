"""5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función."""

def segundos_a_horas(segundos):
    segundos_equivalente = 3600
    horas = segundos/segundos_equivalente
    return horas

segundos = float(input("Por favor, ingresar la cantidad de segundos: "))
print(f"Los segundos {segundos} equivalen a {segundos_a_horas(segundos)} horas.")
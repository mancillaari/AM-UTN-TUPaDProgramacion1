"""6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno."""

promedios_alumnos = {}
print("--- Ingreso de Notas (3 Alumnos) ---")

for i in range(3):

    nombre_usuario = input(f"Ingresa el nombre del alumno {i+1}: ")
    notas_input = input(f"Ingresa las 3 notas de {nombre_usuario} (separadas por coma): ")

    try:
        notas_lista_str = notas_input.split(',')
        
        notas_numeros = [float(nota.strip()) for nota in notas_lista_str]
        if len(notas_numeros) != 3:
            print("Error: Debes ingresar exactamente 3 notas. Se guardará promedio 0.")
            promedio = 0.0
        else:
            notas_tupla = tuple(notas_numeros)
            promedio = sum(notas_tupla) / len(notas_tupla)
    except ValueError:
        print("Error al ingresar las notas. Asegúrate de usar números. Se guardará promedio 0.")
        promedio = 0.0
    promedios_alumnos[nombre_usuario] = promedio

print("\n--- Promedios Finales ---")
for nombre_usuario, promedio in promedios_alumnos.items():
    print(f"El promedio de {nombre_usuario} es: {promedio:.2f}")
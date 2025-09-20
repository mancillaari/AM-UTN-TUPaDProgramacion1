"""7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
semana.
• Calcular el promedio de las mínimas y el de las máximas.
• Mostrar en qué día se registró la mayor amplitud térmica."""

# Mínima, máxima

temperaturas = [
    [12, 20], #día 1
    [10, 22], #2
    [9, 17],  #3
    [10, 26], #4
    [8, 18],  #5
    [14, 24], #6
    [10, 20], #7
]

sumaMin = 0
sumaMax = 0
for dia in temperaturas:
    sumaMin += dia[0] #sumaMin = sumaMin + dia
    sumaMax += dia[1]
promedioMin = sumaMin/len(temperaturas)
promedioMax = sumaMax/len(temperaturas)

print(f"Promedio de las temperaturas mínimas es: {promedioMin:.2f}C")
print(f"Promedio de las temperaturas máximas es: {promedioMax:.2f}C")

amplitudMax = 0
diaAmplitudMax = 0

for i in range(len(temperaturas)):
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    if amplitud > amplitudMax:
        amplitudMax = amplitud
        diaAmplitudMax = i + 1

print(f"La mayor amplitud térmica fue el día {diaAmplitudMax} con amplitud de {amplitudMax}C")
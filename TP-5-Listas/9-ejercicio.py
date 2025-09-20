"""9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
• Inicializarlo con guiones "-" representando casillas vacías.
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
• Mostrar el tablero después de cada jugada."""

tablero = [["-","-","-"],
           ["-","-","-"],
           ["-","-","-"]]

jugadorActual = "X"
jugadas = 0

while jugadas < 9:
    for fila in tablero:
        print(" | ".join(fila))
        print("---------")
    
    print(f"Turno del jugador {jugadorActual}")

    posicionValida = False
    while not posicionValida:
        filaString = input("Ingresa la fila (0, 1, 2): ")
        columnaString = input("Ingresa la columna (0, 1, 2): ")

        if filaString.isdigit() and columnaString.isdigit():
            fila = int(filaString)
            columna = int(columnaString)

            if 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == "-":
                tablero[fila][columna] = jugadorActual
                jugadas += 1
                posicionValida = True
            else:
                print("Posición inválida o ya ocupada. Intente de nuevo.")
        else:
            print("Entrada no válida. Por favor, ingrese un número.")

    if jugadorActual == "X":
        jugadorActual = "O"
    else: 
        jugadorActual = "X"

for fila in tablero:
    print(" | ".join(fila))
    print("---------")

print("Juego terminado!")
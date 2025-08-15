#Actividades "Trabajo practico 1: Estructuras secuenciales"+

#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.

"""name = input("Por favor, ingrese su nombre:")
#print("Hola,",name)"""

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.

"""nombre = input("Por favor, ingrese su nombre:")
apellido = input("Por favor, ingrese su apellido:")
edad = input("Por favor, ingrese su edad:")
lugarResidencia = input("Por favor, ingrese su lugar de residencia:")
print(f"Hola! Soy {nombre} {apellido}. Tengo {edad} años y vivo en {lugarResidencia}.")"""

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro

"""piValor = 3.1416
radio=int(input("Por favor, ingresar el radio del círculo: "))
areaCirculo = float(piValor)*(radio**2)
perimetroCirculo = 2*piValor*radio
print(f"El área del círculo es {areaCirculo} y el perímetro es {perimetroCirculo}")"""

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

"""cantSegundos = float(input("Por favor, ingresar cantidad de segundos: "))
secsEquivalente = 3600
cantHoras = cantSegundos/secsEquivalente
print(f"Los segundos ingresados {cantSegundos} equivalen a {cantHoras} horas")"""

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

"""numUsuario = int(input("Por favor, ingrese un número entero: "))
for i in range (1,11):
    resultado = numUsuario * i
    print(f"La tabla de multiplicar es: {numUsuario} por {i} es igual a {resultado}")"""

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

"""primerNum = int(input("Por favor, ingrese un número entero: "))
segundoNum = int(input("Por favor, ingrese un segundo número entero: "))

suma=(primerNum+segundoNum)
resta=(primerNum-segundoNum)
multi=(primerNum*segundoNum)
divi=(primerNum//segundoNum)

print(f"La suma de {primerNum} y {segundoNum} es {suma}")
print(f"La resta de {primerNum} y {segundoNum} es {resta}")
print(f"La multiplicación de {primerNum} y {segundoNum} es {multi}")
print(f"La división de {primerNum} y {segundoNum} es {divi}")"""

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

"""alturaUsuario = float(input("Por favor, ingrese su altura: "))
pesoUsuario = float(input("Por favor, ingrese su peso: "))
masaCorporal = pesoUsuario/(alturaUsuario**2)

print(f"Su masa corporal es: {masaCorporal}")"""

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

"""gradosCelsius = float(input("Por favor, ingrese la temperatura en grados Celsius: "))
gradosFahren = (gradosCelsius*9/5) + 32

print(f"La temperatura {gradosCelsius} en Celsius es {gradosFahren} es grados Fahrenheit")"""

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

"""primerNum = float(input("Por favor, ingrese un número: "))
segundoNum = float(input("Por favor, ingrese el segundo número: "))
tercerNum = float(input("Por favor, ingrese el tercer número: "))

promedio=(primerNum+segundoNum+tercerNum)/3

print(f"El promedio de los números ingresados: {primerNum}, {segundoNum} y {tercerNum} dan el promedio de: {promedio}")"""
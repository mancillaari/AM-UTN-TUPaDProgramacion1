"""1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”."""

edad_minima = 18
edad = int(input("Ingrese su edad: "))

if edad >= edad_minima:
    print("Es mayor de edad")

"""2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”

nota_alumno = int(input("Por favor, ingresar nota: "))

if nota_alumno >= 6:
    print("Aprobado")
else: print("Desaprobado")"""

"""3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par".

num_user = int(input("Por favor, ingrese un número: "))
if num_user % 2 == 0:
    print("Ha ingresado un número par")
else: print("Por favor, ingresar un número par")"""

"""4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años

edad_user = int(input("Por favor, ingrese su edad: "))
if edad_user < 12:
    print("Su edad pertenece a la categoría: Niño")
elif edad_user>=12 and edad_user <18:
    print ("Su edad pertenece a la categoría: Adolescente")
elif edad_user>=18 and edad_user <30:
    print("Su edad pertenece a la categoría: Adulto joven")
else: 
    print("Su edad pertenece a la categoría: Adulto")"""

"""5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, 
imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 

password_user = input("Por favor, ingrese su contraseña: ")
if len(password_user) >= 8 and len(password_user) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")"""

""""6) escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. 
Imprimir el resultado por pantalla. Definir la lista numeros_aleatorios de la siguiente forma: "import random numeros_aleatorios = [random.randint(1,100) for i in range (50)]". 

import statistics
from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1,100) for i in range (50)]

media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)

#Comparar variables para determinar los sesgos: 

if media > mediana and mediana > moda:
    print("El sesgo es: positivo.")
elif media < mediana and mediana < moda: print ("El sesgo es: negativo.")
elif media == mediana == moda:
    print("No hay sesgo.")
else:
    print("No cumple con ninguna de las tres condiciones.")"""

"""7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string 
resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

palabra_user = input("Por favor, ingresar una palabra:")
ultima_letra = palabra_user[-1].lower()
vocales = "aeiou"

if ultima_letra in vocales:
    print(palabra_user + "!")
else:
    print("La última letra es una consonante.")"""

"""8)  Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla.

nombre_user = input("Por favor, ingrese su nombre: ")
opcion_user = int(input("Por favor, seleccione la opción 1 para mayusculas, 2 para minusculas y 3 para capitalizar: "))

if opcion_user == 1: 
    print(f"Su opción fue la 1: {nombre_user.upper()}")
elif opcion_user == 2: print(f"Su opción fue la 2: {nombre_user.lower()}")
elif opcion_user == 3: print(f"Su opción fue la 3: {nombre_user.title()}")
else: print("La opción elegida no es correcta.")"""

"""9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e 
imprima el resultado por pantalla: ● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
terremoto = int(input("Por favor, ingrese la magnitud del terremoto: "))
if terremoto < 3:
    print("El terremoto es de la categoría: Muy leve.")
elif terremoto >= 3 and terremoto<4:
    print ("El terremoto es de la categoría: Leve.")
elif terremoto >= 4 and terremoto<5:
    print("El terremoto es de la categoría: Moderado.")
elif terremoto >= 5 and terremoto<6:
    print("El terremoto es de la categoría: Fuerte.")
elif terremoto >= 6 and terremoto<7:
    print("El terremoto es de la categoría: Muy fuerte.")
else: 
    print("El terremoto es de la categoría: Extremo.")"""

"""10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información 
para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Por favor, ingresar el hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes en números (1-12): "))
dia = int(input("Ingrese el día: "))

fecha_user = (mes, dia)

if hemisferio == "N":
    if (3,21) <= fecha_user <= (6,20):
        estacion = "Primavera"
    elif (6,21) <= fecha_user <= (9,22):
        estacion = "Verano"
    elif (9,23) <= fecha_user <= (12,20):
        estacion = "Otoño"
    else:
        estacion = "Invierno"

elif hemisferio == "S":
    if (9,21) <= fecha_user <= (12,20):
        estacion = "Primavera"
    elif (12,21) <= fecha_user or fecha_user <= (3,20):
        estacion = "Verano"
    elif (3,21) <= fecha_user <= (6,20):
        estacion = "Otoño"
    else:
        estacion = "Invierno"
else:
    estacion = "Hemisferio no válido."

print("Estación:", estacion)"""
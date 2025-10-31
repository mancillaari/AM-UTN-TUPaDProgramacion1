"""3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: 
“Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
Pedir los datos al usuario y llamar a esta función con los valores ingresados."""

def informacion_personal(nombre, apellido, edad, residencia):
    info_usuario = f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."
    print(info_usuario)

nombre = input("Por favor, ingresa tu nombre: ")
apellido = input("Por favor, ingresa tu apellido: ")
while True: 
    edad_ingreso = input("Por favor, ingresa tu edad: ")
    if edad_ingreso.isdigit():
            edad = edad_ingreso
            break
    else:
         print("Por favor, ingrese un número entero.")
    
residencia = input("Por favor, ingresa tu lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)
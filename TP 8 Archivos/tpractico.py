"""1. Crear archivo inicial con productos: Crear un archivo de texto llamado
productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad"""

import os

productos = [
    "Nombre,Precio,Cantidad\n",
    "Cuaderno,17.50,7\n",
    "Regla,6.0,12\n",
    "Tijera,12.0,8\n"
]

with open("productos.txt", "w") as archivo:
    archivo.writelines(productos)

"""2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30"""

with open("productos.txt", "w") as archivo:
    archivo.writelines(productos)

def imprimir_productos(lista_de_productos):
    print("\n--- Contenido Actual de Productos ---")
    if not lista_de_productos:
        print("No hay productos cargados.")
    else:
        for producto in lista_de_productos:
            print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")

"""3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos, le pida 
al usuario que ingrese un nuevo producto (nombre, precio,cantidad) y lo agregue al archivo sin borrar el contenido existente."""

def agregar_producto(lista_de_productos):
    print("\n--- Agregar Nuevo Producto ---")

    while True:
        nombre = input("Ingrese el nombre del producto: ")
        if nombre and not nombre.isdigit():
            break 
        else:
            print("Por favor ingrese un nombre que contenga letras.")
    
    while True:
        precio_str = input("Ingrese el precio: ")

        if precio_str and precio_str.replace('.', '', 1).isdigit():
            precio = float(precio_str)
            break
        else:
            print("Error: Ingrese un precio válido (ej: 17.50)")

    while True:
        cantidad_str = input("Ingrese la cantidad: ")
        
        if cantidad_str and cantidad_str.isdigit():
            cantidad = int(cantidad_str)
            break
        else:
            print("Error: Ingrese una cantidad válida (ej: 7)")

    nuevo_dic = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    
    lista_de_productos.append(nuevo_dic)
    print("¡Producto agregado a la lista!")
    return lista_de_productos

                
"""4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad."""

def cargar_productos():
    productos_dic = []

    if not os.path.exists("productos.txt"):
        print("Aviso: El archivo 'productos.txt' no existe. Se creará uno nuevo al guardar.")
        return productos_dic
    
    with open("productos.txt", "r") as archivo:
        archivo.readline()

        for linea in archivo:
            partes = linea.strip().split(',')

            if len(partes) == 3:

                catalogo_dic = {
                    "nombre": partes[0],
                    "precio": float(partes[1]),
                    "cantidad": int(partes[2])
                }
                
                productos_dic.append(catalogo_dic)
    
    return productos_dic

"""5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. 
Si no existe, mostrar un mensaje de error."""

def buscar_producto(lista_de_productos):
    if not lista_de_productos:
        print("\nNo hay productos cargados para buscar.")
        return

    nombre_buscado = input("Por favor, ingrese el nombre del producto que necesita: ")

    encontrado = False
    for producto in lista_de_productos:

        if producto["nombre"].lower() == nombre_buscado.lower():
            print("\n--- Producto Encontrado ---")
            print(f"Nombre:   {producto['nombre']}")
            print(f"Precio:   ${producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}")
            encontrado = True
            break

    if not encontrado:
        print(f"\nNo hemos encontrado '{nombre_buscado}' en nuestro catálogo.")


"""6. Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, sobrescribir el archivo productos.txt 
escribiendo nuevamente todos los productos actualizados desde la lista."""

def guardar_productos(lista_de_productos):
    print("\n--- Guardando productos en el archivo... ---")
    with open("productos.txt", "w") as archivo:
        
        archivo.write("Nombre,Precio,Cantidad\n")

        for producto in lista_de_productos:

            linea_formateada = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"

            archivo.write(linea_formateada)
            
    print("¡Datos guardados con éxito!")

def main():
    mis_productos = cargar_productos()
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Mostrar todos los productos")
        print("2. Agregar nuevo producto (guarda automáticamente)")
        print("3. Buscar producto por nombre")
        print("0. Salir (y guardar cambios)")
        
        opcion = input("Elija una opción: ")
        
        if opcion == '1':
            imprimir_productos(mis_productos)
            
        elif opcion == '2':
            mis_productos = agregar_producto(mis_productos)
            guardar_productos(mis_productos)
            print("¡Producto guardado en el archivo productos.txt!")
            
        elif opcion == '3':
            buscar_producto(mis_productos)
            
        elif opcion == '0':
            guardar_productos(mis_productos)
            print("Cambios guardados. ¡Adiós!")
            break
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
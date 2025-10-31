"""8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe."""

stock = {"Heladera": 18, "Freidora": 12, "Lavarropa": 8}

while True: 
    print(f"----Lista de stock {stock.keys()}----")
    producto = input("Ingrese el nombre del producto a gestionar (o 'salir' para terminar): ")

    if producto.lower() == 'salir':
        print("¡Hasta luego!")
        break
    
    if producto in stock:
        # --- CASO 1: El producto YA existe ---
        print(f"El producto '{producto}' existe.")
        
        accion = input("¿Desea Agregar unidades (A) o Consultar (C)?: ").lower()

        if accion == 'a':
            print(f"Stock actual: {stock[producto]} unidades.")
            try: 
                cantidad = int(input(f"¿Cuántas unidades de '{producto}' desea agregar?: "))
                stock[producto] += cantidad  # Forma corta de: stock[producto] = stock[producto] + cantidad
                print(f"¡Stock actualizado! '{producto}' ahora tiene {stock[producto]} unidades.")
            except ValueError:
                print("Error: Debe ingresar un número.")
        
        elif accion == 'c':
            print(f"Stock actual: {stock[producto]} unidades.")
        else:
            print("Acción no reconocida.")
        
    else: 
        print(f"El producto '{producto}' es nuevo.")
        
        accion = input("¿Desea agregarlo al inventario? Escriba S para 'Si' o N para 'No': ").lower()
        
        if accion == 's':
            try:
                cantidad = int(input(f"Ingrese el stock inicial para '{producto}': "))
                stock[producto] = cantidad
                print(f"¡Producto agregado! '{producto}' registrado con {cantidad} unidades.")
            
            except ValueError:
                print("Error: Debe ingresar un número.")
        else:
            print("Producto no agregado. Volviendo al menú...")




"""2) Pedir al usuario que cargue 5 productos en una lista.
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
• Preguntar al usuario qué producto desea eliminar y actualizar la lista."""

productos_lista = []
usuario_productos = input("Por favor, ingrese 5 productos: ")
productos_lista = [producto.strip() for producto in usuario_productos.split(",")]
print(f"La lista original de los productos es: {productos_lista}")

productos_ordenados = sorted(productos_lista, key=str.lower)
print(f"La lista de los productos ordenados álfabeticamente es: {productos_ordenados}")


producto_a_eliminar = input("¿Qué producto deseas eliminar de la lista? ")
if producto_a_eliminar in productos_lista:
    productos_lista.remove(producto_a_eliminar)
    print(f"La lista actualizada es: {productos_lista}")
else:
    print(f"'{producto_a_eliminar}' no se encontró en la lista.")
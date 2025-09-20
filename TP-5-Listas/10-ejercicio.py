"""10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
• Mostrar el total vendido por cada producto.
• Mostrar el día con mayores ventas totales.
• Indicar cuál fue el producto más vendido en la semana."""

#cada fila es un producto y las columnas son los 7: por ejemplo: 10 + 5 + 25 + 14 = 54

ventas = [
    [10, 15, 12, 18, 20, 15, 13],
    [5, 9, 1, 14, 7, 15, 11],
    [25, 15, 30, 20, 18, 14, 10],
    [14, 16, 22, 19, 20, 19, 10]
]

numProductos = len(ventas)
numDias = len(ventas[0])

for i in range(numProductos):
    totalProducto = sum(ventas[i])
    print(f"Total vendido de cada producto: producto {i + 1}: {totalProducto}")

ventasPerDia = []

for j in range(numDias):
    sumaDias = 0
    for i in range(numProductos):
        sumaDias += ventas[i][j]
    ventasPerDia.append(sumaDias)

diaMayorVenta = ventasPerDia.index(max(ventasPerDia)) + 1
print(f"El día con mayores ventas fue el dia {diaMayorVenta} con {max(ventasPerDia)} unidades.")

ventasPerProducto = []

for i in range(numProductos):
    ventasPerProducto.append(sum(ventas[i]))

productoVendido = ventasPerProducto.index(max(ventasPerProducto)) + 1
print(f"El producto más vendido en la semana fue el producto {productoVendido} con {max(ventasPerProducto)} unidades.")
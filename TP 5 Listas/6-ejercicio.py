"""6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
último pasa a ser el primero)."""

listaNum = [3, 6, 1, 9, 6, 2, 8]
print("Lista original de números: ", listaNum)

ultimoNum = listaNum.pop()
listaNum.insert(0, ultimoNum)

print("Lista con los elementos rotados hacia la derecha: ", listaNum)
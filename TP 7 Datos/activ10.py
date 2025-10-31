"""10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores."""

paises = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Uruguay": "Montevideo", "Brasil": "Brazilia"}

invertido = {valor: clave for clave, valor in paises.items()}
invertido_mayus = {k.capitalize(): v.capitalize() for k,v in invertido.items()}
print("Las capitales con sus países son:")
print('\n'.join("{}: {}".format(k, v) for k, v in invertido_mayus.items()))

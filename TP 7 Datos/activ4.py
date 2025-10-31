"""4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe."""

contactos = {"Emiliano": 1130035407, "Agustina": 1192641473, "Mecio": 1113598758}

print(contactos.keys())

eleccion_usuario = input("Por favor, introducir un nombre para conocer su contacto: ")
print(contactos[eleccion_usuario])
"""3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 
n(𝑚) = n * n(𝑚-1)
Prueba esta función en un algoritmo general."""

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base_user = int(input("Por favor, ingresa el número base: "))
exponente_user = int(input("Por favor, ingresa el exponente: "))
print(f"El resultado de {base_user} elevado a {exponente_user} es: {potencia(base_user, exponente_user)}")
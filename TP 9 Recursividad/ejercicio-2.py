"""2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta 
la posición que el usuario especifique."""

def fibonacci(num):
  return 1 if num <= 1 else fibonacci(num - 1) + fibonacci(num - 2)

fib_user = int(input("Por favor, ingresa un número para calcular su valor de la serie de Fibonacci: "))
print(f"El valor de la serie de Fibonacci para el número {fib_user} es: {fibonacci(fib_user)}")
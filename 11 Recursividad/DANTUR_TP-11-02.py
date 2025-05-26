# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
cantidad = int(input("Ingrese un número: "))

print(f"Serie de Fibonacci hasta la posición {cantidad}:")
for i in range(cantidad):
    print(f"{fibonacci(i)}", end=", ")
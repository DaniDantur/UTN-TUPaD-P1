# Ejercicio 5
# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
intentos = 0
numero_aleatorio = random.randint(0, 9)
numero_usuario = -99

print("Adiviná el número entre 0 y 9:")

while numero_usuario != numero_aleatorio:
    numero_usuario = int(input("Ingresá tu número: "))
    intentos += 1
    if numero_usuario != numero_aleatorio:
        print("Número incorrecto. Probá de nuevo.")
    else:
        print(f"Adivinaste el número {numero_aleatorio} en {intentos} intentos.")
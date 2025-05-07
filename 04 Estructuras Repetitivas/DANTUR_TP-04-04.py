# Ejercicio 4
# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

suma = 0

while True:
    numero = int(input("Ingrese un número entero (0 para salir): "))
    if numero == 0:
        break
    suma += numero

print(f"La suma total acumulada es: {suma}")
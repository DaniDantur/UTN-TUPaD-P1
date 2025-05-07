# Ejercicio 2
# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = int(input("Ingrese un número entero: "))
cantidad_digitos = 0

if numero == 0:
    cantidad_digitos = 1
else:
    while numero != 0 and numero != -1:
        numero //= 10
        cantidad_digitos += 1
        
print(f"La cantidad de dígitos es: {cantidad_digitos}")

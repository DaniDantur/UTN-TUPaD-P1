# Ejercicio 9
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

cantidad_numeros = 10
media = 0

for i in range(0,cantidad_numeros):
    numero = int(input("Ingres un número entero: "))
    media += numero

media /= cantidad_numeros

print(f"La media es: {media}")
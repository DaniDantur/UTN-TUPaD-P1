# Ejercicio 8
# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio

cantidad_numeros = 100
pares = 0
impares = 0
negativos = 0
positivos = 0

for i in range(0,cantidad_numeros):
    numero = int(input("Ingrese un número entero: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números negativos: {negativos}")
print(f"Números positivos: {positivos}")
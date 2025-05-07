# Ejercicio 7
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

limite = int(input("Ingrese un número: "))
suma = 0

for i in range(1,limite):
    suma += i

print(f"La suma total es {suma}.")
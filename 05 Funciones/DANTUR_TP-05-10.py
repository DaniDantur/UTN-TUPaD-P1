def calcular_promedio(a, b, c):
    return (a + b + c) / 3

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))
promedio = calcular_promedio(numero1, numero2, numero3)
print(f"El promedio de los tres números es: {promedio:.2f}")

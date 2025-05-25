def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperatura_celsius = float(input("Ingrese la temperatura en Celsius: "))
print(f"{temperatura_celsius}°C son {celsius_a_fahrenheit(temperatura_celsius)}°F.")

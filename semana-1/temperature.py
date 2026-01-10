"""
Convierte grados Celsius a Fahrenheitcel

"""
celsius: float = float(input("Ingresa la temperatura en Celsius: "))
fahrenheit: float = (celsius * 9/5) + 32

print(f"{celsius} °C equivalen a {fahrenheit:.2f} °F")

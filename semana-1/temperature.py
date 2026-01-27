"""
Convierte grados Celsius a Fahrenheitcel

"""
# Solicita al usuario el ingreso de dato por teclado.
celsius: float = float(input("Ingresa la temperatura en Celsius: "))

# Formula.
fahrenheit: float = (celsius * 9/5) + 32

# Mostramos por pantalla el resultado.
print(f"{celsius} °C equivalen a {fahrenheit:.2f} °F")

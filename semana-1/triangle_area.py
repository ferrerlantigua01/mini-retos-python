"""
Realice un algoritmo que calcule el área de un triangulo.
"""

# Solicita al usuario la base y altura por teclado.
base: int = int(input("Ingresa la base del triangulo: "))
height: int = int(input("Ingresa la altura del triangulo: "))

# formula
triangle_area: float = (base * height) /2

# Mostrando por pantalla
print(f"El área del triangulo es: {triangle_area}")
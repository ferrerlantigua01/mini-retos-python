"""
Realice un algoritmo que calcule el área de la circunferencia.
"""

import math  # importamos la libreria math.

# Solita al usuario el radio de la circumferenia por teclado.
radio: int = int(input("Ingrese el radio de la circunferencia: "))

# Formula
area_circumference: float = math.pi * radio ** 2

# Mostramos por pantalla
print(f"El área de la circunferencia es: {area_circumference}")
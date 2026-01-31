"""
Realice un algoritmo que calcule el área de un cuadrado.
"""
# Solicita al usuario que ingrese por teclado el lado de un cuadrado.
side: int = int(input("Ingresa un número entero: "))

# Formula.
area: int = side * side

# Mostrando el resultado por pantalla.
print(f"El área del cuadrado es: {area}")
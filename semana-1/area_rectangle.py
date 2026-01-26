"""
Calcula el área de un rectángulo.

"""
# Se le solicita al usuario qe ingrese los datos por teclado.
base: float = float(input("Ingresa la base: "))
height: float = float(input("Ingresa la altura: "))

# Formula.
area_rectangle = base * height

# Mostramos por pantalla el resultado.
print(f"El área del rectángulo es: {area_rectangle}")

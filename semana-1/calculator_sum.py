"""
Pide dos números y muestra la suma.

"""

# Solicita al usuario que ingrese datos por teclado
number_one: float = float(input("Ingresa un número: "))
number_two: float = float(input("Ingresa otro número: "))

# Formula.
calculator_sum: float = number_one + number_two

# Mostramos el resultado por pantalla.
print(f"La suma de {number_one} y {number_two} es: {calculator_sum}")

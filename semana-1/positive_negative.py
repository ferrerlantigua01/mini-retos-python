"""
Pide un número y di si es positivo o negativo.

"""
# Solicita al usuario que ingrese datos por teclado.
number: int = int(input("Ingresa un número: "))

# Vslidamos si es cero, mayor a cero y negtivo.
if number == 0:
    print(f"El {number} es neutro.")
elif number > 0:
    print(f"El {number} es positivo.")
else:
    print(f"El {number} es negativo.")
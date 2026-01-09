"""
Pide un número y di si es positivo o negativo.

"""

number: int = int(input("Ingresa un número: "))

if number == 0:
    print(f"El {number} es neutro.")
elif number > 0:
    print(f"El {number} es positivo.")
else:
    print(f"El {number} es negativo.")
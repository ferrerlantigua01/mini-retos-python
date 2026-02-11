"""
Verificar si un número es par o impar.

"""
# Solicitar los datos al usuario por teclado
number: int = int(input("Ingrese un número: "))

# Saca residuo de la division. (multiplo de 2)
odd_even: int = number % 2
# verificamos si el número es 0
# luego preguntamoos si es mayor y par
# luego preguntamos si es mayor e impar
# luego preguntamos si es menor y par
#  luego preguntamos si es menor e impar
if number == 0:
    print(f"El {number} es neutro.")
elif number > 0 and odd_even == 0:
    print(f"El {number} es positivo par")
elif number > 0 and odd_even != 0:
    print(f"El {number} es positivo impar")
elif number < 0 and odd_even == 0:
    print(f"El {number} es negativo par")
elif number < 0 and odd_even != 0:
    print(f"El {number} es negativo impar")


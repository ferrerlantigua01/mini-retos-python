"""
Verificar si un número es múltiplo de 5.

"""

# Solicitar los datos al usuario por teclado.
number: int = int(input("Ingresa un número: "))

# Saca el residuo de la division. 
multiple: int = number % 5 # multiplo de 5

# Verifica si el residuo es cero o diferente a cero.
if multiple == 0:
    print(f"El {number} es multiplo de 5")
else:
    print(f"El {number} no es multiplo de 5")
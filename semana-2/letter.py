"""
Comprobar si una palabra tiene más de 5 letras.

"""
# Solicita datos al usuario por teclado.
letter: set = input("ingresa una palabra ")

# Validamos si la palabra tiene mas de 5 letras o no.
if len(letter) > 5:
    print("La palabra tiene más de 5 letras. ")
else:
    print("La palabra tiene menos de 5 letras. ")
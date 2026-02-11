"""
Comprobar si una palabra empieza con “A”.

"""

# Solicitar los datos al usuario por teclado
word: str= input("Ingresa una palabra: ")

# verificamos si la longitud de la palabra es mayor a 0 y la palabra empieza con mayuscula y con la letra A.
if len(word) > 0 and word[0].upper() == "A":
    print("La palabra empieza con A")
else:
    print("La palabra no empieza con A")

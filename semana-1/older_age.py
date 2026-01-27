"""
Programa que pida nombre y edad y diga si es mayor de edad.

"""

# Declaración de constante.
AGE = 18

# solicita al usuario que ingrese los datos por teclado.
name: str = input("Ingresa tu nombre: ").strip().title()
age: int = int(input("Ingresa tu edad: "))

# validamos si la edad que ingresaste es mayor o igual a la que tiene almacenada la constante.
if age >=AGE:
    print(f"{name} eres mayor de edad.")
else:
    print(f"{name} eres menor de edad.")
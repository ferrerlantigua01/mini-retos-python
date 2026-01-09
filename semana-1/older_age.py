"""
Programa que pida nombre y edad y diga si es mayor de edad.

"""
AGE = 18

name: str = input("Ingresa tu nombre: ").strip().title()
age: int = int(input("Ingresa tu edad: "))

if age >=AGE:
    print(f"{name} eres mayor de edad.")
else:
    print(f"{name} eres menor de edad.")
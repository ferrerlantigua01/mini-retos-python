"""
Sistema de login con usuario y contraseña.

"""
# Solicitar los datos del usuario por teclado.
user = input("Usuario: ")
password = input("Contraseña: ")

# Validar si los datos son correctos o no.
if user == "iani" and password == "1234":
    print("Bienvenido al sistema")
    print("Accediendo...")
else:
    print("Usuario o contraseña incorrectos")

"""
Validar usuario y contraseña simples.

"""
# Solicitar datos al usuario por teclado.
username: str = input("Nombre: ")
password: str = input("Clave: ")

# Validamos si username y password tienen los datos correctos o incorrectos.
if username == "admin" and password == "123":
    print("El usuario y la cotraseña son validos.")
else:
    print("El usuario y la cotraseña son invalidos.")
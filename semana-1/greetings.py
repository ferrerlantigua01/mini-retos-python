"""
Pide al usuario su nombre y salúdalo

"""
# Solicita al usuario que  ingrese los datos por teclado
name: str = input("Ingresa tu nombre: ")
name.strip()  # Quita los espaios en blancos.
name.title() # Muestra la primeras letra de cada palabra en mayuscula.

# Mostramos el resultado por pantalla.
print(f"Hola {name}, ¿cómo estás?")

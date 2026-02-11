"""
Simular un semáforo (verde, amarillo, rojo).

"""

# Solicita los datos al usuario por teclado.
traffic_light: str = input("Digita rojo, amarillo o verde: ")
 
# Evalúa el valor ingresado por teclado
match traffic_light:
    # Se ejecuta si el usuario escribe "rojo"
    case "rojo":
        print(f"El semáfaro está en {traffic_light}.")
    # Se ejecuta si el usuario escribe "amarillo"
    case "amarillo":
        print(f"El semáfaro está en {traffic_light}.")
    # Se ejecuta si el usuario escribe "verde"
    case "verde":
        print(f"El semáfaro está en {traffic_light}.")
     # Se ejecuta si el usuario escribe "un color no valido   
    case _:
        print("No existe esa color")

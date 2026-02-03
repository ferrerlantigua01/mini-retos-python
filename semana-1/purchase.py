"""
 Don José tiene una frutería y necesita calcular el total 
 de una compra. Un cliente compró 3 manzanas a $2.50 cada 
 una, 2 naranjas a $1.80 cada una y 5 plátanos a $1.20 
 cada una. Calcula el total que debe pagar el cliente.
"""
# Colocamos las cantidades que quiere el usuario 
# de cada fruta.
apple: int = 3
oranges: int = 2
bananas: int = 5

# Colocamos el precio de cada fruta.
price_apple: float = 2.50
price_oranges: float = 1.80
price_bananas: float = 1.20

# hacemos el calculo de cada fruta. 
# Multiplicandoo la cantidades de cada 
# fruta x el precio de cada fruta.
total_apple: float = price_apple * apple
total_oranges: float = price_oranges * oranges
total_bananas: float = price_bananas * bananas

# Hacemos la sumatoria de las fruta a pagar.
total_purchase: float = total_apple + total_oranges + total_bananas

print(f"El total a pagar es: {total_purchase}")
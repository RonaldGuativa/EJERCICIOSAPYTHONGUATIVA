import random

# Valor inicial de la compra (podría ser ingresado por el usuario)
vCompra = float(input("Ingrese el valor de la compra: "))

# Colores de las balotas y sus respectivos descuentos
colores = ['verde', 'amarillo', 'rojo', 'blanco']
descuentos = {'verde': 1.0, 'amarillo': 0.75, 'rojo': 0.5, 'blanco': 0.0}

# Simulamos la extracción aleatoria de una balota
bGanada = random.choice(colores)

# Determinar el descuento según el color de la balota
descuento = descuentos[bGanada]
vPagar = vCompra * (1 - descuento)

# Mostrar el resultado
print(f"Valor de la compra: ${vCompra}")
print(f"Color de la balota extraída: {bGanada.capitalize()}")

# Mostrar el valor a pagar después del descuento de la balota
print(f"Valor a pagar después del descuento: ${vPagar:.2f}")
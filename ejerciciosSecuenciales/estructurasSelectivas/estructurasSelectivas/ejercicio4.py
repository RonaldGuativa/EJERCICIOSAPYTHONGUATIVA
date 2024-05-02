import random

# Definir los descuentos según el color de la balota
descuentoRojo = 0.15  # Descuento del 15% si la balota es roja
descuentoVerde = 0.20  # Descuento del 20% si la balota es verde

# Solicitar al usuario ingresar el valor total de la compra
valorCompra = float(input("Ingrese el valor total de la compra: "))

# Simular la extracción aleatoria de un color de balota
colores = ['rojo', 'verde']
colorBalota = random.choice(colores)

# Determinar el descuento según el color de la balota
if colorBalota == 'rojo':
    descuento = descuentoRojo
elif colorBalota == 'verde':
    descuento = descuentoVerde
else:
    descuento = 0.0  # No hay descuento si el color no es rojo ni verde

# Calcular el valor a pagar después del descuento
valorDescuento = valorCompra * descuento
valorPagar = valorCompra - valorDescuento

# Imprimir los resultados
print(f"Valor de la compra: ${valorCompra:.2f}")
print(f"Color de la balota: {colorBalota}")
if descuento > 0:
    print(f"Descuento aplicado ({int(descuento * 100)}%): ${valorDescuento:.2f}")
else:
    print("No se aplicó ningún descuento.")
print(f"Valor a pagar después del descuento: ${valorPagar:.2f}")

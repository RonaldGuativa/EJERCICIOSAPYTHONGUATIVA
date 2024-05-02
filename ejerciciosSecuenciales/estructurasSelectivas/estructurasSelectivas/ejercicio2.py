


# Solicitar la cantidad de zapatillas compradas al usuario
cZapatillas = int(input("Ingrese la cantidad de zapatillas compradas: "))

# Solicitar el precio unitario de cada zapatilla al usuario
precioxZapatilla = float(input("Ingrese el precio unitario de cada zapatilla: "))

# Calcular el total de la compra
totalCompra = cZapatillas * precioxZapatilla

# Aplicar descuento según la cantidad de zapatillas compradas
if cZapatillas >= 3:
    descuento = 0.20  # Descuento del 20% si se compran tres o más zapatillas
else:
    descuento = 0.10  # Descuento del 10% si se compran menos de tres zapatillas

# Calcular el monto del descuento
montoDescuento = totalCompra * descuento

# Calcular el total a pagar después del descuento
pagoTotal = totalCompra - montoDescuento

print(f"Total a pagar por la compra de {cZapatillas} zapatillas: ${pagoTotal:.2f}")

#Aca se explica el costo sin el descuento y tambien el descuento correspondiente

print(f"Detalles de la compra:")
print(f"- Precio unitario por zapatilla: ${precioxZapatilla:.2f}")
print(f"- Total de la compra (sin descuento): ${totalCompra:.2f}")
print(f"- Descuento aplicado ({descuento * 100}%): ${montoDescuento:.2f}")
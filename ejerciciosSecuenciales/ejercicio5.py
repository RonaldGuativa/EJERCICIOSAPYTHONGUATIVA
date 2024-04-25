#ingresar los valores de las compras

valorcompra = float(input("Ingrese el valor de la compra: "))
descuento = float(input("Ingrese el valor del descuento (%): "))

# Se calcula el valor del descuento en dinero
descuento_dinero = valorcompra * (descuento / 100)

# Se calcula el valor final a pagar restando el descuento al valor de la compra
valorfinal = valorcompra - descuento_dinero

# Se muestra en pantalla la información solicitada
print("La compra fue ${:.2f}, con un descuento de ${:.2f} y el valor final a pagar es ${:.2f}".format(valorcompra, descuento_dinero, valorfinal))
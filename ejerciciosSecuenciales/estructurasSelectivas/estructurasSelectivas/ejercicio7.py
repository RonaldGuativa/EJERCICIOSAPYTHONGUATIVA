# Solicitar al usuario ingresar la cantidad de llantas a comprar
cantidadLlantas = int(input("Ingrese la cantidad de llantas a comprar: "))

# Definir los precios por cantidad de llantas según la promoción establecida
if cantidadLlantas < 5:
    precioxLlanta = 300  # Precio por llanta si se compran menos de cinco
elif cantidadLlantas >= 5 and cantidadLlantas <= 10:
    precioxLlanta = 250  # Precio por llanta si se compran entre cinco y diez
else:
    precioxLlanta = 200  # Precio por llanta si se compran más de diez

# Calcular el precio total de las llantas
precioTotal = cantidadLlantas * precioxLlanta

# Imprimir el resultado
print(f"Cantidad de llantas a comprar: {cantidadLlantas}")
print(f"Precio por llanta: ${precioxLlanta}")
print(f"Precio total a pagar: ${precioTotal}")

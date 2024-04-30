# Solicitar al usuario ingresar la cantidad de llantas a comprar
cantidad_llantas = int(input("Ingrese la cantidad de llantas a comprar: "))

# Definir los precios por cantidad de llantas según la promoción establecida
if cantidad_llantas < 5:
    precio_por_llanta = 300  # Precio por llanta si se compran menos de cinco
elif cantidad_llantas >= 5 and cantidad_llantas <= 10:
    precio_por_llanta = 250  # Precio por llanta si se compran entre cinco y diez
else:
    precio_por_llanta = 200  # Precio por llanta si se compran más de diez

# Calcular el precio total de las llantas
precio_total = cantidad_llantas * precio_por_llanta

# Imprimir el resultado
print(f"Cantidad de llantas a comprar: {cantidad_llantas}")
print(f"Precio por llanta: ${precio_por_llanta}")
print(f"Precio total a pagar: ${precio_total}")

# Solicitar el monto total de la compra a la empresa
montoCompra = float(input("Ingrese el monto total de la compra: "))

# Definir las condiciones según el monto de la compra
if montoCompra > 500000:
    # Caso 1: Monto de compra mayor a $500,000
    inversionPropia = 0.55 * montoCompra
    prestamoBanco = 0.30 * montoCompra
    creditoFabricante = montoCompra - inversionPropia - prestamoBanco
else:
    # Caso 2: Monto de compra igual o menor a $500,000
    inversionPropia = 0.70 * montoCompra
    creditoFabricante = montoCompra - inversionPropia
    prestamoBanco = 0  # No se pide préstamo al banco en este caso

# Calcular los intereses a pagar al fabricante por el crédito
interesesCredito = 0.20 * creditoFabricante

# Imprimir los resultados
print(f"Valor invertido de su propio dinero: ${inversionPropia:.2f}")
print(f"Valor prestado al banco: ${prestamoBanco:.2f}")
print(f"Valor del crédito solicitado al fabricante: ${creditoFabricante:.2f}")
print(f"Intereses a pagar al fabricante por el crédito: ${interesesCredito:.2f}")

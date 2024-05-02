# Se solicita el monto total de la compra a la empresa
monto_compra = float(input("Ingrese el monto total de la compra: "))

#De la linea 4 a 14 se Defininen las condiciones según el monto de la compra
if monto_compra > 500000:
    # Caso 1: Monto de compra mayor a $500,000
    inversion_propia = 0.55 * monto_compra
    prestamo_banco = 0.30 * monto_compra
    credito_fabricante = monto_compra - inversion_propia - prestamo_banco
else:
    # Caso 2: Monto de compra igual o menor a $500,000
    inversion_propia = 0.70 * monto_compra
    credito_fabricante = monto_compra - inversion_propia
    prestamo_banco = 0  # No se pide préstamo al banco en este caso

# Calcular los intereses a pagar al fabricante por el crédito
intereses_credito = 0.20 * credito_fabricante

#De la linea 20 a 23 se muestran los resultados segun la condicion a la que corresponda 
print(f"Valor invertido de su propio dinero: ${inversion_propia:.2f}")
print(f"Valor prestado al banco: ${prestamo_banco:.2f}")
print(f"Valor del crédito solicitado al fabricante: ${credito_fabricante:.2f}")
print(f"Intereses a pagar al fabricante por el crédito: ${intereses_credito:.2f}")

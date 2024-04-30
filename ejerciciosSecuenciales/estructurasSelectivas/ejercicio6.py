# Solicitar al usuario ingresar el promedio obtenido por el alumno en el último periodo
promedio = float(input("Ingrese el promedio obtenido por el alumno: "))

# Definir el costo base de la pensión (sin IVA)
pension_base = 1000  # Por ejemplo, $1000

# Calcular el descuento y el monto a pagar según el promedio obtenido
if promedio >= 9:
    descuento = 0.30  # Descuento del 30% si el promedio es mayor o igual a 9
else:
    descuento = 0.0  # Sin descuento si el promedio es menor que 9

# Calcular el monto a pagar después de aplicar el descuento (si corresponde)
monto_descuento = pension_base * descuento
pension_con_descuento = pension_base - monto_descuento

# Calcular el monto total a pagar, incluyendo el 10% de IVA si no hay descuento
if descuento == 0.0:
    iva = 0.10
else:
    iva = 0.0  # No se aplica IVA si hay descuento

# Calcular el monto total a pagar incluyendo el IVA (si corresponde)
monto_iva = pension_con_descuento * iva
total_a_pagar = pension_con_descuento + monto_iva

# Imprimir el resultado
print(f"Promedio obtenido por el alumno: {promedio}")
print(f"Monto a pagar por la pensión con descuento (30%): ${pension_con_descuento:.2f}")
print(f"Monto a pagar por concepto de IVA (10%): ${monto_iva:.2f}")
print(f"Total a pagar por el alumno: ${total_a_pagar:.2f}")

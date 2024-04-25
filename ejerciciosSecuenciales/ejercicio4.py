#ingresar la informacion y ingresar los valores correspodientes

vendedor=input("ingrese el nombre del vendedor Papi")
sueldo=float(input("ingrese el sueldo bby "))
ComisionV=float(input("ingrese el valor de la comision honey"))
VentasT=float(input("ingrese el numero de ventas porfi"))

#sumar el sueldo con la comision 

sueldoTotal= sueldo+ComisionV

#sacar el porcentaje 

PorcentajeComision= 0.05

#hacer el proceso del valor de la comision por ventas

ComisionV=VentasT*PorcentajeComision

#muestra toda la informacion ingresada en orden 

print("El vendedor",vendedor,"tiene un sueldo de",sueldo,"y durante su quincena de trabajo tuvo una comision de",ComisionV,"y el valor final que el tiene que cobrar de su sueldo es",sueldoTotal)
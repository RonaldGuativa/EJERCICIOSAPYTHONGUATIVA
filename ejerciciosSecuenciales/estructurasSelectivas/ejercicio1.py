


#ingresar las notas

nota1=float(input("ingrese la nota 1 porfi"))
nota2=float(input("ingrese la nota 2 porfi"))
nota3=float(input("ingrese la nota 3 porfi"))

#hacer la formula para promedio para saber la nota 

promedio=(nota1+nota2+nota3)/3

#muestra toda la informacion ingresada en orden

print("El promedio de los 3 numeros es",promedio,)

#
if promedio >= 70:
    print(f"El aprendiz ha aprobado Algoritmia con un promedio de {promedio:.2f}")
else:
    print(f"El aprendiz ha desaprobado Algoritmia con un promedio de {promedio:.2f}")
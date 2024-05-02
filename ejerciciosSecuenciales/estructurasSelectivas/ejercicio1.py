

nota1=float(input("ingrese la nota 1 porfi"))
nota2=float(input("ingrese la nota 2 porfi"))
nota3=float(input("ingrese la nota 3 porfi"))

#de las lineas 3 a 5 se ingresan las notas para el promedio


#hacer la formula para promedio para saber la nota 

promedio=(nota1+nota2+nota3)/3

#muestra toda la informacion ingresada en orden

print("El promedio de los 3 numeros es",promedio,)

#se muestra en pantalla el resultado de la ecuacion

if promedio >= 70:
    print(f"El aprendiz ha aprobado Algoritmia con un promedio de {promedio:.2f}")
else:
    print(f"El aprendiz ha desaprobado Algoritmia con un promedio de {promedio:.2f}")

#De las lineas 20 a 23 se muestra el mensaje respecto a la condicion que corresponda

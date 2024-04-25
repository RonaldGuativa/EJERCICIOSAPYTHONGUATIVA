# Se solicita al usuario que ingrese el nombre del estudiante y las calificaciones correspondientes
nombre_estudiante = input("Ingrese el nombre del estudiante: ")
actividades_clase = float(input("Ingrese la calificación promedio de las actividades en clase: "))
proyecto_final = float(input("Ingrese la calificación del proyecto final: "))
evaluaciones_parciales = float(input("Ingrese la calificación promedio de las evaluaciones parciales: "))

# Se calcula la nota final 
nota_final = (actividades_clase * 0.3) + (proyecto_final * 0.5) + (evaluaciones_parciales * 0.2)

# Se muestra informacion se ingreso
print("La nota final de algoritmia del estudiante {} es: {:.2f}".format(nombre_estudiante, nota_final))
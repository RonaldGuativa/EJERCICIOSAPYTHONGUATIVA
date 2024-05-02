def determinar_anemia(edadMeses, nivelHemoglobina, sexo):
    # Convertir la edad de meses a años para simplificar las comparaciones
    edad_anios = edadMeses / 12.0

    # Definir los rangos de hemoglobina según la tabla
    if edadMeses <= 1:
        if nivelHemoglobina < 13 or nivelHemoglobina > 26:
            return True  # Anemia positiva
        else:
            return False  # No hay anemia
    elif 1 < edadMeses <= 6:
        if nivelHemoglobina < 10 or nivelHemoglobina > 18:
            return True
        else:
            return False
    elif 6 < edadMeses <= 12:
        if nivelHemoglobina < 11 or nivelHemoglobina > 15:
            return True
        else:
            return False
    elif 1 < edad_anios <= 5:
        if nivelHemoglobina < 11.5 or nivelHemoglobina > 15:
            return True
        else:
            return False
    elif 5 < edad_anios <= 10:
        if nivelHemoglobina < 12.6 or nivelHemoglobina > 15.5:
            return True
        else:
            return False
    elif 10 < edad_anios <= 15:
        if nivelHemoglobina < 13 or nivelHemoglobina > 15.5:
            return True
        else:
            return False
    elif edad_anios > 15:
        if sexo == "mujer":
            if nivelHemoglobina < 12 or nivelHemoglobina > 16:
                return True
            else:
                return False
        elif sexo == "hombre":
            if nivelHemoglobina < 14 or nivelHemoglobina > 18:
                return True
            else:
                return False
    else:
        return "Edad fuera de rango"

# Función para solicitar datos al usuario e imprimir el resultado de anemia
def evaluarAnemia():
    # Solicitar datos al usuario
    edadMeses = float(input("Ingrese la edad en meses: "))
    nivelHemoglobina = float(input("Ingrese el nivel de hemoglobina en g%: "))
    sexo = input("Ingrese el sexo (mujer/hombre): ").lower()  # Convertir a minúsculas

    # Llamar a la función determinar_anemia con los datos ingresados
    tieneAnemia = determinar_anemia(edadMeses, nivelHemoglobina, sexo)

    # Mostrar el resultado de la evaluación de anemia
    if isinstance(tieneAnemia, bool):  # Verificar si el resultado es booleano
        if tieneAnemia:
            print("La persona tiene anemia.")
        else:
            print("La persona no tiene anemia.")
    else:
        print("Error:", tieneAnemia)  # Mostrar mensaje de error si la edad está fuera de rango

# Llamar a la función para evaluar la anemia
evaluarAnemia()

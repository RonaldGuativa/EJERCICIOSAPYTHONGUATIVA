# Solicitar al usuario ingresar su sexo (femenino o masculino)
sexo = input("Ingrese su sexo (femenino o masculino): ").lower()

# Solicitar al usuario ingresar su edad
edad = int(input("Ingrese su edad: "))

# de la linea 8 a 14 calculamos el número de pulsaciones por cada 10 segundos de ejercicio aeróbico
if sexo == 'femenino':
    num_pulsaciones = (220 - edad) / 10
elif sexo == 'masculino':
    num_pulsaciones = (210 - edad) / 10
else:
    print("Sexo no válido. Por favor ingrese 'femenino' o 'masculino'.")
    num_pulsaciones = None  # Marcar como None si el sexo no es válido

#de la linea 17 a 18 imprimimos el resultado si el sexo es válido
if num_pulsaciones is not None:
    print(f"Número de pulsaciones por cada 10 segundos de ejercicio: {num_pulsaciones:.2f}")

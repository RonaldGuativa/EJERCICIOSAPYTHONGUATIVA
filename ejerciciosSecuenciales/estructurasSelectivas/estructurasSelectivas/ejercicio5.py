# Solicitar al usuario ingresar su sexo (femenino o masculino)
sexo = input("Ingrese su sexo (femenino o masculino): ").lower()

# Solicitar al usuario ingresar su edad
edad = int(input("Ingrese su edad: "))

# Calcular el número de pulsaciones por cada 10 segundos de ejercicio aeróbico
if sexo == 'femenino':
    numPulsaciones = (220 - edad) / 10
elif sexo == 'masculino':
    numPulsaciones = (210 - edad) / 10
else:
    print("Sexo no válido. Por favor ingrese 'femenino' o 'masculino'.")
    numPulsaciones = None  # Marcar como None si el sexo no es válido

# Imprimir el resultado si el sexo es válido
if numPulsaciones is not None:
    print(f"Número de pulsaciones por cada 10 segundos de ejercicio: {numPulsaciones:.2f}")

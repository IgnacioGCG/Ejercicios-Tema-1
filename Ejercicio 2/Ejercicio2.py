# Ejercicio2.py

# Definir el capital inicial
capital_inicial = 1000

# Leer la tasa de interés anual
tasa_interes = float(input("Introduce la tasa de interés anual (entre 1% y 10%): "))

# Verificar que la tasa de interés esté en el rango correcto
if tasa_interes < 1 or tasa_interes > 10:
    print("La tasa de interés debe estar entre 1% y 10%.")
else:
    # Convertir la tasa de interés a un valor decimal
    tasa_interes /= 100

    # Leer el número de años
    años = int(input("Introduce el número de años: "))

    # Calcular el capital final usando la fórmula del interés compuesto
    capital_final = capital_inicial * (1 + tasa_interes) ** años

    # Mostrar el capital final
    print(f"El capital final después de {años} años es: {capital_final:.2f}")
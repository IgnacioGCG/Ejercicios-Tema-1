def formatear_receta(cadena_corrupta):
    # Invertir la cadena
    cadena_invertida = cadena_corrupta[::-1]
    
    # Separar el nombre de la receta y las calorías
    partes = cadena_invertida.split(' ', 1)
    calorias = partes[0]
    nombre_receta = partes[1]
    
    # Formatear la cadena
    resultado = f"La receta de {nombre_receta} contiene {calorias} calorías."
    return resultado

# Ejemplo de uso
cadena_corrupta = "sainolac 052 alohciN"
print(formatear_receta(cadena_corrupta))

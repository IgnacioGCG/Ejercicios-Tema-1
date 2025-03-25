# Definir las dos listas de palabras
lista1 = ["manzana", "banana", "pera", "naranja", "uva"]
lista2 = ["pera", "kiwi", "banana", "mango", "uva"]

# Generar la tercera lista con las palabras que se repiten en ambas listas, sin repetición
lista3 = list(set(lista1) & set(lista2))

# Imprimir la tercera lista
print(lista3)
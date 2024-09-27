#Escribe un programa que identifique y muestre los elementos que se repiten en una
#lista.

# Solicitar una lista de números al usuario, separados por espacio
numeros_usuario = input("Ingresa una lista de números separados por espacio: ")

# Convertir los números ingresados en una lista de enteros
numeros_lista = list(map(int, numeros_usuario.split()))

# Diccionario para contar las ocurrencias de cada número
contador = {}

# Contar las ocurrencias de cada número en la lista
for numero in numeros_lista:
    if numero in contador:
        contador[numero] += 1
    else:
        contador[numero] = 1

# Encontrar y mostrar los elementos que se repiten
repetidos = [numero for numero, cuenta in contador.items() if cuenta > 1]

# Mostrar los resultados
if repetidos:
    print(f"Los elementos que se repiten son: {repetidos}")
else:
    print("No hay elementos que se repitan.")



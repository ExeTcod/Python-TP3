#Escribe un programa que pida al usuario una lista de números y cuente cuántos de
#ellos son pares y cuántos son impares.


# Solicitar una lista de números al usuario, separados por espacio
numeros_usuario = input("Ingresa una lista de números separados por espacio: ")

# Convertir los números ingresados en una lista de enteros
numeros_lista = list(map(int, numeros_usuario.split()))

# Utilizar comprensión de listas para contar los números pares e impares
pares = [x for x in numeros_lista if x % 2 == 0]
impares = [x for x in numeros_lista if x % 2 != 0]

# Mostrar los resultados
print(f"Cantidad de números pares: {len(pares)}")
print(f"Cantidad de números impares: {len(impares)}")

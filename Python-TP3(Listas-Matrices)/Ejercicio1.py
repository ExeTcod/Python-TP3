#Escribe un programa que permita al usuario ingresar una lista de números y calcule la
#suma de todos los elementos en la lista.

# Solicitar una lista de números al usuario, separados por espacio
numeros_usuario = input("Ingresa una lista de números separados por espacio: ")

# Convertir los números ingresados en una lista de enteros
numeros_lista = list(map(int, numeros_usuario.split()))

# Utilizar la función sum para calcular la suma de los elementos
suma_total = sum(numeros_lista)

# Mostrar el resultado
print(f"La suma de los números es: {suma_total}")

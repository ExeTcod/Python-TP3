#Escribe un programa que pida al usuario una lista de números y encuentre el mayor y
#el menor de ellos.

# Solicitar una lista de números al usuario, separados por espacio
numeros_usuario = input("Ingresa una lista de números separados por espacio: ")

# Convertir los números ingresados en una lista de enteros
numeros_lista = list(map(int, numeros_usuario.split()))

# Utilizar las funciones max y min para encontrar el mayor y el menor
numero_mayor = max(numeros_lista)
numero_menor = min(numeros_lista)

# Mostrar los resultados
print(f"El número mayor es: {numero_mayor}")
print(f"El número menor es: {numero_menor}")


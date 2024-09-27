#Escribe un programa que permita al usuario ingresar una lista de números y elimine los
#elementos duplicados.


# Solicitar una lista de números al usuario, separados por espacio
numeros_usuario = input("Ingresa una lista de números separados por espacio: ")

# Convertir los números ingresados en una lista de enteros
numeros_lista = list(map(int, numeros_usuario.split()))

# Utilizar la función set para eliminar duplicados y convertirlo de nuevo en lista
numeros_sin_duplicados = list(set(numeros_lista))

# Mostrar la lista sin duplicados
print(f"Lista sin duplicados: {numeros_sin_duplicados}")




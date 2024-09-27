#Escribe un programa que permita al usuario ingresar una lista y un número, y cuente
#cuántas veces aparece ese número en la lista.


def contar_apariciones(numeros, numero_buscar):
    """Función que cuenta cuántas veces aparece un número en la lista."""
    return numeros.count(numero_buscar)

# Solicitar una lista de números al usuario, separados por espacio
numeros_usuario = input("Ingresa una lista de números separados por espacio: ")

# Convertir los números ingresados en una lista de enteros
numeros_lista = list(map(int, numeros_usuario.split()))

# Solicitar el número a buscar
numero_buscar = int(input("Ingresa el número que deseas contar en la lista: "))

# Contar cuántas veces aparece el número en la lista
cantidad_apariciones = contar_apariciones(numeros_lista, numero_buscar)

# Mostrar el resultado
print(f"El número {numero_buscar} aparece {cantidad_apariciones} veces en la lista.")

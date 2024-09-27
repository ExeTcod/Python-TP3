#Escribe un programa que permita al usuario ingresar una lista de números y eliminar
#un elemento en un índice especificado.

# Solicitar una lista de números al usuario, separados por espacio
numeros_usuario = input("Ingresa una lista de números separados por espacio: ")

# Convertir los números ingresados en una lista de enteros
numeros_lista = list(map(int, numeros_usuario.split()))

# Mostrar la lista original
print(f"Lista original: {numeros_lista}")

# Solicitar el índice del elemento a eliminar
indice_eliminar = int(input("Ingresa el índice del elemento que deseas eliminar: "))

# Verificar si el índice es válido
if 0 <= indice_eliminar < len(numeros_lista):
    # Eliminar el elemento en el índice especificado usando 'del'
    elemento_eliminado = numeros_lista[indice_eliminar]
    del numeros_lista[indice_eliminar]
    print(f"Elemento eliminado: {elemento_eliminado}")
else:
    print("Índice inválido. Por favor, ingresa un índice dentro del rango de la lista.")

# Mostrar la lista actualizada
print(f"Lista actualizada: {numeros_lista}")

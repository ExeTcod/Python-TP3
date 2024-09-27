#Escribe un programa que permita al usuario ingresar una lista y la invierta

# Solicitar una lista de números al usuario, separados por espacio
numeros_usuario = input("Ingresa una lista de números separados por espacio: ")

# Convertir los números ingresados en una lista de enteros
numeros_lista = list(map(int, numeros_usuario.split()))

# Utilizar la función reverse para invertir la lista
numeros_lista.reverse()

# Mostrar la lista invertida
print(f"La lista invertida es: {numeros_lista}")



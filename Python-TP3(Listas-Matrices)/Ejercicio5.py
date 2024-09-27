#Escribe un programa que multiplique cada elemento de una lista de números por un
#valor ingresado por el usuario.

# Solicitar una lista de números al usuario, separados por espacio
numeros_usuario = input("Ingresa una lista de números separados por espacio: ")

# Convertir los números ingresados en una lista de enteros
numeros_lista = list(map(int, numeros_usuario.split()))

# Solicitar el valor por el cual se va a multiplicar cada elemento
multiplicador = int(input("Ingresa el valor por el cual deseas multiplicar: "))

# Multiplicar cada elemento de la lista por el valor ingresado utilizando comprensión de listas
resultado = [x * multiplicador for x in numeros_lista]

# Mostrar la lista resultante
print(f"Lista resultante después de multiplicar: {resultado}")




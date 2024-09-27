#Escribe un programa que permita al usuario ingresar una lista de números y calcule el
#promedio de los elementos.

# Solicitar una lista de números al usuario, separados por espacio
numeros_usuario = input("Ingresa una lista de números separados por espacio: ")

# Convertir los números ingresados en una lista de enteros
numeros_lista = list(map(int, numeros_usuario.split()))

# Calcular el promedio
if len(numeros_lista) > 0:
    promedio = sum(numeros_lista) / len(numeros_lista)
    print(f"El promedio de los números es: {promedio}")
else:
    print("La lista está vacía, no se puede calcular el promedio.")




#Escribe un programa que sume dos listas de números elemento por elemento. Las
#listas deben tener la misma longitud.

def sumar_listas(lista1, lista2):
    #Función que suma dos listas elemento por elemento.
    return [a + b for a, b in zip(lista1, lista2)]

# Solicitar la primera lista de números al usuario
numeros_usuario1 = input("Ingresa la primera lista de números separados por espacio: ")
lista1 = list(map(int, numeros_usuario1.split()))

# Solicitar la segunda lista de números al usuario
numeros_usuario2 = input("Ingresa la segunda lista de números separados por espacio: ")
lista2 = list(map(int, numeros_usuario2.split()))

# Verificar que las listas tengan la misma longitud
if len(lista1) != len(lista2):
    print("Las listas deben tener la misma longitud.")
else:
    # Sumar las listas utilizando la función
    resultado = sumar_listas(lista1, lista2)
    
    # Mostrar el resultado
    print(f"La suma de las dos listas es: {resultado}")

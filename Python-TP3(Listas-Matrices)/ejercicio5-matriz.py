#Escribe un programa que encuentre el valor más grande en una lista bidimensional.

def encontrar_maximo(matriz):
    """Función que encuentra el valor máximo en una lista bidimensional."""
    maximo = float('-inf')  # Inicializar el máximo con el valor más pequeño posible

    for fila in matriz:
        for elemento in fila:
            if elemento > maximo:
                maximo = elemento  # Actualizar el máximo si se encuentra un nuevo máximo

    return maximo

# Solicitar el tamaño de la matriz
filas = int(input("Ingresa el número de filas de la matriz: "))
columnas = int(input("Ingresa el número de columnas de la matriz: "))

# Inicializar la matriz
matriz = []

# Solicitar los elementos de la matriz
print("Ingresa los elementos de la matriz:")
for i in range(filas):
    fila = list(map(int, input(f"Fila {i + 1}: ").split()))
    while len(fila) != columnas:
        print(f"Por favor, ingresa exactamente {columnas} elementos.")
        fila = list(map(int, input(f"Fila {i + 1}: ").split()))
    matriz.append(fila)

# Encontrar el valor máximo en la matriz
maximo = encontrar_maximo(matriz)

# Mostrar la matriz
print("\nMatriz:")
for fila in matriz:
    print(fila)

# Mostrar el valor máximo encontrado
print("El valor más grande en la matriz es:", maximo)



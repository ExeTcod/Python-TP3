#Escribe un programa que calcule la transpuesta de una matriz. La transpuesta de una
#matriz intercambia sus filas por columnas.

def calcular_transpuesta(matriz):
    """Calcula la matriz transpuesta."""
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

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

# Calcular la transpuesta de la matriz
transpuesta = calcular_transpuesta(matriz)

# Mostrar la matriz original
print("\nMatriz original:")
for fila in matriz:
    print(fila)

# Mostrar la matriz transpuesta
print("\nMatriz transpuesta:")
for fila in transpuesta:
    print(fila)


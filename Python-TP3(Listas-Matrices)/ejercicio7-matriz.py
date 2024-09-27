#Escribe un programa que extraiga los elementos de la diagonal principal de una matriz
#cuadrada.

def extraer_diagonal_principal(matriz):
    """Extrae los elementos de la diagonal principal de una matriz cuadrada."""
    diagonal = []
    for i in range(len(matriz)):
        diagonal.append(matriz[i][i])  # Agrega el elemento de la diagonal principal
    return diagonal

# Solicitar el tamaño de la matriz cuadrada
n = int(input("Ingresa el tamaño de la matriz cuadrada (n x n): "))

# Inicializar la matriz
matriz = []

# Solicitar los elementos de la matriz
print("Ingresa los elementos de la matriz:")
for i in range(n):
    fila = list(map(int, input(f"Fila {i + 1}: ").split()))
    while len(fila) != n:
        print(f"Por favor, ingresa exactamente {n} elementos.")
        fila = list(map(int, input(f"Fila {i + 1}: ").split()))
    matriz.append(fila)

# Extraer la diagonal principal
diagonal_principal = extraer_diagonal_principal(matriz)

# Mostrar la matriz
print("\nMatriz:")
for fila in matriz:
    print(fila)

# Mostrar los elementos de la diagonal principal
print("Elementos de la diagonal principal:", diagonal_principal)



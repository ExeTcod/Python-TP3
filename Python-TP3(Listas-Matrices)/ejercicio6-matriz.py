#Escribe un programa que multiplique cada elemento de una lista bidimensional por un
#valor escalar dado por el usuario.

def multiplicar_matriz_por_escalar(matriz, escalar):
    """Multiplica cada elemento de una lista bidimensional por un valor escalar."""
    matriz_resultante = []  # Inicializar la matriz resultante

    for fila in matriz:
        # Multiplicar cada elemento de la fila por el escalar y agregarla a la matriz resultante
        fila_resultante = [elemento * escalar for elemento in fila]
        matriz_resultante.append(fila_resultante)

    return matriz_resultante

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

# Solicitar el valor escalar
escalar = float(input("Ingresa el valor escalar por el cual multiplicar los elementos: "))

# Multiplicar la matriz por el escalar
matriz_resultante = multiplicar_matriz_por_escalar(matriz, escalar)

# Mostrar la matriz original
print("\nMatriz original:")
for fila in matriz:
    print(fila)

# Mostrar la matriz resultante
print("\nMatriz después de multiplicar por el escalar:")
for fila in matriz_resultante:
    print(fila)


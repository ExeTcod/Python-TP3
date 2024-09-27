#Crea un programa que genere una matriz identidad de tamaño n. Una matriz identidad
#es una matriz cuadrada donde los elementos de la diagonal principal son 1 y el resto
#son 0

def generar_matriz_identidad(n):
    """Genera una matriz identidad de tamaño n x n."""
    matriz_identidad = []  # Inicializar la matriz

    for i in range(n):
        fila = []  # Inicializar una nueva fila
        for j in range(n):
            if i == j:
                fila.append(1)  # Colocar 1 en la diagonal principal
            else:
                fila.append(0)  # Colocar 0 en otras posiciones
        matriz_identidad.append(fila)  # Agregar la fila a la matriz

    return matriz_identidad

# Solicitar el tamaño de la matriz
n = int(input("Ingresa el tamaño de la matriz identidad (n): "))

# Generar la matriz identidad
matriz_identidad = generar_matriz_identidad(n)

# Mostrar la matriz identidad
print("\nMatriz identidad de tamaño", n, "x", n, ":")
for fila in matriz_identidad:
    print(fila)



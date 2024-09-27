#Crea un programa que genere una matriz identidad inversa de tamaño n. Una matriz
#identidad inversa es una matriz cuadrada donde los elementos de la diagonal inversa
#principal son 1 y el resto son 0.

def generar_matriz_identidad_inversa(n):
    """Genera una matriz identidad inversa de tamaño n x n."""
    matriz_inversa = []  # Inicializar la matriz

    for i in range(n):
        fila = []  # Inicializar una nueva fila
        for j in range(n):
            if i + j == n - 1:
                fila.append(1)  # Colocar 1 en la diagonal inversa principal
            else:
                fila.append(0)  # Colocar 0 en otras posiciones
        matriz_inversa.append(fila)  # Agregar la fila a la matriz

    return matriz_inversa

# Solicitar el tamaño de la matriz
n = int(input("Ingresa el tamaño de la matriz identidad inversa (n): "))

# Generar la matriz identidad inversa
matriz_inversa = generar_matriz_identidad_inversa(n)

# Mostrar la matriz identidad inversa
print("\nMatriz identidad inversa de tamaño", n, "x", n, ":")
for fila in matriz_inversa:
    print(fila)


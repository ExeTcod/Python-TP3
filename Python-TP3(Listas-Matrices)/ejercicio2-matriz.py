#Escribe un programa que calcule la suma de todos los elementos en una lista
#bidimensional.

def suma_matriz(matriz):
    """Función que calcula la suma de todos los elementos en una lista bidimensional."""
    suma_total = 0  # Inicializar la suma total
    
    for fila in matriz:
        suma_total += sum(fila)  # Sumar los elementos de cada fila

    return suma_total

# Ejemplo de uso de la función
matriz_bidimensional = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Calcular la suma de todos los elementos en la matriz
resultado = suma_matriz(matriz_bidimensional)

# Mostrar el resultado
print("La suma de todos los elementos en la matriz es:", resultado)

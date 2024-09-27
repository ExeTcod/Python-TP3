#Modifica el programa anterior para que imprima la suma de cada fila de la lista
#bidimensional.

def suma_matriz(matriz):
    """Función que calcula la suma de cada fila y la suma total en una lista bidimensional."""
    suma_total = 0  # Inicializar la suma total

    for i, fila in enumerate(matriz):
        suma_fila = sum(fila)  # Sumar los elementos de la fila
        suma_total += suma_fila  # Agregar la suma de la fila a la suma total
        print(f"Suma de la fila {i + 1}: {suma_fila}")  # Imprimir la suma de la fila

    return suma_total

# Ejemplo de uso de la función
matriz_bidimensional = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Calcular la suma de todos los elementos en la matriz
resultado_total = suma_matriz(matriz_bidimensional)

# Mostrar el resultado total
print("La suma total de todos los elementos en la matriz es:", resultado_total)



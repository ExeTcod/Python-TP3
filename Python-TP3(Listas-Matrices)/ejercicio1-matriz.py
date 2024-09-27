#Crea una función que reciba dos parámetros: el número de filas y columnas. La función
#debe generar una matriz de ese tamaño, donde los valores son números enteros
#consecutivos empezando desde 1.

def generar_matriz(filas, columnas):
    """Genera una matriz de tamaño filas x columnas con números enteros consecutivos."""
    matriz = []
    contador = 1  # Comenzar desde 1
    
    for i in range(filas):
        fila = []  # Inicializar una nueva fila
        for j in range(columnas):
            fila.append(contador)  # Agregar el número actual a la fila
            contador += 1  # Incrementar el contador
        matriz.append(fila)  # Agregar la fila a la matriz
    
    return matriz

# Ejemplo de uso de la función
filas = int(input("Ingresa el número de filas: "))
columnas = int(input("Ingresa el número de columnas: "))

matriz_generada = generar_matriz(filas, columnas)

# Mostrar la matriz generada
print("Matriz generada:")
for fila in matriz_generada:
    print(fila)

import numpy as np

def esSimetrica(matriz):
  
    matriz = np.array(matriz)
    
    return np.array_equal(matriz, matriz.T)
#matriz.T invierte la matriz intercambiando los valores de i y j

#Caso de prueba(Modificar para chequear)
matriz_numpy = [[1, 2, 3],
                [2, 5, 6],
                [3, 6, 9]]

if esSimetrica(matriz_numpy):
    print("La matriz es simetrica.")
else:
    print("La matriz no es simetrica.")

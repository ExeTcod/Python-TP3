import numpy as np

def rotar(matriz):
    
    matriz_numpy = np.array(matriz)
    
   
    matrizRotada = np.rot90(matriz_numpy, k=-1) 
    #(k=-1)= sentido horario (k=1)= sentido antihorario
    return matrizRotada

#Caso de prueba
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

matrizRotada = rotar(matriz)
print(matrizRotada)

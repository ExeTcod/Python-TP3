#Escribe un programa que permita al usuario ingresar una lista de números y filtre los
#números primos.

def es_primo(num):
    """Función que verifica si un número es primo."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filtrar_primos(numeros):
    """Función que filtra y devuelve los números primos de una lista."""
    return [num for num in numeros if es_primo(num)]

# Solicitar una lista de números al usuario, separados por espacio
numeros_usuario = input("Ingresa una lista de números separados por espacio: ")

# Convertir los números ingresados en una lista de enteros
numeros_lista = list(map(int, numeros_usuario.split()))

# Filtrar los números primos
numeros_primos = filtrar_primos(numeros_lista)

# Mostrar los resultados
print(f"Los números primos en la lista son: {numeros_primos}")

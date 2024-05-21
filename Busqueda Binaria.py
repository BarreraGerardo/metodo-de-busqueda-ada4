def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1

# Lista ordenada de números
numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Número a buscar
numero_a_buscar = 13

# Ejecución de la búsqueda
indice = busqueda_binaria(numeros, numero_a_buscar)

if indice != -1:
    print(f"Número encontrado en el índice {indice}")
else:
    print("Número no encontrado en la lista")
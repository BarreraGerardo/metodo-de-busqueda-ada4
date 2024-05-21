def busqueda_secuencial(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Lista de nombres
nombres = ["Ana", "Luis", "Pedro", "Maria", "Juan", "Carla", "José"]

# Nombre a buscar
nombre_a_buscar = "Maria"

# Ejecución de la búsqueda
indice = busqueda_secuencial(nombres, nombre_a_buscar)

if indice != -1:
    print(f"Nombre encontrado en el índice {indice}")
else:
    print("Nombre no encontrado en la lista")
# Programa para manipular listas y tuplas de manera interactiva

def iniciar_programa():
    print("Bienvenido al programa de manipulación de listas y tuplas.\n")

    # Capítulo 10: Cómo crear listas y utilizarlas
    mi_lista = []  # Inicializamos una lista vacía
    print("Vamos a crear una lista de frutas.")
    
    # Agregar frutas a la lista
    while True:
        fruta = input("Introduce una fruta (o escribe 'fin' para terminar): ").lower()
        if fruta == 'fin':
            break
        mi_lista.append(fruta)  # Capítulo 15: Insertar elementos con append()
    
    print(f"Lista de frutas: {mi_lista}")
    
    # Capítulo 11: Posiciones negativas
    if mi_lista:
        print(f"Última fruta de la lista (usando índice negativo): {mi_lista[-1]}")
    
    # Capítulo 12: Eliminar elementos con del()
    if mi_lista:
        print("\nEliminar una fruta de la lista por su posición.")
        posicion = int(input(f"Introduce una posición entre 0 y {len(mi_lista) - 1}: "))
        if 0 <= posicion < len(mi_lista):
            del mi_lista[posicion]
            print(f"Lista después de eliminar la fruta en la posición {posicion}: {mi_lista}")
    
    # Capítulo 13: Eliminar elementos con remove()
    if mi_lista:
        print("\nEliminar una fruta de la lista por su nombre.")
        fruta_eliminar = input("Introduce el nombre de la fruta a eliminar: ").lower()
        if fruta_eliminar in mi_lista:
            mi_lista.remove(fruta_eliminar)
            print(f"Lista después de eliminar '{fruta_eliminar}': {mi_lista}")
        else:
            print(f"La fruta '{fruta_eliminar}' no está en la lista.")
    
    # Capítulo 14: Eliminar elementos con pop()
    if mi_lista:
        print("\nEliminar la última fruta de la lista usando pop.")
        fruta_eliminada = mi_lista.pop()
        print(f"Fruta eliminada: {fruta_eliminada}")
        print(f"Lista actualizada: {mi_lista}")
    
    # Capítulo 17: Ordenar elementos con sort() y sorted()
    print("\nVamos a ordenar la lista de frutas.")
    print(f"Lista ordenada con sorted: {sorted(mi_lista)}")
    
    # Capítulo 18: Contar elementos con len()
    print(f"Número de frutas en la lista: {len(mi_lista)}")

    # Capítulo 19: Crear y manejar tuplas
    mi_tupla = tuple(mi_lista)  # Convertimos la lista a tupla
    print(f"\nTupla creada desde la lista: {mi_tupla}")

    # Capítulo 20: Convertir tuplas a listas y viceversa
    lista_desde_tupla = list(mi_tupla)  # Convertimos la tupla de nuevo a lista
    print(f"Lista convertida desde la tupla: {lista_desde_tupla}")

    # Opción para reiniciar o salir del programa
    while True:
        opcion = input("\n¿Quieres reiniciar el programa o salir? (reiniciar/salir): ").lower()
        if opcion == "reiniciar":
            iniciar_programa()
            break
        elif opcion == "salir":
            print("¡Gracias por usar el programa! Adiós.")
            return
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Iniciamos el programa
iniciar_programa()

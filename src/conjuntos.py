def elimina_duplicados(lista: list) -> list:
    """
    Devuelve la lista resultante de eliminar los elementos duplicados, 
    conservando para el resto de elementos el orden de la lista original.

    Parámetros:
    lista (list): Lista de elementos que puede contener duplicados.
    
    Devuelve:
    list: La lista sin elementos duplicados, manteniendo el orden original.
    """
    lista_res = []
    for i in lista:
        if i not in lista_res:
            lista_res.append(i)
    return lista_res

def une_conjuntos(lista_de_conjuntos: list[set]) -> set:
    """
    Devuelve el conjunto resultante de la unión de todos los conjuntos de la lista.

    Parámetros:
    lista_de_conjuntos (list[set]): Lista de conjuntos a unir.
    
    Devuelve:
    set: El conjunto resultante de la unión de todos los conjuntos.
    """
    conjunto_res = set()
    for i in lista_de_conjuntos:
        conjunto_res = conjunto_res.union(i)
    return conjunto_res


def intersecta_conjuntos(lista_de_conjuntos: list[set]) -> set:
    """
    Devuelve el conjunto resultante de la intersección de todos los conjuntos de la lista.

    Parámetros:
    lista_de_conjuntos (list[set]): Lista de conjuntos a intersectar.
    
    Devuelve:
    set: El conjunto resultante de la intersección de todos los conjuntos.
    """
    conjunto_res = une_conjuntos(lista_de_conjuntos)
    for i in lista_de_conjuntos:
        conjunto_res = conjunto_res.intersection(i)
    return conjunto_res
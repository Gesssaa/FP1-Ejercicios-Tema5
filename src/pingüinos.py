from collections import namedtuple
import csv

Penguin = namedtuple("Penguin", [
    "species",           # Especie del pingüino (Adelie, Chinstrap, Gentoo)
    "island",            # Isla donde fue observado (Torgersen, Biscoe, Dream)
    "bill_length_mm",    # Longitud del pico en milímetros
    "bill_depth_mm",     # Profundidad (grosor) del pico en milímetros
    "flipper_length_mm", # Longitud de la aleta (alas) en milímetros
    "body_mass_g",       # Masa corporal en gramos
    "sex",               # Sexo del ejemplar (male, female o NA)
    "year"               # Año en el que se tomó la muestra (2007–2009)
])

def lee_pingüinos(ruta_archivo: str) -> list[Penguin]:
    """
    Lee un archivo CSV con datos de pingüinos y devuelve una lista de
    tuplas Penguin con la información de cada pingüino.

    Parámetros:
    ruta_archivo (str): Ruta al archivo CSV que contiene los datos.

    Devuelve:
    list[Penguin]: Lista de tuplas Penguin con los datos leídos del archivo.
    """    
    with open(ruta_archivo, 'r') as f:
        pingüinos = []
        lector = csv.reader(f)
        next(f)  
        for species, island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex, year in lector:
            pingüino = Penguin(
                species=species,
                island=island,
                bill_length_mm=float(bill_length_mm) if bill_length_mm != "NA" else None,
                bill_depth_mm=float(bill_depth_mm) if bill_depth_mm != "NA" else None,
                flipper_length_mm=int(flipper_length_mm) if flipper_length_mm != "NA" else None,
                body_mass_g=int(body_mass_g) if body_mass_g != "NA" else None,
                sex=sex,
                year=int(year) if year != "NA" else None
            )
            pingüinos.append(pingüino)
        return pingüinos
    
def cuenta_pingüinos_por_especie(pingüinos: list[Penguin]) -> dict[str, int]:
    """
    Cuenta el número de pingüinos por especie.

    Parámetros:
    pingüinos (list[Penguin]): Lista de tuplas Penguin con los datos de los pingüinos.

    Devuelve:
    dict[str, int]: Diccionario que asocia cada especie de pingüino con su conteo.
    """
    dict_res = {}
    for i in pingüinos:
        if i.species not in dict_res:
            dict_res[i.species] = 0
        dict_res[i.species] += 1
    return dict_res

def calcula_media_masa_corporal_por_especie(pingüinos: list[Penguin]) -> dict[str, float]:
    """
    Calcula la masa corporal media de los pingüinos por especie.

    Parámetros:
    pingüinos (list[Penguin]): Lista de tuplas Penguin con los datos de los pingüinos.

    Devuelve:
    dict[str, float]: Diccionario que asocia cada especie de pingüino con su masa corporal media.
    """
    dict_res = {}
    dict_conteo = cuenta_pingüinos_por_especie(pingüinos)
    for i in pingüinos:
        if i.species not in dict_res:
            dict_res[i.species] = 0
        if i.body_mass_g != None:
            dict_res[i.species] += i.body_mass_g
        else:
            dict_conteo[i.species] -= 1
    for j in dict_res:
        dict_res[j] = dict_res[j]/dict_conteo[j]
    return dict_res
        

def calcula_minimo_maximo_pico_por_especie(pingüinos: list[Penguin]) -> dict[str, tuple[float, float]]:
    """
    Calcula la longitud mínima y máxima del pico de los pingüinos por especie.

    Parámetros:
    pingüinos (list[Penguin]): Lista de tuplas Penguin con los datos de los pingüinos.

    Devuelve:
    dict[str, tuple[float, float]]: Diccionario que asocia cada especie de pingüino con una tupla
                                    que contiene la longitud mínima y máxima del pico.
    """
    dict_res = {}
    for i in pingüinos:
        if i.bill_length_mm != None:
            if i.species not in dict_res:
                dict_res[i.species] = (-10, -10)
            if dict_res[i.species][0] < 0 or dict_res[i.species][1] < 0:
                dict_res[i.species] = (i.bill_length_mm, i.bill_length_mm)
            else:
                if dict_res[i.species][0] > i.bill_length_mm:
                    dict_res[i.species] = (i.bill_length_mm, dict_res[i.species][1])
                if dict_res[i.species][1] < i.bill_length_mm:
                    dict_res[i.species] = (dict_res[i.species][0], i.bill_length_mm)
    return dict_res
        

def cuenta_pingüinos_por_especie_filtro(pingüinos: list[Penguin], filtra_isla: str | None = None) -> dict[str, int]:
    """
    Cuenta el número de pingüinos por especie, opcionalmente filtrando por isla.

    Parámetros:
    pingüinos (list[Penguin]): Lista de tuplas Penguin con los datos de los pingüinos.
    filtra_isla (str, opcional): Nombre de la isla para filtrar los pingüinos. Si es None, no se aplica filtro.
    
    Devuelve:
    dict[str, int]: Diccionario que asocia cada especie de pingüino con su conteo.
    """
    dict_res = {}
    for i in pingüinos:
        if filtra_isla == None or i.island == filtra_isla:
            if i.species not in dict_res:
                dict_res[i.species] = 0
            dict_res[i.species] += 1
    return dict_res
    

def calcula_media_masa_corporal_por_especie_filtro(pingüinos: list[Penguin], filtra_isla: str | None = None) -> dict[str, float]:
    """
    Calcula la masa corporal media de los pingüinos por especie, opcionalmente filtrando por isla.

    Parámetros:
    pingüinos (list[Penguin]): Lista de tuplas Penguin con los datos de los pingüinos.
    filtra_isla (str, opcional): Nombre de la isla para filtrar los pingüinos. Si es None, no se aplica filtro.
    
    Devuelve:
    dict[str, float]: Diccionario que asocia cada especie de pingüino con su masa corporal media.
    """
    dict_res = {}
    dict_conteo = cuenta_pingüinos_por_especie(pingüinos)
    for i in pingüinos:
        if filtra_isla == None or i.island == filtra_isla:
            if i.species not in dict_res:
                dict_res[i.species] = 0
            if i.body_mass_g != None:
                dict_res[i.species] += i.body_mass_g
            else:
                dict_conteo[i.species] -= 1
        else:
            dict_conteo[i.species] -=1
    for j in dict_res:
        dict_res[j] = dict_res[j]/dict_conteo[j]
    return dict_res

def calcula_minimo_maximo_pico_por_especie_filtro(pingüinos: list[Penguin], filtra_isla: str | None = None) -> dict[str, tuple[float, float]]:
    """
    Calcula la longitud mínima y máxima del pico de los pingüinos por especie, opcionalmente filtrando por isla.

    Parámetros:
    pingüinos (list[Penguin]): Lista de tuplas Penguin con los datos de los pingüinos.
    filtra_isla (str, opcional): Nombre de la isla para filtrar los pingüinos. Si es None, no se aplica filtro.

    Devuelve:
    dict[str, tuple[float, float]]: Diccionario que asocia cada especie de
                                    pingüino con una tupla que contiene la longitud mínima y máxima del pico.
    """
    dict_res = {}
    for i in pingüinos:
        if filtra_isla == None or i.island == filtra_isla:
            if i.bill_length_mm != None:
                if i.species not in dict_res:
                    dict_res[i.species] = (-10, -10)
                if dict_res[i.species][0] < 0 or dict_res[i.species][1] < 0:
                    dict_res[i.species] = (i.bill_length_mm, i.bill_length_mm)
                else:
                    if dict_res[i.species][0] > i.bill_length_mm:
                        dict_res[i.species] = (i.bill_length_mm, dict_res[i.species][1])
                    if dict_res[i.species][1] < i.bill_length_mm:
                        dict_res[i.species] = (dict_res[i.species][0], i.bill_length_mm)
    return dict_res

from collections import Counter


def sustituye_palabras(texto: str, diccionario: dict[str, str]) -> str:
    """Sustituye en el texto las palabras que aparecen en el diccionario como claves por sus valores asociados.

    Parámetros:
        texto: Texto en el que se van a sustituir las palabras.
        diccionario: Diccionario con las palabras a sustituir como claves y las palabras sustitutas como valores.

    Devuelve:
        Texto resultante de las sustituciones.
    """
    texto_res = texto
    lista_texto = texto.split()
    for i in lista_texto:
        if i in diccionario.keys():
            texto_res = texto_res.replace(i, diccionario[i])
    return texto_res


def indexa_por_iniciales(texto: str) -> dict[str, set[str]] | None:
    """
    Construye un diccionario que indexa las distintas palabras del texto
    (pasado a minúsculas) por sus iniciales.
    
    Parámetros:
        texto: Texto del que se van a extraer las palabras.
    
    Devuelve:
        Diccionario que asocia a cada inicial el conjunto de palabras
         que comienzan por dicha inicial.
    
    """
    dict_res = {}
    texto_separado = texto.split()
    for i in texto_separado:
        i = i.lower()
        if i[0] not in dict_res.keys():
            dict_res[i[0]] = set()
        dict_res[i[0]].add(i)
    return dict_res


def construye_frecuencias_bigramas(texto: str) -> dict[str, float]:
    """
    Construye un diccionario con las frecuencias normalizadas de cada bigrama 
    en el texto dado, ignorando mayúsculas y minúsculas.

    Un bigrama es una secuencia de dos letras consecutivas en el texto.

    Cada frecuencia estará contenida entre 0 y 1.
    
    Parámetros:
        texto: Texto del que se van a contar los bigramas.
    Devuelve:
        Diccionario que asocia a cada bigrama su frecuencia normalizada en el texto.
    """
    dict_res = {}
    texto_unido = texto.strip()
    total_bigramas = 0
    for i, j in zip(texto_unido, texto_unido[1:]):
        if i+j not in dict_res:
            dict_res[i+j] = 0
        dict_res[i+j] += 1
        total_bigramas +=1
    for h in dict_res:
        dict_res[h] = dict_res[h]/total_bigramas
    return dict_res

def calcula_distancia_media_frecuencias(freq1: dict[str, float], freq2: dict[str, float]) -> float:
    """
    Calcula la distancia media entre las frecuencias normalizadas
    representadas por dos diccionarios de frecuencias.

    Parámetros:
        freq1: Primer diccionario de frecuencias.
        freq2: Segundo diccionario de frecuencias.

    Devuelve:
        Distancia media entre los dos vectores de frecuencias, o 0.0 si ambos diccionarios están vacíos.
    """
    media = 0
    num_bigramas = 0
    conjunto_claves = set()
    for i in freq1:
        conjunto_claves.add(i)
    for j in freq2:
        conjunto_claves.add(j)
    if len(conjunto_claves) == 0:
        return 0.0
    for h in conjunto_claves:
        media += abs(freq1.get(h, 0)-freq2.get(h, 0))
    media = media/len(conjunto_claves)
    return media


def identifica_idioma(textos_ejemplo: dict[str, str], texto_a_identificar: str) -> str:
    """
    Identifica el idioma de un texto comparando sus frecuencias de bigramas
    con las frecuencias de bigramas de textos de ejemplo en distintos idiomas.

    Parámetros:
        textos_ejemplo: Diccionario que asocia a cada idioma (por ejemplo 'es') un texto de ejemplo en ese idioma.
        texto_a_identificar: Texto cuyo idioma se quiere identificar.

    Devuelve:
        El idioma identificado del texto.
    """
    freq_texto = construye_frecuencias_bigramas(texto_a_identificar)
    mayor_coincidencia = ""
    menor_distancia = 100
    for i in textos_ejemplo:
        freq_idioma = construye_frecuencias_bigramas(textos_ejemplo[i])
        distancia = calcula_distancia_media_frecuencias(freq_texto, freq_idioma)
        print(f"distancia de {i} es {distancia}")
        if distancia < menor_distancia:
            menor_distancia = distancia
            mayor_coincidencia = i
    return mayor_coincidencia




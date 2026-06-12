"""
EJERCICIO: Analizador de Texto Básico (v0.1)
===========================================

OBJETIVO:
Completa la función 'contar_basico' para que lea un archivo de texto,
cuente sus elementos y devuelva un diccionario con las métricas.

ENTRADA:
- ruta (str): Ubicación del archivo de texto.

SALIDA:
- dict: Debe contener exactamente estas tres claves:
    {
        "lineas": int,
        "palabras": int,
        "caracteres": int
    }

PISTAS PASO A PASO:
1. Usa `with open(ruta, "r", encoding="utf-8") as archivo:` para abrirlo.
2. Lee todo el texto en una variable usando `archivo.read()`.
3. Para los caracteres, mide la longitud total del texto con `len()`.
4. Para las palabras, usa el método `.split()` del texto y mide el resultado.
5. Para las líneas, usa el método `.splitlines()` del texto y mide el resultado.
6. Devuelve el diccionario estructurado con los tres datos numéricos.
"""


def contar_basico(ruta):
    # 1. Abre el archivo y guarda su contenido en una variable
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            leer_archivo = archivo.read()
    except FileNotFoundError:
        print("Archivo no encontrado.\n")
        return {
            "lineas": 0,
            "palabras": 0,
            "caracteres": 0,
        }

    # 2. Cuenta los caracteres, palabras y lineas del texto leido
    caracteres_totales = len(leer_archivo)
    palabras_totales = len(leer_archivo.split())
    lineas_totales = len(leer_archivo.splitlines())

    # 3. Devuelve el diccionario con los resultados
    return {
        "lineas": lineas_totales,
        "palabras": palabras_totales,
        "caracteres": caracteres_totales,
    }


# EJERCICIO v0.2: Top 5 palabras mas frecuentes
# =================================================
# Objetivo:
# Crear una nueva funcion que lea un archivo de texto y devuelva las 5 palabras
# que mas se repiten.
#
# Pistas para la proxima clase:
# 1. Leer el contenido del archivo con `with open(...)`.
# 2. Convertir el texto a minusculas con `.lower()`.
# 3. Separar el texto en palabras con `.split()`.
# 4. Usar un diccionario para contar cuantas veces aparece cada palabra.
# 5. Ordenar el diccionario por frecuencia.
# 6. Devolver solo las 5 primeras palabras.

contador_de_texto = contar_basico("samples/ejemplo.txt")

for clave, valor in contador_de_texto.items():
    print(f"{clave} : {valor}")

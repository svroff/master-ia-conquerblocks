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

    # 2. Cuenta los caracteres totales

    # 3. Cuenta las palabras

    # 4. Cuenta las líneas

    # 5. Devuelve el diccionario con los resultados
    pass


if __name__ == "__main__":
    # Descomenta la línea de abajo para probar tu función cuando esté lista:
    # print(contar_basico("samples/ejemplo.txt"))
    pass

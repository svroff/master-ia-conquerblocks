"""
TextAnalyzer — Tu primer proyecto integrador del máster
========================================================

Pequeño analizador de ficheros de texto en Python. El proyecto se construye
capa a capa, una versión por sesión, hasta cubrir Python Básico + Python
Avanzado en un solo proyecto manejable.

Orden de trabajo:
    v0.1 -> v0.2 -> v0.3 -> v0.4 -> v0.5 -> v0.6

NO TOQUES las funciones de versiones superiores hasta que la versión
actual esté cerrada y probada. El esqueleto te marca qué va después.
"""


def contar_basico(ruta):
    """
    v0.1 — Contar líneas, palabras y caracteres de un fichero de texto.

    Args:
        ruta: ruta al fichero de texto (relativa al cwd o absoluta).

    Returns:
        dict con tres claves:
            "lineas":     int, número de líneas del fichero
            "palabras":   int, número de palabras
            "caracteres": int, número total de caracteres del fichero

    Ejemplo:
        >>> contar_basico("samples/ejemplo.txt")
        {'lineas': 7, 'palabras': 35, 'caracteres': 240}

    Plan por capas (sigue este orden, una idea cada vez):

        Capa 1: Abre el fichero con `with` y guarda todo el contenido
                en una variable `contenido`.

        Capa 2: Calcula el número de caracteres con `len(contenido)`.

        Capa 3: Calcula el número de palabras con `len(contenido.split())`.

        Capa 4: Calcula el número de líneas con `len(contenido.splitlines())`
                (o con `contenido.count("\\n")` si te resulta más claro).

        Capa 5: Devuelve un dict con los tres conteos.

    Pista:
        No intentes hacerlo todo de golpe. Escribe cada capa, ejecuta,
        y comprueba. Cuando las cinco estén, v0.1 está listo.
    """
    # Capa 1: apertura con `with` y lectura en una variable `contenido`.

    # Capa 2: número de caracteres.

    # Capa 3: número de palabras.

    # Capa 4: número de líneas.

    # Capa 5: return con el diccionario.

    pass  # <-- Reemplaza esto por tu implementación capa a capa.


# ============================================================================
# v0.2 y siguientes: NO TOCAR hasta cerrar v0.1
# ============================================================================


def top_palabras(ruta, n=5):
    """[v0.2 — DESPUÉS] Las n palabras más frecuentes del fichero."""
    pass


def medir_tiempo(funcion):
    """[v0.3 — DESPUÉS] Decorador que mide tiempo de ejecución."""
    pass


def analizar_fichero(ruta):
    """[v0.4 — DESPUÉS] Punto de entrada principal con try/except."""
    pass


def analizar_varios(*rutas):
    """[v0.5 — DESPUÉS] Procesa varios ficheros con *args."""
    pass


def exportar_informe(informe, ruta_salida):
    """[v0.6 — DESPUÉS] Escribe el informe en un fichero de salida."""
    pass


if __name__ == "__main__":
    # v0.1: este bloque solo comprueba que el archivo se importa sin errores.
    # Cuando cierres v0.1, puedes descomentar la línea siguiente para
    # hacer una prueba rápida con el sample incluido.
    #
    # print(contar_basico("samples/ejemplo.txt"))
    #
    # Más adelante (v0.4) aquí irá la llamada real a `analizar_fichero`.
    print("TextAnalyzer cargado. Completa v0.1 (contar_basico) para empezar.")

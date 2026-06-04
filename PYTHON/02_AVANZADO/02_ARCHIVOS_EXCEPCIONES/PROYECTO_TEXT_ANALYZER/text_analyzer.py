"""
TextAnalyzer
============

Esqueleto del proyecto integrador. Cada función está vacía (pass) y debe
completarse capa a capa siguiendo el plan del README.

Orden recomendado de trabajo:
    v0.1 -> v0.2 -> v0.3 -> v0.4 -> v0.5 -> v0.6
"""


def contar_basico(ruta):
    """
    v0.1

    Abre el fichero en `ruta` y devuelve un diccionario con:
        - "lineas":    numero de lineas (\n)
        - "palabras":  numero de palabras
        - "caracteres": numero total de caracteres del fichero

    Pistas:
        - Usa `with open(ruta, "r") as f: contenido = f.read()`.
        - "palabras" sale de `contenido.split()`.
        - "lineas" sale de `contenido.count("\n")` o de contar sobre
          `contenido.splitlines()`.
    """
    pass


def top_palabras(ruta, n=5):
    """
    v0.2

    Devuelve una lista con las `n` palabras mas frecuentes del fichero,
    ordenadas de mayor a menor frecuencia. Cada elemento es una tupla
    (palabra, frecuencia).

    Pistas:
        - Recorre las palabras y mete conteos en un dict.
        - Para ordenar por frecuencia de mayor a menor, usa
          `sorted(items, key=lambda x: x[1], reverse=True)`.
        - Devuelve los primeros `n` con slicing.
    """
    pass


def medir_tiempo(funcion):
    """
    v0.3

    Decorador que imprime cuanto tarda en ejecutarse la funcion decorada.
    Aplicalo a la funcion principal para ver el rendimiento en ficheros
    grandes.

    Pista:
        - Captura `inicio = time.time()` antes y `fin = time.time()` despues.
        - Imprime `f"Tiempo: {fin - inicio:.4f}s"`.
    """
    pass


def analizar_fichero(ruta):
    """
    v0.4

    Punto de entrada principal. Combina `contar_basico` y `top_palabras`
    en un informe legible por pantalla. Si el fichero no existe, captura
    `FileNotFoundError` y muestra un mensaje claro en vez de romper.

    Pista:
        - `try: ... except FileNotFoundError: print("Fichero no encontrado:", ruta)`
    """
    pass


def analizar_varios(*rutas):
    """
    v0.5

    Acepta varias rutas y devuelve una lista de informes, uno por fichero.
    Usa `*args` para recibirlas.
    """
    pass


def exportar_informe(informe, ruta_salida):
    """
    v0.6

    Escribe el informe (un string o un dict convertible) en `ruta_salida`
    usando `with open(ruta_salida, "w") as f:` y `f.write(...)`.
    """
    pass


if __name__ == "__main__":
    # Mientras el esqueleto este vacio, este bloque solo comprobara que
    # el archivo se ejecuta sin errores de sintaxis. Mas adelante, aqui
    # ira la llamada real a `analizar_fichero` con la ruta de un sample.
    print("TextAnalyzer - esqueleto cargado. Completa v0.1 para empezar.")

# Práctica de cierre — Recursividad


cache = {}


def fibonacci(indice):
    if indice <= 1:
        valor = indice

    else:
        valor = fibonacci(indice - 1) + fibonacci(indice - 2)

    cache[indice] = valor
    return valor

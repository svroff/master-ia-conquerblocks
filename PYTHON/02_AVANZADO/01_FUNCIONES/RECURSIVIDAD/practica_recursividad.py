from functools import lru_cache


@lru_cache(maxsize=None)
def factorial(num):
    if num == 1:
        valor = num
    else:
        valor = num * factorial(num - 1)
    return valor


print(factorial(10))

# Práctica de cierre — Recursividad


cache = {}


def fibonacci(indice):
    if indice <= 1:
        valor = indice

    else:
        valor = fibonacci(indice - 1) + fibonacci(indice - 2)

    cache[indice] = valor
    return valor

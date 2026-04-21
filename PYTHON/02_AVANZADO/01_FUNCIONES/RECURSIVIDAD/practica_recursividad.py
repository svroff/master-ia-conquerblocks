from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(num):

    if num == 1:
        valor = num
    else:
        valor = num * factorial(num - 1)
    return valor

print(factorial(10))
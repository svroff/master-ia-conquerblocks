from functools import lru_cache

@lru_cache
def factorial(num):
    if num == 0:
        return 1
    print(f'Calculo factorial({num})')
    resultado = num * factorial(num - 1)
    return resultado

print(factorial(5))
print(factorial(3))
print(factorial(6))

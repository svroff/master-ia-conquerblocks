# Objetivo: crear una función factorial(num) que use un diccionario llamado cache.

cache = {}
def factorial(num):
    if num in cache:
        print(f"Uso cache para {num}")
        return cache[num]
    
    if num == 0 or num == 1:
        cache[num] = 1
        return 1
    print(f"Calculo factorial({num})")
    resultado = num * factorial(num - 1)
    cache[num] = resultado
    return resultado

print(factorial(5))
print(cache)
print(factorial(7))
print(cache)

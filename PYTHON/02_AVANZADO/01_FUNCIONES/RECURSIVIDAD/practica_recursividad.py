cache = {}

def factorial(num):
    if num in cache:
        return cache[num]
    elif num == 1:
        valor = num
    else:
        valor = num * factorial(num - 1)
    cache[num] = valor
    return valor

print(factorial(5))
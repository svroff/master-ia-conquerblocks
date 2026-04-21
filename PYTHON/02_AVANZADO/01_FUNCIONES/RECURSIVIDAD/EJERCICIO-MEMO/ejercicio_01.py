# EJERCICIO 1 — Collatz con memoización
#
# El algoritmo de Collatz es una secuencia de transformaciones sobre un número entero.
# Partes de un número n y en cada paso lo transformas según estas reglas:
#   - Si n es par     → el siguiente número es n // 2        (ej: 6 → 3)
#   - Si n es impar   → el siguiente número es n * 3 + 1     (ej: 3 → 10)
#   - Cuando llegas a 1, paras. Ese es el caso base.
#
# Ejemplo paso a paso con n=6:
#   6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1   (8 pasos)
#
# Tu función NO devuelve el número transformado.
# Devuelve CUÁNTOS PASOS se necesitan para llegar a 1.
# Cada llamada recursiva cuenta como 1 paso — súmalos.
#
# Pista: caso base → collatz(1) devuelve 0 (ya estás en 1, cero pasos más).
#        caso recursivo → 1 + collatz(siguiente_número)
#
# Ejemplo: collatz(6) → 8
#          collatz(1) → 0

from functools import lru_cache

@lru_cache(maxsize=None)
def numero_collatz(num):
    if num == 1:
        valor = 0
    else:
        if num % 2 == 0:
            valor = 1 + numero_collatz(num // 2)
        else:
            valor =  1+ numero_collatz(num  * 3  + 1)
    return valor

print(numero_collatz(6))
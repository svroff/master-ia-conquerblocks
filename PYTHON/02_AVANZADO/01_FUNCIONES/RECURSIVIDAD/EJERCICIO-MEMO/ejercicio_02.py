# EJERCICIO 2 — Potencia con memoización
#
# Escribe una función recursiva con @lru_cache que calcule base^exponente.
#
# Ejemplo: potencia(2, 4) → 16   porque 2 * 2 * 2 * 2 = 16
#          potencia(3, 3) → 27   porque 3 * 3 * 3 = 27
#          potencia(5, 0) → 1    cualquier número elevado a 0 es siempre 1
#
# Cómo funciona la recursión:
#   potencia(2, 4) = 2 * potencia(2, 3)
#   potencia(2, 3) = 2 * potencia(2, 2)
#   potencia(2, 2) = 2 * potencia(2, 1)
#   potencia(2, 1) = 2 * potencia(2, 0)
#   potencia(2, 0) = 1  ← caso base, aquí paras
#
# En cada paso, el exponente baja en 1.
# Cuando el exponente llega a 0, devuelves 1 y la recursión se deshace.
#
# La función recibe dos parámetros: base y exponente.
from functools import lru_cache

@lru_cache(maxsize=None)
def potencia(base, exponente):
    if exponente == 0:
        valor = 1
    else:
        valor = base * potencia(base, exponente - 1)
    return valor

print(potencia(2,4))
# EJERCICIO 3 — Suma de dígitos con memoización
#
# Escribe una función recursiva con @lru_cache que sume todos los dígitos de un número.
#
# Ejemplo: suma_digitos(1234) → 10   porque 1 + 2 + 3 + 4 = 10
#          suma_digitos(999)  → 27   porque 9 + 9 + 9 = 27
#          suma_digitos(7)    → 7    ← caso base: un solo dígito, se devuelve tal cual
#
# Cómo funciona la recursión:
#   suma_digitos(1234) = 4 + suma_digitos(123)   ← el último dígito es 1234 % 10 = 4
#   suma_digitos(123)  = 3 + suma_digitos(12)    ← el último dígito es 123 % 10 = 3
#   suma_digitos(12)   = 2 + suma_digitos(1)
#   suma_digitos(1)    = 1  ← caso base, número de un solo dígito (menor que 10)
#
# Pistas:
#   - El último dígito de cualquier número se obtiene con: num % 10
#   - Para "quitar" el último dígito usas: num // 10
#   - El caso base es cuando el número es menor que 10 (ya es un solo dígito)

from functools import lru_cache

@lru_cache(maxsize=None)
def suma_digitos(digito):
    if digito > 10:
        valor = digito
    num = digito % 10
    num = num // 10
    return num

print(suma_digitos(1234))
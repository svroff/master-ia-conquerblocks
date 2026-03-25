"""
Enunciado:
Escribe una función recursiva factorial(n) que calcule el factorial de un número.
El factorial de un número es la multiplicación de todos los números desde 1 hasta ese número:

factorial(5) → 120 (porque 5×4×3×2×1 = 120)
factorial(3) → 6 (porque 3×2×1 = 6)
factorial(1) → 1
"""


def factorial(n):
    print(n)
    if n == 1:
        return 1
    return n * factorial(n - 1)


resultado = factorial(5)
print(resultado)

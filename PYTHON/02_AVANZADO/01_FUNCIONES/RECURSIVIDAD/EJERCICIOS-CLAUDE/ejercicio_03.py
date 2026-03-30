"""
Enunciado:
Escribe una función recursiva potencia(base, exponente) que calcule la potencia de un número sin usar el operador ** de Python.

potencia(2, 3) → 8 (porque 2×2×2)
potencia(3, 4) → 81 (porque 3×3×3×3)
potencia(5, 0) → 1 (ojo con este caso base 👀)

Pista: potencia(2, 3) es lo mismo que 2 * potencia(2, 2). ¿Ves el patrón? ¿Y cuándo paras?
"""


def potencia(base, exponente):
    if base < 0 or exponente < 0:
        return "error"
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)


resultado = potencia(3, 4)

print(resultado)

# Vamos con potencia usando @lru_cache, despacio.

# Queremos calcular esto:
# potencia(2, 4) = 2 * 2 * 2 * 2 = 16

from functools import lru_cache

@lru_cache
def potencia(base, exponente):
    if exponente == 0:
        return 1

    print(f"Calculo {base}^{exponente}")
    resultado = base * potencia(base, exponente - 1)
    return resultado

print(potencia(2, 4))
print(potencia(2, 3))
print(potencia(2, 5))
print(potencia(3, 3))

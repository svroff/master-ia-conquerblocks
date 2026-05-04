# Vamos con potencia con memoización manual, despacio.

# Queremos calcular esto:
# potencia(2, 4) = 2 * 2 * 2 * 2 = 16
cache = {}
def potencia(base, exponente):
    if (base, exponente) in cache:
        print(f"Uso cache para {base}^{exponente}")
        return cache[(base, exponente)]
    
    if exponente == 0:
        cache[(base, exponente)] = 1
        return 1
    
    print(f"Calculo {base}^{exponente}")
    resultado = base * potencia(base, exponente - 1)
    cache[(base, exponente)] = resultado
    return resultado

print(potencia(2, 4))
print(cache)

# 1. Define la función aquí
def calcular_total(precio, iva = 21):
    return precio + (precio * iva / 100)

# 2. Pruebas (Descomenta para probar)
precio_final = calcular_total(100)       # Debería dar 121
print(f"El precio es: {precio_final}")

precio_reducido = calcular_total(100, 10) # Debería dar 110 (IVA del 10%)
print(f"El precio reducido es: {precio_reducido}")
# Enunciado:
# Escribe una función recursiva suma_hasta(n) que dado un número n, devuelva la suma de todos los números desde 1 hasta n.
# Por ejemplo:

# suma_hasta(5) → devuelve 15 (porque 1+2+3+4+5 = 15)
# suma_hasta(3) → devuelve 6 (porque 1+2+3 = 6)
# ---------------------------------------------------------------------------------------------


# Creamos función recursiva
def suma_hasta(n):
    print(n)
    if n == 1:
        return 1
    return n + suma_hasta(n - 1)


resultado = suma_hasta(6)
print(f"Devuelve {resultado}")

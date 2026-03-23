# Paso 1: una función normal (sin recursividad)
# Paso 2: la misma cuenta atrás pero recursiva
def cuenta_atras(n):
    print(n)
    if n == 1:  # caso base: para aquí
        return
    cuenta_atras(n - 1)  # la función se llama a sí misma


cuenta_atras(5)

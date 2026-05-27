def decorador(funcion_original):
    def wrapper(*args, **kwargs):
        print("Antes de ejecutar la función")
        resultado = funcion_original(*args, **kwargs)
        print("Después de ejecutar la función")
        return resultado

    return wrapper


def decorador_corto(funcion_original):
    def wrapper(*args, **kwargs):
        print("Ejecutando función...")
        return funcion_original(*args, **kwargs)

    return wrapper


@decorador
def sumar(a, b):
    return a + b


@decorador_corto
def multiplicar(a, b):
    return a * b


resultado = sumar(2, 3)
resultado_corto = multiplicar(2, 3)
print("Resultado guardado: ", resultado)
print("Resultado corto: ", resultado_corto)

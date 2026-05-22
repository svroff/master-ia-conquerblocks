def decorador(funcion_original):
    def wrapper(*args, **kwargs):
        print("Antes de ejecutar la función")
        resultado = funcion_original(*args, **kwargs)
        print("Después de ejecutar la función")
        return resultado

    return wrapper


@decorador
def sumar(a, b):
    return a + b


resultado = sumar(2, 3)
print("Resultado guardado: ", resultado)

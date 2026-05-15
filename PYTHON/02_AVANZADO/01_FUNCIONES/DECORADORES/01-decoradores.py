def decorador(funcion_original):
    def wrapper():
        print("Antes")
        funcion_original()
        print("Después")

    return wrapper


@decorador
def saludar():
    print("Hola Sergi!")


saludar()

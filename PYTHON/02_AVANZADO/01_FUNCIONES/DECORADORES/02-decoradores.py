def mostrar_inicio_fin(funcion_original):
    def wrapper(*args, **kwargs):
        print("Inicio de función")
        funcion_original(*args, **kwargs)
        print("Fin de función")

    return wrapper


@mostrar_inicio_fin
def aprender(nombre="Sergi"):
    print(f"Estoy aprendiendo decoradores, mi nombre es: {nombre}")


aprender()

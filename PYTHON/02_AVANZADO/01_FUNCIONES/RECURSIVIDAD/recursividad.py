def fibonacci(indice):
    # print(f"Calculando fibonacci({indice})")
    if indice <= 1:
       # print(f"Caso base: devuelvo {indice}")
        return indice
    resultado = fibonacci(indice - 1) + fibonacci(indice - 2)
    print(f"fibonacci({indice}) = {resultado}")
    return resultado


fibonacci(8)

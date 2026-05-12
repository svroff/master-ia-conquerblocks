def suma_digitos(numero):
    if numero == 0:
        return 0
    
    ultimo_digito = numero % 10
    resto_numero = numero // 10

    print(f"Numero actual: {numero}")
    print(f"Ultimo digito: {ultimo_digito}")
    print(f"Resto numero: {resto_numero}")

    return ultimo_digito + suma_digitos(resto_numero)


print(suma_digitos(9876))

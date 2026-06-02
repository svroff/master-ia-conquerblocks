try:
    texto = open("fichero-test.txt", "rb")
    fichero = texto.read()
    print(fichero)
    fichero = texto.close()
except FileNotFoundError:
    print("ha habido un error, fichero no existe.")

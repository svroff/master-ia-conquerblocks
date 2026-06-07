try:
    texto = open("fichero-test.txt", "rb")
    fichero = texto.read()
    print(fichero)
    fichero = texto.close()
except FileNotFoundError:
    print("ha habido un error, fichero no existe.")

try:
    copia =open("copia.bin", "wb")
    copia.write(fichero)
    copia.close()
except:
    print("ha habido un error, no se ha podido copiar el fichero.")
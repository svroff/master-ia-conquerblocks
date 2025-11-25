'''
Crea un programa en el que se pregunte al usuario por una frase y una letra, y muestre por 
pantalla el número de veces que aparece la letra en la frase.
'''

# pedimos la frase y la letra
frase = input('Escribe una frase: ')
letra = input('Escribe una letra: ')
contador_de_letras = 0 # aquí iremos almacenando cuántas veces sale la letra que queremos

# lógica del for. si el iterador es igual a la letra, sumas 1 al contador de letras.
for i in frase:
    if i == letra:
        contador_de_letras += 1

# print final.
print('La letra ', letra, ' se encuentra ', contador_de_letras, ' veces.')
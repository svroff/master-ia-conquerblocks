''' 
Crea un script que pida al usuario una palabra y luego muestre por pantalla una a una las letras 
de la palabra introducida empezando por la última. 
'''

# pedimos la palabra
palabra = input("Dime una palabra: ").upper()

# usamos un bucle for pero utilizamos la posición ::-1 que lo que hace es invertir el orden.
for letra in palabra[::-1]:
    print(letra)
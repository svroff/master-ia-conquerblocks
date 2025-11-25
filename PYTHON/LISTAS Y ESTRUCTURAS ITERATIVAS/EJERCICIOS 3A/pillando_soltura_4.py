# 4. Crea un script que cuente el número de elementos más grandes que un determinado número dado por el usuario (supón una lista numérica). 
lista_numeros = [5,6,2,34,56,65,23,423,123,5456,23]
lista_mayores = []
# pido numero
numero_consola = int(input('Dime un numero: '))

for n in lista_numeros:
    if n > numero_consola:
        lista_mayores.append(n)

contador_numeros = len(lista_mayores)        
print('Hay ', contador_numeros, " numeros más grandes que ", numero_consola)
print('Los numeros son: ', lista_mayores)
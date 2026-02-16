# 6. Escribe un script que pida un número al usuario y dada una lista encuentre el número más alto que es inferior al número introducido o determinado al inicio del programa. 

lista_numeros = [5,6,2,34,56,65,23,423,123,5456,23]
lista_menores = []
# pido numero
numero_consola = int(input('Dime un numero: '))



if numero_consola < 0 or numero_consola == 0:
    print('Indica un numero mayor a 0')
else:
    for n in lista_numeros:
        if n < numero_consola:
            lista_menores.append(n)
    
    if lista_menores:
        numero_mayor = max(lista_menores)
        print('Los números inferiores a', numero_consola, 'son', lista_menores)
        print('El número más alto pero inferior a', numero_consola, 'es', numero_mayor)
    else:
        print('No hay números menores que', numero_consola)

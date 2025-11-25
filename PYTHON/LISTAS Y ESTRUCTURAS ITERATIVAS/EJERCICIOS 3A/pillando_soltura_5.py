# 5. Crea un script que, dado un número introducido por el usuario o determinado al inicio del programa, realice la suma de aquellos números que sean divisibles por este. 

lista_numeros = [5,6,2,34,56,65,23,423,123,5456,23]
numeros_divisibles = []
numero_consola = int(input(' Dime un numero: '))

if numero_consola == 0:
        print('No se puede dividir entre 0')
else:       
    for n in lista_numeros:   
        if n % numero_consola == 0:
            numeros_divisibles.append(n)
    

    suma_total = sum(numeros_divisibles)
    print('Los numeros divisibles entre ', numero_consola, ' de la lista son')
    print(numeros_divisibles)
    print('Y la suma total de estos numeros es ', suma_total)
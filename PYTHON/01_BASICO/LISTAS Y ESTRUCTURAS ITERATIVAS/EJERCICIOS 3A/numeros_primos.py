'''
Crea un programa que imprima todos los números primos entre el 2 y el 100. Un numero primo es 
un numero positivo y entero mayor que uno que no tiene un divisor positivo y entero que no sea 1 
o sí mismo.
'''

# creamos una lista dónde iremos añadiendo los números.
lista_numeros_primos = []
# creamos una variable numero simbolica.
numero = 2


while numero <= 100:
    es_primo = True    # creamos una variable boleana para determinar si es o no.
    for i in range(2, numero):
        if numero % i == 0: # si hay algun divisor por tanto ya no es primo.
            es_primo = False
            break # salimos del bucle
    if es_primo:
        lista_numeros_primos.append(numero) # y lo añadimos.
    numero += 1 # sumamos uno para que el bucle while vuelva a empezar, hemos hecho un break del bucle for

print(lista_numeros_primos)
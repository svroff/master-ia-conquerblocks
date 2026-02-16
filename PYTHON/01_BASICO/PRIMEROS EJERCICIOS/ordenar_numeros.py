'''

Crea un script en el que el usuario introduzca un número de más de una cifra. 
El script debe imprimir los componentes del número uno a uno por pantalla. 
Por ejemplo si el número introducido es el 4532 por pantalla deberá imprimirse:

4
5
3
2

Crea un script que dado un numero entero de cuatro cifras calcula e imprima el número
que resulta de leer el número introducido de derecha a izquierda. 
Por ejemplo si el número introducido
es 4532, el output deberá ser 2354.

'''

numero = input('Dime un número: ')
for n in numero:
    print(n)
    
print('-----')

numero_invertido = numero[::-1]
print(numero_invertido)
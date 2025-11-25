'''
Crea un script que dado un número y una potencia compruebe si ese numero elevado a esa
potencia es par o impar. (Pista: los números pares tiene resto = 0 al dividirlos por 2)
'''

# pedimos número
valor = int(input('Dime un número: '))
potencia = int(input('Dime a cuánto quieres elevarlo(potencia): '))

# calculamos
valor_elevado = valor**potencia

# comprobamos si es par o impar
if valor_elevado % 2 == 0:
    print(valor_elevado, ' es par')
else:
    print(valor_elevado, ' es impar')

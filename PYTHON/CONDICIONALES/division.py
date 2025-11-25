'''
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el
divisor es cero el programa debe mostrar un error.
'''

# pedimos numeros en enteros
primer_numero = int(input('Dime un numero: '))
segundo_numero = int(input('Dime otro numero: '))

# hacemos la comprobacion y dividimos
if segundo_numero == 0:
    print('uno de los dos números no debe ser 0 para hacer la division')
else:
    division = primer_numero / segundo_numero
    print('La division de ', primer_numero, ' entre ', segundo_numero, ' es ', division)

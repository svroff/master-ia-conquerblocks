'''
RELACION ENTRE NÚMEROS:
Crea un script que pida al usuario 3 números diferentes y le indique si alguno de ellos es la suma 
de los otros dos.
'''

# pedimos numeros
primer_valor = int(input('Primer numero: '))
segundo_valor = int(input('Segundo numero: '))
tercer_valor = int(input('Tercer numero: '))

# comparamos las sumas y las variables para determinar si uno de los numeros es la suma de los otros dos.
if primer_valor + segundo_valor == tercer_valor:
    print('El ', tercer_valor, " es la suma de ", primer_valor, ' y ' ,segundo_valor)
elif primer_valor + tercer_valor == segundo_valor:
    print('El ', segundo_valor, " es la suma de ", primer_valor, ' y ' ,tercer_valor)
elif segundo_valor + tercer_valor == primer_valor:
    print('El ', primer_valor, " es la suma de ", segundo_valor, ' y ' ,tercer_valor)
else:
    print('Ninguno es la suma de ninguno')
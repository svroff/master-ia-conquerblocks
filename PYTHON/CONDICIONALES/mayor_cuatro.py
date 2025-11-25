'''
EL MAYOR DE CUATRO:
Crea un script que pida al usuario 4 números diferentes y imprima el mayor de los cuatro por 
pantalla.
'''

# pedimos los 4 numeros diferentes
primer_valor = int(input('Primer numero: '))
segundo_valor = int(input('Segundo numero: '))
tercer_valor = int(input('Tercer numero: '))
cuarto_valor = int(input('Cuarto numero: '))

# comparamos
if primer_valor > segundo_valor and primer_valor > tercer_valor and primer_valor > cuarto_valor:
    print(primer_valor, ' es el mayor')
elif segundo_valor > primer_valor and segundo_valor > tercer_valor and segundo_valor > cuarto_valor:
    print(segundo_valor, ' es el mayor')
elif tercer_valor > primer_valor and tercer_valor > segundo_valor and tercer_valor > cuarto_valor:
    print(tercer_valor, ' es el mayor')
else:
    print(cuarto_valor, ' es el mayor')
'''
EL TRIÁNGULO:
En una obra es necesario construir para el tejado de una casa una estructura triangular con tres 
piezas. El ingeniero se pregunta si dadas la largura de las piezas que ha recibido podrá construir 
esta estructura. Crea un script que dados tres longitudes indique si podría construirse un triangulo 
con esas piezas.
(Pista: la suma de dos piezas tiene que ser mayor que el lado restante. Esto debe ser así para 
todas las posibles combinaciones)
'''

# pedimos las longitudes
a = int(input('Primer numero: '))
b = int(input('Segundo numero: '))
c = int(input('Tercer numero: '))

# la suma de dos piezas tiene que ser mayor que el lado restante. Esto debe ser así para todas las posibles combinaciones

# las tres desigualdades deben cumplirse a la vez
if (a + b > c) and (a + c > b) and (b + c > a):
    print('Se podrá construir')
else:
    print('No se podrá construir')

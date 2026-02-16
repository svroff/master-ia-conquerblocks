'''
Un ordenador tiene tres usuarios distintos (Alejandro, Naomi y Sergio) y otro usuario invitado.
Haz un script que pida el nombre al usuario y le dé una bienvenida personalizada. Crea el script
de tal manera que si el usuario no es ninguno de los tres se le dé un saludo genérico.
¿Que ocurre si uno de los usuarios introduce su nombre completamente en minúsculas?¿Y si lo
introduce en mayúsculas? ¿Y si sin querer pone in punto en mitad de su nombre (p.e. nao.mi)?¿Y
si se le cuela una almohadilla (p.e se#rgio)?
'''

# Definimos los usuarios predefinidos
alejandro = 'Alejandro'
naomi = 'Naomi'
sergio = 'Sergio'

# Pedimos el nombre al usuario
invitado = input('Dime tu nombre: ')

# Nos aseguremos que esté bien escrito
invitado = invitado.replace(".", "")
invitado = invitado.replace("#", "")

# Analizamos si coincide con alguno de los predefinidos
if(invitado.title() == alejandro or invitado.title() == naomi or invitado.title() == sergio):
    print('Bienvenido ', invitado.title(), ' !!')
else:
    print('Bienvenido Invitado')
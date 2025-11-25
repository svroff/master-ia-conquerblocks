'''
Crea un script que pida una contraseña al usuario (el script sabe cual es la contraseña correcta). 
Si la contraseña es correcta el script debe darle la bienvenida al usuario. De lo contrario debe 
indicarle que la contraseña es incorrecta y darle una segunda oportunidad de introducir la 
contraseña. Al segundo fallo debe mostrar un mensaje de error y terminar de ejecutarse.
Cambia el script para que no distinga entre mayúsculas y minúsculas.

(Pista: Necesitarás in If Statement anidado)

'''
# definimos la contraseña
passwd = 'password'

# pedimos contraseña
passwd_user = input('Introduce la contraseña: ')

# evaluamos
if passwd_user.lower() != passwd.lower():
    # creamos una segunda variable para el segundo intento
    passwd_segundo_intento = input('Contraseña incorrecta, vuelva a intentarlo: ')
    if passwd_segundo_intento.lower() != passwd.lower():
        print('Contraseña incorrecta')
    else:
        print('Contraseña correcta, bienvenido')
else:
    print('Contraseña correcta, bienvenido')
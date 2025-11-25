'''
CONTRASEÑA SEGURA:
Por motivos de seguridad una contraseña debe tener una vocal en minúscula, dos símbolos
especiales diferentes (pueden ser solo * o #). Dada una contraseña ingresada por el usuario,
comprueba si es una contraseña segura e indícalo por pantalla.
'''

# Pedimos una contraseña al usuario
passwd = input('Introduce una contraseña: ')

# Verificamos si tiene * y #
if '#' in passwd and '*' in passwd:
    if 'a' in passwd or 'e' in passwd or 'i' in passwd or 'o' in passwd or 'u' in passwd:
        print('ok')
    else: 
        print('mec')

    

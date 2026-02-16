'''
2. Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
'''

# creamos la variable con "contraseña"

passwd = "contraseña"
passwd_consola = input('Dime la contraseña: ')

while(passwd_consola.lower() != passwd.lower()):
    print('¡¡ Contraseña incorrecta !!')
    passwd_consola = input('Dime la contraseña: ')
    if passwd_consola.lower() == passwd.lower():
        print("¡¡ Contraseña Correcta !!")
# ==========================================
# EJERCICIO 3: CONTRASEÑA SEGURA (Parte 2: Creador)
# ==========================================
# Crea otro script creador.py con una función llamada generar_contrasena
# que genere contraseñas seguras de forma aleatoria.
#
# La función debe permitir especificar la longitud de la contraseña y
# qué tipos de caracteres deben incluirse (por ejemplo, letras mayúsculas,
# letras minúsculas, números y caracteres especiales).
#
# (Nota del PDF: Para el generador de contraseñas puedes probar a usar
# los modulos random y string).

print("\n--- EJERCICIO 3: CREADOR DE CONTRASEÑAS ---")

import string
import random


# Tu código aquí:
def password_generator(length):
    digits = string.ascii_letters + string.digits + string.punctuation

    passwd = ""

    for _ in range(length):
        caracter = random.choice(digits)
        passwd += caracter

    return passwd


len_input = int(input("De cuántos caracteres quieres la password? "))
password_generada = password_generator(len_input)
print(f"Tu nueva clave es {password_generada}")

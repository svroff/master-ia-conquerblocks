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
mi_palabra = ""

letras = string.ascii_letters  # "abcdef...XYZ"
numeros = string.digits  # "0123456789"
simbolos = string.punctuation  # "!#$%&/()..."

for l in letras:
    l = random.choice(letras)
    print(l)

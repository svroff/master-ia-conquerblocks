# primer ejercicio
nombre = input("Cómo te llamas? ")
nombre = nombre.strip().lower().capitalize().replace('.', '')
output = '¡Hola, ' + nombre + ', estás usando Python!'
print(output)

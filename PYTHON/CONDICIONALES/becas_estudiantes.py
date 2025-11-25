'''
BECAS PARA ESTUDIANTES (BONUS*):
El gobierno quiere otorgar becas de excelencia a los estudiantes con un mínimo de un 8 de media. 
Además para acceder a la beca el estudiante debe tener entre 17 y 21 años. Crea un script que 
pida el nombre, la edad y la nota media del estudiante e indique si puede optar a la beca o no.
*Los ejercicios bonus no se resolverán directamente en clase si no que están pensados para que 
los alumnos los discutan por el chat de Discord y compartan sus soluciones. Las soluciones 
compartidas de los alumnos se subirán en un archivo a la academia.
'''

# creamos variables
nombre = input('Nombre del alumno: ')
edad = int(input('Edad: '))
nota_media = int(input('Nota media: '))

if nota_media >= 8 and edad >= 17 and edad < 21:
    print('Puede acceder a la beca')
else:
    print('No cumple alguno de los requisitos. Debe de tener mínimo un 8 de media y entre 17 y 21 años.')
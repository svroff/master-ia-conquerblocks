'''
BASE DE DATOS DE UN COLEGIO: 
Trabajas en colegio y estas encargado de mantener un seguimiento de las notas de los 
estudiantes de un clase. En tu base de datos tienes una lista con los nombres de los estudiantes y 
para cada estudiante debes guardar sus notas provenientes de deberes, exámenes y proyectos. 
También necesitas calcular a nota media de cada estudiante y la nota media de la clase al 
completo. 
Pista: Para resolver este problema puedes usar una lista anidada donde guardes las notas para 
cada estudiante. Entonces puedes usar un bucle para recorrer la lista de listas y calcular la nota 
media de cada estudiante. También puedes usar otro bucle para calcular la nota media de toda la 
clase. 
'''

# lista con los nombres de los estudiantes
estudiantes = ['Andrea', 'Sergio', 'Adri']

# creamos la bbdd dónde iremos, con un bucle for, metiendo datos.
base_de_datos_estudiantes = []
nota_media_de_cada_estudiante = 0 
nota_media_estudiantes = []
media_clase = 0

# creamos el bucle for donde iterará por estudiantes
for estudiante in estudiantes:
    # creamos las notas para introducirlas manualmente.
    notas = []
    # creamos la variable nota_media para calcularla por estudiante

    
    print(f'Introduce las notas de {estudiante} ')
    deberes = int(input('Deberes: '))
    notas.append(deberes)
    examenes = int(input('Examenes: '))
    notas.append(examenes)
    proyectos = int(input('Proyectos: '))
    notas.append(proyectos)
    
    # bucle de dónde sacaremos la media
    for n in notas:
        nota_media_de_cada_estudiante = sum(notas) / len(notas)
    
    nota_media_estudiantes.append(nota_media_de_cada_estudiante)
    
    # la printamos dentro del bucle para que lo haga después de cada estudiante.  
    print(f'La nota media de {estudiante} es: {nota_media_de_cada_estudiante}')
    
    # introducimos las notas en la bbdd de estudiantes, sino, sólo tendremos las notas del último alumno.
    base_de_datos_estudiantes.append([estudiante, notas])

# nota media de todos los estudiantes
media_clase = sum(nota_media_estudiantes) / len(nota_media_estudiantes)
# nota_media_estudiantes = sum(nota_media_estudiantes) / 3

print(f'La nota media total, de la clase, es de {media_clase}')

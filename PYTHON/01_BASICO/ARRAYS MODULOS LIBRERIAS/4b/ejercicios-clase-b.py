import numpy as np

'''
CALCULO DE NOTAS FINALES
Supongamos que tienes un conjunto de calificaciones de un grupo de estudiantes en un
curso. 
Cada estudiante tiene cuatro calificaciones: dos exámenes, un trabajo final y una participación en clase. Quieres calcular la nota final de cada estudiante, donde los exámenes valen un 30% cada uno, el trabajo final vale un 30% y la participación en clase vale un 10%. 
Para ello, puedes usar NumPy para crear un array de 4 columnas y n filas, donde n es el número de estudiantes. Cada columna representa una de las calificaciones y cada fila representa un estudiante. Luego, puedes usar operaciones de NumPy para calcular la nota final de cada estudiante y almacenarla en un nuevo array de una sola columna.
'''


'''
# cada estudiante tiene cuatro calificaciones, dos exámenes, un trabajo final y una participacion. --> 4 columnas. N filas (por estudiante)
arr_notas = np.array([
    (8,7,9,6), 
    (7,7,8,5), 
    (9,9,8.7,9)], dtype=np.float16)

# hay que calcular la nota final. 30% cada examen, 30% trabajo final, 10% participación
# creamos como lo vamos a ponderar con otro array
arr_peso_notas = np.array([0.30, 0.30, 0.30, 0.10], dtype=np.float16)

# usamos la funcion dot que multiplica elemento por elemento y luego suma todo.
arr_nota_final = np.dot(arr_notas, arr_peso_notas)

# almacenarla en un nuevo array de una sola columna
arr_nota_final = arr_nota_final.reshape((3, 1))

print(arr_nota_final)
'''



# 1. Crea un script que pida los tiempos por pantalla para cada uno de los finalistas 
tiempo_hannah  = input('Tiempo Hannah: ')
'''tiempo_jackie = input('Tiempo Jackie: ')
tiempo_bos = input('Tiempo Bos: ')'''

# 2. Convierte los tiempos de minutos-segundos-centésimas a segundos
hannah_minutos, hannah_segundos, hannah_centesimas = tiempo_hannah.split(' ')
'''jackie_minutos, jackie_segundos, jackie_centesimas = tiempo_jackie.split(' ')
bos_minutos, bos_segundos, bos_centesimas = tiempo_bos.split(' ')'''

hannah_segundos = (int(hannah_minutos) * 60) + int(hannah_segundos) + (int(hannah_centesimas) * 0.01)
print('Hannah ha hecho: ', hannah_segundos, ' segundos')

# 3. Sabiendo que la pista es de 100 metros calcula la velocidad media de cada uno de ellos en
# metros por segundo. 

velocidad_media = 100 / hannah_segundos

# 4. Imprime los resultados por pantalla
print('Hannah ha recorrido la pista en ', velocidad_media, ' m/s')
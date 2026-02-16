'''


DECLARACION DE LA RENTA:

Para tributar en un determinado país es necesario ser mayor de edad y cobrar más de 1000 euros 
al mes. Además los tramos impositivos de la renta anual son los siguientes:

RENTA                       TIPO IMPOSITIVO
Menos de 15.000 eu              5%
Entre 15.000 y 25.000 eu        15%
Entre 25.000 y 35.000 eu        20%
Entre 35.000 y 60.000 eu        30%
Más de 60.000 eu                45%
 
Escribe un script que primero compruebe si eres susceptible de que se te aplique algún tipo 
impositivo y en caso afirmativo imprima por pantalla cuál te tocaría.


'''

mayor_edad = int(input('Cuántos años tienes? '))


if mayor_edad < 18:
    print('Eres menor de edad, por tanto, no puedes trabajar')
else:  
    sueldo = float(input('Cuánto cobras ? '))  
    if sueldo < 15000:
        print('Te toca pagar un 5%')
    elif sueldo >= 15000 and sueldo < 25000:
        print('Te toca pagar el 15%')
    elif sueldo >= 25000 and sueldo < 35000:
        print('Te toca pagar el 20%')
    elif sueldo >= 35000 and sueldo < 60000:
        print('Te toca pagar el 30%')
    else:
        print('Te toca pagar el 45%')

    
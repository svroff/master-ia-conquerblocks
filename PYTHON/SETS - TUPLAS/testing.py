"""sospechosos = ["Mr. Robot", "Trinity", "Agent Smith"]
niveles_peligro = [5, 2, 10]

for s, n in zip(sospechosos, niveles_peligro):

    if n >= 10:
        print(f"El sujeto {s} tiene el nivel {n}.¡AMENAZA CRÍTICA DETECTADA!")
    else:
        print(f"El sujeto {s} tiene el nivel {n}.")"""

numeros = [1, 2, 2, 3, 4, 4, 5]
# Convierte esa lista en un Set para borrar los duplicados.
set_num = set(numeros)
print(type(set_num))

list_num = list(set_num)
print(type(list_num))
print(list_num)

list_num_mult = []

for n in list_num:
    n = n * 10
    list_num_mult.append(n)

print(list_num_mult)
list_num_mult_lambda = list(map(lambda n: n * 10, list_num))
print(list_num_mult_lambda)
# "Multiplica n por 10 PARA cada n EN list_num"
resultado = [n * 10 for n in list_num]
temps = [15, 30, 12, 40, 35, 10]
alertas = [n for n in temps if n >= 30]
notas = [3, 8, 10, 4, 6]
aprobados = ["Aprobado" if n >= 5 else "Suspendido" for n in notas]
print(aprobados)

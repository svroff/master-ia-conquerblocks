sospechosos = ["Mr. Robot", "Trinity", "Agent Smith"]
niveles_peligro = [5, 2, 10]

for s, n in zip(sospechosos, niveles_peligro):

    if n >= 10:
        print(f"El sujeto {s} tiene el nivel {n}.¡AMENAZA CRÍTICA DETECTADA!")
    else:
        print(f"El sujeto {s} tiene el nivel {n}.")

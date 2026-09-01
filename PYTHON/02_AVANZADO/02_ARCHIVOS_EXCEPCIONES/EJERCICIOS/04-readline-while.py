with open("fichero-test.txt", "r") as f:
    n = 1
    while True:
        linea = f.readline()
        if linea == "":
            break
        print(f"{n}: {linea.strip()}")
        n += 1
with open("fichero-test.txt", "r") as b:
    lineas = b.readlines()
    print(type(lineas))
    print(len(lineas))
    print(lineas[0])
    print(lineas)

with open(
    "fichero-test.txt",
    "w",
) as f:
    f.write("Primera línea del archivo.")

with open(
    "fichero-test.txt",
    "a",
) as f:
    f.write("\nSegunda línea del archivo.\n")

with open(
    "fichero-test.txt",
    "r",
) as f:
    for linea in f:
        print(linea.strip())

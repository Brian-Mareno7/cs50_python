f = open("alumnos.txt", "r")

conteo_gryffindor = 0

for linea in f:
    datos = linea.strip()
    linea = datos.split(" - ")
    print(linea[1])
    if linea[1] == "Gryffindor":
        conteo_gryffindor = conteo_gryffindor + 1


f.close()
print(conteo_gryffindor)
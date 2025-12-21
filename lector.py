archivo = open("alumnos.txt", "r") 

conteo_gryffindor = 0

for linea_sucia in archivo:
    linea_limpia = linea_sucia.strip()
    lista_datos = linea_limpia.split(" - ")

    casa_actual = lista_datos[1]
    
    if casa_actual == "Gryffindor":
        conteo_gryffindor = conteo_gryffindor + 1

archivo.close()
print("Total de leones:", conteo_gryffindor)
def obtener_casa(linea):
    linea_limpia = linea.strip()
    linea_datos = linea_limpia.split(" - ")
    return linea_datos [1]
    
archivo = open("alumnos.txt", "r") 

conteo_gryffindor = 0

for lineas in archivo:
    casa = obtener_casa(lineas)
    
    if casa == "Gryffindor":
        conteo_gryffindor = conteo_gryffindor + 1

archivo.close()
print("Total de leones:", conteo_gryffindor)
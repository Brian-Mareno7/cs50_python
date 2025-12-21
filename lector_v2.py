# --- PASO 1: PREPARACIÓN ---
# Abrimos el archivo solo para leer ("r").
# Imagina que sacas el libro de la estantería.
archivo = open("alumnos.txt", "r") 

# Creamos el contador fuera del bucle.
# IMPORTANTE: Si lo pones dentro, se reiniciaría a 0 con cada alumno.
conteo_gryffindor = 0

# --- PASO 2: EL BUCLE (PROCESAMIENTO) ---
# "for linea in archivo" lee el texto renglón por renglón automáticamente.
for linea_sucia in archivo:
    
    # A. LIMPIEZA
    # La variable 'linea_sucia' tiene el salto de línea (\n) invisible.
    # Usamos .strip() para quitarlo y guardamos el resultado en una variable nueva.
    linea_limpia = linea_sucia.strip() 
    
    # B. CORTE (La tijera)
    # Cortamos el texto donde haya un guion.
    # Esto convierte el texto "Harry - Gryffindor" en la lista ["Harry", "Gryffindor"]
    lista_datos = linea_limpia.split(" - ")
    
    # C. SELECCIÓN
    # Queremos analizar solo la casa. La casa está en la posición 1 de la lista.
    # (Posición 0 es el nombre, Posición 1 es la casa).
    casa_actual = lista_datos[1]
    
    # D. DECISIÓN
    # Preguntamos: ¿La casa de este alumno específico es Gryffindor?
    if casa_actual == "Gryffindor":
        # Si es SÍ, sumamos 1 a nuestro contador general.
        # (+= 1 es una forma corta de decir "lo que tenías + 1")
        conteo_gryffindor += 1

# --- PASO 3: CIERRE ---
# Es importante cerrar el archivo para liberar la memoria de la computadora.
archivo.close()

# Finalmente, mostramos el resultado total.
print("Total de leones:", conteo_gryffindor)
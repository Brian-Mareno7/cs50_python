# 1. Abrimos el archivo en modo 'a' (append) para no borrar lo anterior
f = open("lista_hogwarts.txt", "a")

# 2. Escribimos algo dentro.
# IMPORTANTE: \n significa "salto de línea" (Enter), sino escribe todo pegado.
f.write("Harry Potter - Gryffindor\n")

# 3. Cerramos el archivo para guardar cambios.
f.close()
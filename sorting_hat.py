#ejercicio 1
import random
import time

casas = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw" ]

cualidad={ "Valiente": "Gryffindor",
        "Astuto": "Slytherin",
        "Leal": "Hufflepuff",
        "Sabio": "Ravenclaw"}

while True:
    nombre = input("Ingresa tu nombre :")
    respuesta = input("Qué cualidad prefieres? (Valiente/Astuto/Leal/Sabio) ").lower()

    if respuesta == "salir":
        print("Travesura realizada")
        break

    print("El sombrero está pensando")
    
    time.sleep(2)

    if respuesta == "valiente":
        casa = (cualidad["Valiente"])
    elif respuesta == "astuto":
        casa = (cualidad["Astuto"])
    elif respuesta == "leal":
        casa =(cualidad["Leal"])
    elif respuesta == "sabio":
        casa =(cualidad["Sabio"])   
    elif respuesta == "no se":
        casa = (random.choice(casas))
    else: 
        casa = ("¡Eres un muggle!")
    
    f = open("alumnos.txt", "a")
    f.write(nombre + " - " + casa + "\n")
    f.close()
    print(nombre + " - " + casa + "\n")
#ejercicio 1
import random
import time

casas = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw" ]

cualidad={ "Valiente": "Gryffindor",
        "Astuto": "Slytherin",
        "Leal": "Hufflepuff",
        "Sabio": "Ravenclaw"}

while True:
    respuesta = input("Qué cualidad prefieres? (Valiente/Astuto/Leal/Sabio) ").lower()

    if respuesta == "salir":
        print("Travesura realizada")
        break

    print("El sombrero está pensando")
    
    time.sleep(2)

    if respuesta == "valiente":
        print(cualidad["Valiente"])
    elif respuesta == "astuto":
        print(cualidad["Astuto"])
    elif respuesta == "leal":
        print(cualidad["Leal"])
    elif respuesta == "sabio":
        print(cualidad["Sabio"])   
    elif respuesta == "no se":
        print(random.choice(casas))
    else: 
        print("¡Eres un muggle!")
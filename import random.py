import random


def dificultad():
    dif = int(input(""""Seleccione el grado de dificultad
    1.- Facilito
    2.- Intermedio
    3.- Dificil
    """))
    if dif == 1:
        run(3, 20, 4)
    elif dif == 2:
        run(4, 50, 6)
    elif dif == 3:
        run(5, 100, 8)
    else:
        print("Porfavor elija un numero correcto")


def run(vidas, rango, cercania):
    num_random = random.randint(1, rango)
    num_elegido = int(
        input("Introduce un numero entre 0 y " + str(rango) + " : "))
    while num_random != num_elegido:
        if num_random < num_elegido:
            if num_elegido - num_random < cercania:
                print("Caliente!! ,elige un numero mas pequeño.")
            else:
                print("Elige un numero mas pequeño.")
            vidas -= 1
        elif num_random > num_elegido:
            if num_random - num_elegido < cercania:
                print("Caliente!! ,elige un numero mas grande.")
            else:
                print("Elige un numero mas grande.")
            vidas -= 1
        if vidas == 0:
            print("------ GAME OVER ------" +
                  "\n El numero era: " + str(num_random))
            break
        print("Tienes", vidas, "vidas restantes")
        num_elegido = int(input("Introduce numero: "))
    if num_random == num_elegido:
        print("FELICIDADES GANASTE")


if __name__ == "__main__":
    dificultad()

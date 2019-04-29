from time import sleep
import random
condition = True
while condition:
    usu_number = input("\nIngrese un número del 1 al 10: ")
    random_number = random.randint(1, 10)
    random_number = str(random_number)
    sleep(2)
    if usu_number == random_number:
        print("¡¡¡Has ganado!!!\n\n")
        condition = False
    else:
        print("Puedes volver a intentarlo.")
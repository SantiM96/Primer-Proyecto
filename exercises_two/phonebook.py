
def question():
    print("¿Que desea hacer?")
    print("-----------------------")
    print("Agregar número [A]")
    print("Consultar número [C]")
    print("Borrar [B]")
    ret = input().upper()
    print("-----------------------")
    return ret

print("")
book = dict()
condition = True

while condition:
    print("-----------------------")
    answer = question()

    #Add number
    if answer == "A":
        name = input("Nombre: ")
        number = input("Número: ")
        book[name] = number
        print("¡Número añadido!")

    #Check number
    elif answer == "C":
        print("¿Que número desea saber?")
        name = input()
        print(book[name])

    #Clean
    elif answer == "B":
        print("¿Seguro desea borrar su agenda? [Si/No]")
        sure = input().upper()
        if sure == "SI":
            print("")
            print("Su agenda ha sido borrada")
            condition = False


    print("")


def check_menu(selection):
    ishere = False

    if selection == "HAMBURGUESA":
        ishere = True
    elif selection == "PANCHO":
        ishere = True
    elif selection == "CHORIZO":
        ishere = True
    elif selection == "PAPAS FRITAS":
        ishere = True
    elif selection == "COCA COLA":
        ishere = True
    elif selection == "SPRITE":
        ishere = True
    elif selection == "FANTA":
        ishere = True
    elif selection == "AGUA":
        ishere = True

    if ishere == True:
        return True
    else:
        return False
def menu():
    print(" ")
    print("           Menú")
    print("          ------")
    print(" ")

    print("         Comidas")
    print("Hamburguesa ---$100")
    print("Pancho --------$80")
    print("Chorizo--------$100")
    print("Papas fritas---$50")
    print(" ")

    print("         Bebidas")
    print("Coca Cola------$45")
    print("Sprite---------$45")
    print("Fanta----------$45")
    print("Agua-----------$30")
    print(" ")
def correct(list):
    new_list = []
    for item in list:
        reset = 0
        new_item = ""
        for letter in item:
            if reset != 0:
                letter.lower()
                new_item += letter
            else:
                new_item += letter





order_list_client = []
large_list = 0
total = 0


print("")
input("Presione enter para comenzar su pedido")
menu()


main_condition = True
while main_condition:
    if large_list > 0:
        print("\n -Su pedido actual es: {}".format(order_list_client))
        selection = input("\nEscriba su selección o presione"
                          "\nenter para confirmar el pedido: ").upper()
    else:
        selection = input("\nEscriba su selección: ").upper()

    #check select
    tof = check_menu(selection)


    if tof == True:
        order_list_client.append(selection)
        large_list += 1
    else:
        if selection == "":
            if large_list != 0:
                main_condition = False

            else:
                print("\nIngrese una selección indicada en el Menú\n")
        else:
            print("\nIngrese una selección indicada en el Menú"
                  "\n")





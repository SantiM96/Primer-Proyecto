
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
                letter = letter.lower()
                new_item += letter
                reset += 1
                if letter == " ":
                    reset = 0
            else:
                new_item += letter
                reset += 1
        new_list.append(new_item)
    return new_list
def value_selection(selection):
    value = 0
    if selection == "HAMBURGUESA":
        value = 100
    elif selection == "PANCHO":
        value = 80
    elif selection == "CHORIZO":
        value = 100
    elif selection == "PAPAS FRITAS":
        value = 50
    elif selection == "COCA COLA":
        value = 45
    elif selection == "SPRITE":
        value = 45
    elif selection == "FANTA":
        value = 45
    elif selection == "AGUA":
        value = 30
    return value




order_list_client = []
order_list_final = []
large_list = 0
total = 0


print("")
input("Presione enter para comenzar su pedido")
menu()


main_condition = True
while main_condition:
    if large_list > 0:
        print("\n -Su pedido actual es: {}".format(correct(order_list_client)))
        selection = input("\n\tEscriba su selección o presione"
                          "\nenter para confirmar el pedido: ").upper()
    else:
        selection = input("\nEscriba su selección: ").upper()

    #check select
    tof = check_menu(selection)


    if tof == True:
        order_list_client.append(selection)
        large_list += 1
        total += value_selection(selection)
    else:
        if selection == "":
            if large_list != 0:
                main_condition = False

            else:
                print("\nIngrese una selección indicada en el Menú\n"
                      "\n------------------------------------------")
        else:
            print("\nIngrese una selección indicada en el Menú\n"
                  "\n------------------------------------------")

order_list_final = correct(order_list_client)
print("\n\n\nUsted seleccionó {}"
      "\nSerían: {}"
      "\ngracias por su preferencia\n\n\n".format(order_list_final, total))




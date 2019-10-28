
def check_menu(selection):
    ishere = False

    if selection in food_menu_list or selection in drinks_menu_list:
        ishere = True

    if ishere == True:
        return True
    else:
        return False
def large_script(word):
    large = 0
    for letter in word:
        large += 1
    script = (17 - large)
    script = "-" * script
    ret = word + script
    return ret
def menu():
    print(" ")
    print("           Menú")
    print("          ------")
    print(" ")

    print("         Comidas")
    for food in food_menu_list:
        print(large_script(food) + food_menu_dict[food])
    print(" ")
    print("         Bebidas")
    for drink in drinks_menu_list:
        print(large_script(drink) + drinks_menu_dict[drink])
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
    if selection in food_menu_list:
        value += int(food_menu_dict[selection])
    if selection in drinks_menu_list:
        value += int(drinks_menu_dict[selection])
    return value



food_menu_list = ["Hamburguesa", "Pancho", "Chorizo", "Papas fritas"]
food_menu_dict = dict({"Hamburguesa": "100", "Pancho": "80", "Chorizo": "100", "Papas fritas": "50"})

drinks_menu_dict = dict({"Coca Cola": "45", "Sprite": "45", "Fanta": "45", "Agua": "30"})
drinks_menu_list = ["Coca Cola", "Sprite", "Fanta", "Agua"]

check_list_admin = ["AC", "AB", "B1", "BC", "BB", ""]



first_condition = True
while first_condition:


    order_list_client = []
    order_list_final = []
    large_list = 0
    total = 0



    print("")
    ask_admin = input("Presione enter para comenzar su pedido")
    if ask_admin == "admin":
        condition_answer = True
        while condition_answer:

            print("Agregar Comida [AC]\n"
                  "Agregar Bebida [AB]\n"
                  "Borrar 1 [B1]\n"
                  "Borrar Comidas [BC]\n"
                  "Borrar Bebidas [BB]\n"
                  "Salir [Enter]")

            answer = input().upper()
            if answer in check_list_admin:


                # Add Food
                if answer == "AC":
                    new_food_name = input("Ingrese la nueva comida: ")
                    new_food_price = input("Ingrese el precio: ")
                    food_menu_list.append(new_food_name)
                    food_menu_dict[new_food_name] = new_food_price
                    print("Comida Agregada")


                # Add Drink
                elif answer == "AB":
                    new_drink_name = input("Ingrese la nueva bebida: ")
                    new_drink_price = input("Ingrese el precio: ")
                    drinks_menu_list.append(new_drink_name)
                    drinks_menu_dict[new_drink_name] = new_drink_price
                    print("Bebida Agregada")


                #Remove one
                elif answer == "B1":
                    delete_one = input("Ingrese el elemento que desea borrar del menú: ")
                    if delete_one in food_menu_list:
                        food_menu_list.remove(delete_one)
                        del food_menu_dict[delete_one]
                        print("Comida borrada")
                    elif delete_one in drinks_menu_list:
                        drinks_menu_list.remove(delete_one)
                        del drinks_menu_dict[delete_one]
                        print("Bebida Borrada")


                #Clean Foods
                elif answer == "BC":
                    food_menu_list = []
                    food_menu_dict = dict()
                    print("Menú de comidas borrado")


                #Clean Drinks
                elif answer == "BB":
                    drinks_menu_list = []
                    drinks_menu_dict = dict()
                    print("Menú de bebidas borrado")


                # Exit
                elif answer == "":
                    condition_answer = False



            else:
                print("Ingrese una de las opciones indicadas")





    else:

        menu()


        main_condition = True
        while main_condition:
            if large_list > 0:
                print("\n -Su pedido actual es: {}".format(correct(order_list_client)))
                selection = input("\nEscriba su selección o presione"
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
              "\nGracias por su preferencia\n\n\n".format(order_list_final, total))




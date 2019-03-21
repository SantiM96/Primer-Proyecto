
total = 0
selection_1 = "a"
selection_2 = "b"

input ("Presione enter para comenzar su pedido")
print(" ")

print("Escriba su selección del menú:")
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

selection_1 = input("Ingrese su selección: ").upper()
quest_1 = input("¿Desea pedir algo más?(Si / No): ").upper()

if selection_1 == "HAMBURGUESA":
    total += 100
elif selection_1 == "PANCHO":
    total += 80
elif selection_1 == "CHORIZO":
    total += 100
elif selection_1 == "PAPAS FRITAS":
    total += 50
elif selection_1 == "COCA COLA":
    total += 45
elif selection_1 == "SPRITE":
    total += 45
elif selection_1 == "FANTA":
    total += 45
elif selection_1 == "AGUA":
    total += 30

if quest_1 != "SI":
    print(" ")
    print("Su pedido es {}. Demorará entre 10 y 15 minutos".format(selection_1))
    print("Total: ${}".format(total))
else:
    selection_2 = input("Ingrese su selección: ").upper()
    quest_2 = input("¿Desea pedir algo más? (Si / No): ").upper()

    if selection_2 == "HAMBURGUESA":
        total += 100
    elif selection_2 == "PANCHO":
        total += 80
    elif selection_2 == "CHORIZO":
        total += 100
    elif selection_2 == "PAPAS FRITAS":
        total += 50
    elif selection_2 == "COCA COLA":
        total += 45
    elif selection_2 == "SPRITE":
        total += 45
    elif selection_2 == "FANTA":
        total += 45
    elif selection_2 == "AGUA":
        total += 30

    if quest_2 != "SI":
        print(" ")
        print("Su pedido es {} con {}. Demorará entre 10 y 15 minutos".format(selection_1, selection_2))
        print("Total: ${}".format(total))
    else:
        selection_3 = input("Ingrese su selección: ").upper()
        quest_3 = input("¿Desea pedir algo más?(Si / No): ").upper()

        if selection_3 == "HAMBURGUESA":
            total += 100
        elif selection_3 == "PANCHO":
            total += 80
        elif selection_3 == "CHORIZO":
            total += 100
        elif selection_3 == "PAPAS FRITAS":
            total += 50
        elif selection_3 == "COCA COLA":
            total += 45
        elif selection_3 == "SPRITE":
            total += 45
        elif selection_3 == "FANTA":
            total += 45
        elif selection_3 == "AGUA":
            total += 30

        if quest_3 != "SI":
            print(" ")
            print("Su pedido es {} con {} y {}. Demorará entre 10 y 15 minutos".format(selection_1, selection_2, selection_3))
            print("Total: ${}".format(total))
        else:
            selection_4 = input("Ingrese su selección: ").upper()
            quest_4 = input("¿Desea pedir algo más?(Si / No): ").upper()

            if selection_4 == "HAMBURGUESA":
                total += 100
            elif selection_4 == "PANCHO":
                total += 80
            elif selection_4 == "CHORIZO":
                total += 100
            elif selection_4 == "PAPAS FRITAS":
                total += 50
            elif selection_4 == "COCA COLA":
                total += 45
            elif selection_4 == "SPRITE":
                total += 45
            elif selection_4 == "FANTA":
                total += 45
            elif selection_4 == "AGUA":
                total += 30

            if quest_4 != "SI":
                print(" ")
                print("Su pedido es {}, {}, {} y {}. Demorará entre 15 y 20 minutos".format(selection_1, selection_2, selection_3, selection_4))
                print("Total: ${}".format(total))
            else:
                selection_5 = input("Ingrese su selección(Si / No): ").upper()
                if selection_5 == "HAMBURGUESA":
                    total += 100
                elif selection_5 == "PANCHO":
                    total += 80
                elif selection_5 == "CHORIZO":
                    total += 100
                elif selection_5 == "PAPAS FRITAS":
                    total += 50
                elif selection_5 == "COCA COLA":
                    total += 45
                elif selection_5 == "SPRITE":
                    total += 45
                elif selection_5 == "FANTA":
                    total += 45
                elif selection_5 == "AGUA":
                    total += 30

                print(" ")
                print("Su pedido es {}, {}, {}, {} y {}. Demorará entre 15 y 20 minutos".format(selection_1, selection_2, selection_3, selection_4, selection_5))
                print("Total: ${}".format(total))

print(" ")
print(" ")
print("Gracias por su compra")
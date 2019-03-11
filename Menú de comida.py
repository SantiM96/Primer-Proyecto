selection_1 = 0
selection_2 = 0
selection_3 = 0
selection_4 = 0
selection_5 = 0

input ("Presione enter para comenzar su pedido")
print(" ")

print("Escriba su selección del menú:")
print(" ")

print("         Comidas")
print("Hamburguesa")
print("Pancho")
print("Chorizo")
print("Papas fritas")
print(" ")

print("         Bebidas")
print("Coca Cola")
print("Sprite")
print("Fanta")
print("Agua")
print(" ")

selection_1 = input("Ingrese su selección: ").upper()

selection_2 = input("¿Desea pedir algo más?: ").upper()
if selection_2 == "SI" or "OK" or "OKEY" or "YES":
    selection_2 = input("Ingrese su selección: ").upper()

elif selection_2 != "SI"
    print(" ")
    print("Su pedido es {}".format(selection_1))

if selection_3 != "SI":
    print(" ")
    print("Su pedido es {} con {}".format(selection_1, selection_2))
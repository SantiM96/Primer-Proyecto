
print("")
print("Ingrese una serie de números para contar. (Ingrese FIN para continuar)")
print(" ")
print("")

n_list = []
n_usu = " "
n_count = 0

while n_usu != "FIN":
    while not n_usu.isdigit() and n_usu != "FIN":
        n_usu = input("Ingrese un número: ").upper()
        if not n_usu.isdigit() and n_usu != "FIN":
            print("Solo números")
            n_usu = " "

    if n_usu.isdigit():
        n_list.append(n_usu)
        n_count += 1
        print("¡Número añadido!")
        n_usu = " "


print("")
print("")
print("Usted ha ingresado {} números.".format(n_count))
print("")
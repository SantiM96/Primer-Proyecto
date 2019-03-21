
print("")
list_number = []
n_usu = " "
n_quantity = int(input("¿Cuantos números desea comparar?: "))
n_order = 1
print("")


while len(list_number) < n_quantity:
    while not n_usu.isdigit():
        n_usu = input("Ingrese el número ({}): ".format(n_order))
        if not n_usu.isdigit():
            print("Solo números ma friend")
            n_usu = " "

    if n_usu.isdigit():
        list_number.append(n_usu)
        n_order += 1
        print("¡Número añadido!")
        n_usu = " "

n_usu = list_number[1]

for number in list_number:
    n_small = n_usu
    if number < n_small:
        n_small = number

print("")
print("")
print("El menor número de los ingresados es: {}".format(n_small))


list_number = []
list_number_int = []
n_usu = " "
n_order = 1

print("")
print("Ingrese una serie de números para determinar el más pequeño.")
print("Ingrese `FIN` para continur")
print("")

while n_usu != "FIN":
    while not n_usu.isdigit() and n_usu != "FIN":
        n_usu = input("Ingrese el número ({}): ".format(n_order)).upper()
        if not n_usu.isdigit() and n_usu != "FIN":
            print("Solo números ma friend")
            n_usu = " "

    if n_usu.isdigit():
        list_number.append(n_usu)
        n_order += 1
        print("¡Número añadido!")
        n_usu = " "

for number in list_number:
    list_number_int.append(int(number))

n_usu = list_number_int[0]
n_small = n_usu
for number_1 in list_number_int:
    if number_1 <= n_small:
        n_small = number_1

print("")
print("")
print("El menor número de los ingresados es: {}".format(n_small))

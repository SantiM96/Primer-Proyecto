
print("")
list_number = []
list_number_int = []

n_usu = " "
n_order = 1

list_xtwo = []
list_xtrhee = []
list_xfive = []
list_xseven = []

print("")
print("Ingrese una serie de números para determinar el más pequeño.")
print("Ingrese \"FIN\" para continur")
print("")

while n_usu != "FIN":
    while not n_usu.isdigit() and n_usu != "FIN":
        n_usu = input("Ingrese el número ({}): ".format(n_order)).upper()
        if not n_usu.isdigit() and n_usu != "FIN":
            print("Solo números")
            n_usu = " "

    if n_usu.isdigit():
        list_number.append(n_usu)
        n_order += 1
        print("¡Número añadido!")
        n_usu = " "

for number in list_number:
    list_number_int.append(int(number))

for number in list_number_int:
    if number % 2 == 0:
        list_xtwo.append(number)
    if number % 3 == 0:
        list_xtrhee.append(number)
    if number % 5 == 0:
        list_xfive.append(number)
    if number % 7 == 0:
        list_xseven.append(number)

print("")
print("Los múltiplos de 2 son: {}".format(list_xtwo))
print("Los múltiplos de 3 son: {}".format(list_xtrhee))
print("Los múltiplos de 5 son: {}".format(list_xfive))
print("Los múltiplos de 7 son: {}".format(list_xseven))
print("")


list_number = []
n_usu = " "
print(""
      "Ingrese una serie de números para determinar el más pequeño."
      "Ingrese `FIN` para continur"
      "")
n_order = 1

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

n_usu = list_number[0]
n_small = n_usu
for number in list_number:
    if number <= n_small:
        n_small = number

print(""
      ""
      "El menor número de los ingresados es: {}".format(n_small))

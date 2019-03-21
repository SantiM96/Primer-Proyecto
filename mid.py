
print("")
print("Ingrese una serie de números para calcular la media. (Ingrese FIN para continuar)")
print("")

n_list = []
n_list_int = []
n_usu = " "
n_count = 0
sum = 0
result = 0

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
# Convert list str numbers to int
for number in n_list:
    n_list_int.append(int(number))

for number_1 in n_list_int:
    sum += number_1
result = sum / n_count

print("")
print("")
print("La media entre sus números es {}".format(result))
print("")
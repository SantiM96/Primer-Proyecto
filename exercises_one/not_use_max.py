
print("")
n_list = [2, 30, 44, 88, 135, 95, 1003, 2015, 55, 77]
print("")

n_max = n_list[0]

for number in n_list:
    if number > n_max:
        n_max = number

print("El número más grande de la lista es {}".format(n_max))
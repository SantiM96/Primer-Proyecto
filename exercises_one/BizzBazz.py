"""
Primero formato sin terminar ¡
"""
n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 30, 50, 70]

for index in range(len(n_list)):
    number = n_list[index]
    pri = ""
    if number % 3 == 0:
        pri += "Bizz"
    if number % 5 == 0:
        pri += "Bazz"
    if number % 3 == 0 and number % 5 == 0:
        pri = "Bazinga"
    if number % 3 == 0 or number % 5 == 0:
        n_list[index] = pri

print(n_list)
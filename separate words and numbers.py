"""not found"""
start_list = [2, "hola", 7, "chau", "nos vemos", "hasta", 48, 55]
str_list = []
n_list = []

for item in start_list:
    if type(item) is int:
        n_list.append(item)
    else:
        str_list.append(item)

print("")
print("los números de la lista son: ", n_list)
print("Las palabras de la lista son: ", str_list)



print("")
n_tabla_usu = int(input("Ingrese el número para obtener su tabla: "))
print("")

result = 0

for multiplo in reversed(range(1, 11)):
    result = n_tabla_usu * multiplo
    if result % 2 == 0:
        print("{} x {} = {}".format(n_tabla_usu, multiplo, result))

print("")

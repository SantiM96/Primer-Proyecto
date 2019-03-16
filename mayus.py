
print("")
txt_usu = input("Ingrese una frase: ")

mayus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
n_mayus = 0

for letra in txt_usu:
    if letra in mayus:
        n_mayus += 1

print("")
print("")
print("Su frase tiene {} mayusculas".format(n_mayus))

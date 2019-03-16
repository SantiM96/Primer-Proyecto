
print("")
txt_usu = input("ingrese una frase: ")

vocales = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
n_vocales = 0
list_vocales = []

for letra in txt_usu:
    if letra in vocales:
        list_vocales.append(letra)
    elif letra in vocales:
        n_vocales += 1

print("")
print("")
print("Esta es la lista de vocales de su frase: {}".format(list_vocales))

print("")
txt_usu = input("ingrese una frase: ")

vocales = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
list_vocales = []

for letra in txt_usu:
    if letra in vocales:
        list_vocales.append(letra)

print("")
print("")
print("Esta es la lista de vocales de su frase: {}".format(list_vocales))
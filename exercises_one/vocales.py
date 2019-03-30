
print("")
txt_usu = input("Ingrese una frase: ").upper()

vocales = ["A", "E", "I", "O", "U"]
espacios = " "
n_vocales = 0
n_consonantes = 0


for letra in txt_usu:
    if letra in vocales:
        n_vocales += 1
    elif letra not in vocales and letra != espacios:
        n_consonantes += 1

print("")
print("")
print("La frase tiene {} vocales".format(n_vocales))
print("La frase tiene {} consonantes".format(n_consonantes))
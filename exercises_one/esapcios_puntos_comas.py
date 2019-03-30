
print("")
txt_usu = input("Ingrese una frase: ")

espacios = " "
puntos = "."
comas = ","
n_espacios = 0
n_puntos = 0
n_comas = 0

for letra in txt_usu:
    if letra in espacios:
        n_espacios += 1
    elif letra in puntos:
        n_puntos += 1
    elif letra in comas:
        n_comas += 1

print("")
print("")
print("La frase tiene {} esapcios".format(n_espacios))
print("La frase tiene {} puntos".format(n_puntos))
print("La frase tiene {} comas".format(n_comas))

print("")
usu_sent = input("Ingrese una oración: ")
print("")

n_appear = 0
vow_list = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

for letter in usu_sent:
    if letter in vow_list:
        n_appear += 1
        n_appear = str(n_appear)
        usu_sent = usu_sent.replace(letter, n_appear, 1)
        n_appear = int(n_appear)

print(usu_sent)
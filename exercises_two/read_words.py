
print("")
txt_usu = input("Ingrese una oración: ")
print("")
new_str = ""
quan = dict()
index = 1
more = 0

#apart word
for letter in txt_usu:
    if letter != " " and letter != "." and letter != "," and letter != "!"and letter != "¡" and letter != "?" and letter != "¿":
        new_str += letter
    if letter == " " or index == len(txt_usu):
        if new_str in quan:
            more = quan[new_str]
            more += 1
            quan[new_str] = more
        if new_str not in quan:
            quan[new_str] = 1
        new_str = ""
    index += 1

print("")
print("Usted ha ingresado las siguientes palabras:")
print("")

#print words
for word in quan:
    forprint = word
    word += ":"
    if quan[forprint] == 1 or quan[forprint] == -1:
        print(word, quan[forprint], "vez")
    else:
        print(word, quan[forprint], "veces")
print("")
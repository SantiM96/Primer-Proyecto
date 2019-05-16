
def check_ci(ci, list, text):
    condition = True
    condition_numbers = False
    condition_dots = False
    while condition:
        list_ci = []
        list_ci_complete = []
        for letter in ci:
            if letter in list:
                list_ci.append(letter)
        if len(list_ci) == 8:
            condition_numbers = True
        for letter in ci:
            list_ci_complete.append(letter)
        if list_ci_complete[1] == "." and list_ci_complete[5] == "." and list_ci_complete[9] == "-":
            condition_dots = True
        if condition_numbers and condition_dots:
            condition = False
        else:
            print(text)
            ci = input()

    return ci
def check(file, possible_list, text):
    condition_check = True
    while condition_check:
        if file not in possible_list:
            print(text)
            file = input().upper()
        if file in possible_list:
            condition_check = False
    return file
def subjects(text_sub, text_error):
    sub = input(text_sub)
    sub = check(sub, list_number, text_error)
    int(sub)
    condition = True
    while condition:
        if sub <= 20 and sub >= 0:
            condition = False
        else:
            sub = input(text_error)
            sub = check(sub, list_number, text_error)
            int(sub)
    return sub
def question_subjects():
    dict_sub = dict()

    mate = subjects("Ingrese la nota de matemátcas: ", "Ingrese una nota válida: ")
    dict_sub["Matemáticas"] = mate

    lenguague = subjects("Ingrese la nota de lenguaje: ", "Ingrese una nota válida: ")
    dict_sub["Lenguaje"] = lenguague

    critic = subjects("Ingrese la nota de formación crítica: ", "Ingrese una nota válida: ")
    dict_sub["Formación Crítica"] = critic

    elective = subjects("Ingrese la nota de electiva: ", "Ingrese una nota válida: ")
    dict_sub["Electiva"] = elective

    atr = subjects("Ingrese la nota de ATR: ", "Ingrese una nota válida: ")
    dict_sub["ATR"] = atr

    proyect = subjects("Ingrese la nota de Proyecto: ", "Ingrese una nota válida: ")
    dict_sub["Proyecto"] = proyect

    algoritmic = subjects("Ingrese la nota de Algorítmica: ", "Ingrese una nota válida: ")
    dict_sub["Algorítmica"] = algoritmic

    return dict_sub



list_trimester = ["primero", "segundo", "tercero"]
list_number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
dict_course = dict()
name_usu = input("Ingrese su nombre: ")
CI = input("Ingrese su cédula: ")
CI = check_ci(CI, list_number, "Ingrese una cédula válida")
dict_course["trimestre_uno"]
course = input("Ingrese su curso: ")
print("¿En que trimestre se encuentra? [Primero / Segundo / Tercereo]")
trimester = input().lower()
trimester = check(trimester, list_trimester, "Ingrese una de las opciones [Primero / Segundo / Tercereo]")

print("Ingrese las notas del primer semestre")
dict_one = question_subjects()

print("Ingrese las notas del segundo semestre")
dict_two = question_subjects()

print("Ingrese las notas del tercero semestre")
dict_three = question_subjects()

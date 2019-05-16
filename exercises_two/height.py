"""
De una lista de N cantidad de estaturas de personas se desea saber lo siguiente
1) El promedio
2) El punto medio
3) Cuantos son menores a 1.70
4) Cuantos son mayores a 1.70
"""

def check_number_height(number, text):
    list_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    not_is_number = True
    is_possible_height = True
    while not_is_number and is_possible_height:
        not_is_number = True
        is_possible_height = True
        while not_is_number:
            list_usu = []
            for item in number:
                list_usu.append(item)
            if len(list_usu) == 4:
                if list_usu[0] in list_numbers and list_usu[1] == "." and\
                   list_usu[2] in list_numbers and list_usu[3] in list_numbers:
                    not_is_number = False
                else:
                    number = input(text)
            elif len(list_usu) == 3:
                if list_usu[0] in list_numbers and list_usu[1] == "." and list_usu[2] in list_numbers:
                    not_is_number = False
                else:
                    number = input(text)
            else:
                number = input(text)

            if not not_is_number:
                number = float(number)
                if number < 3.5 and number > 1.0:
                    is_possible_height = False
                else:
                    number = input(text)


    return number
def check_number_height_key(number, text, keyword):
    list_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    not_is_number = True
    is_possible_height = True
    while not_is_number or is_possible_height:
        not_is_number = True
        is_possible_height = True
        while not_is_number:
            list_usu = []
            for item in number:
                list_usu.append(item)
            if len(list_usu) == 4:
                if list_usu[0] in list_numbers and list_usu[1] == "." and\
                   list_usu[2] in list_numbers and list_usu[3] in list_numbers:
                    not_is_number = False
                else:
                    number = input(text)
            elif len(list_usu) == 3:
                if list_usu[0] in list_numbers and list_usu[1] == "." and list_usu[2] in list_numbers:
                    not_is_number = False
                else:
                    number = input(text)
            else:
                number = input(text)

            if not not_is_number:
                number = float(number)
                if number < 3.5 and number > 1.0:
                    is_possible_height = False
                else:
                    number = input(text)
            if keyword == number:
                not_is_number = False
                is_possible_height = False



    return number

list_height = []
higher = []
less = []
average = 0
mid_point = 0


height = input("\nIngrese su estatura: ")
height = check_number_height(height, "Ingrese una estatura válida: ")
list_height.append(height)
height = input("Ingrese su estatura: ")
height = check_number_height(height, "Ingrese una estatura válida; ")
list_height.append(height)

condition = True
while condition:
    height = input("Ingrese su estatura o ingrese listo para continuar: ")
    if height.lower() != "listo":
        height = check_number_height_key(height, "Ingrese una estatura válida: ", "listo")
        list_height.append(height)
    else:
        condition = False

# Average
for number in list_height:
    average += number
average = average / len(list_height)

# Mid Point
mid_point = list_height[0] + list_height[(len(list_height) - 1)]
mid_point = mid_point / 2

# Higher 1.70
for number in list_height:
    if number >= 1.70:
        higher.append(number)

# Less 1.70
for number in list_height:
    if number < 1.70:
        less.append(number)

print("\n\nEl promedio de las estaturas es: {}"
      "\nEl punto medio es: {}"
      "\nLos mayores a 1.70 son: {}"
      "\nLos menores a 1.70 son: {}".format(average, mid_point, higher, less))

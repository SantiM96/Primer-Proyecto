"""
De una lista de N cantidad de estaturas de personas se desea saber lo siguiente
1) El promedio
2) El punto medio
3) Cuantos son menores a 1.70
4) Cuantos son mayores a 1.70
"""

def check_number_height(number, min_number, max_number, text_error):
    list_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    condition_while = True

    while condition_while:
        condition_one = False
        condition_two = False
        list_of_number = []
        for item in number:
            list_of_number.append(item)


        if len(list_of_number) == 1:
            if list_of_number[0] in list_numbers:
                condition_one = True


        elif len(list_of_number) == 3:
            if list_of_number[0] in list_numbers and list_of_number[1] == "." and list_of_number[2] in list_numbers:
                condition_one = True


        elif len(list_of_number) == 4:
            if list_of_number[0] in list_numbers and list_of_number[1] == "." and\
            list_of_number[2] in list_numbers and list_of_number[3] in list_numbers:
                condition_one = True


        if condition_one:
            number = float(number)
            if number <= max_number and number >= min_number:
                condition_two = True


        if condition_one and condition_two:
            condition_while = False
        else:
            number = input(text_error)

    return number
def check_number_height_key(number, min_number, max_number, key, text_error):
    list_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    condition_while = True

    while condition_while:
        condition_one = False
        condition_two = False
        list_of_number = []

        for item in number:
            list_of_number.append(item)


        if len(list_of_number) == 1:
            if list_of_number[0] in list_numbers:
                condition_one = True


        elif len(list_of_number) == 3:
            if list_of_number[0] in list_numbers and list_of_number[1] == "." and list_of_number[2] in list_numbers:
                condition_one = True


        elif len(list_of_number) == 4:
            if list_of_number[0] in list_numbers and list_of_number[1] == "." and\
            list_of_number[2] in list_numbers and list_of_number[3] in list_numbers:
                condition_one = True


        if condition_one:
            number = float(number)
            if number <= max_number and number >= min_number:
                condition_two = True


        if (condition_one and condition_two):
            condition_while = False
        elif not condition_one:
            if number.lower() == key:
                condition_while = False
            else:
                number = input(text_error)
        else:
            number = input(text_error)

    return number


list_height = []
higher = []
less = []
average = 0
mid_point = 0


height = input("\nIngrese su estatura: ")
height = check_number_height(height, 1, 3.5, "Ingrese una estatura válida: ")
list_height.append(height)
height = input("Ingrese su estatura: ")
height = check_number_height(height, 1, 3.5, "Ingrese una estatura válida: ")
list_height.append(height)



main_condition = True
while main_condition:
    height = input("Ingrese su estatura o ingrese listo para continuar: ")
    height = check_number_height_key(height, 1, 3.5, "listo", "Ingrese una estatura válida: ")
    if height == "listo":
        main_condition = False
    else:
        list_height.append(height)


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
print("\n------------------------------------------------------")
print("\nEl promedio de las estaturas es: {}"
      "\nEl punto medio es: {}"
      "\nLos mayores a 1.70 son: {}"
      "\nLos menores a 1.70 son: {}".format(average, mid_point, higher, less))

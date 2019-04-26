import datetime

print("")
print("Ingresa tu fecha de nacimiento [dd/mm/aaaa]")
birth_date = input()

def chdate(date, error_message_ivalid, error_message_same, error_message_exceed):
    check = [["0", "1", "2", "3"], ["0", "1", "2"], ["0", "1"]]
    all_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    condition = True
    while condition == True:
        print("")
        date_list = []
        n = 0
        condition_day = False
        condition_month = False
        condition_year = False
        condition_numbers = False

        for item in date:
            date_list.append(item)
            n += 1
        if n == 10:
            if date_list[2] == "/" and date_list[5] == "/":

                # Check day
                if date_list[0] in check[0]:
                    if date_list[0] == "3":
                        if date_list[1] in check[1]:
                            condition_day = True
                    else:
                        condition_day = True

                # Check month
                if date_list[3] in check[2]:
                    if date_list[3] == "1":
                        if date_list[4] in check[1]:
                            condition_month = True
                    else:
                        condition_month = True

                # Check all number
                if date_list[0] in all_numbers and date_list[1] in all_numbers and date_list[3] in all_numbers and \
                        date_list[4] in all_numbers and date_list[6] in all_numbers and date_list[7] in all_numbers and \
                        date_list[8] in all_numbers and date_list[9] in all_numbers:
                    condition_numbers = True

                # Check year
                if condition_numbers == True:
                    date_now = datetime.datetime.now()
                    year_f_check_str = date_list[6] + date_list[7] + date_list[8] + date_list[9]
                    year_f_check_int = int(year_f_check_str)
                    year_now_int = date_now.year
                    if year_now_int == year_f_check_int:
                        print(error_message_same)
                    if year_now_int < year_f_check_int:
                        print(error_message_exceed)
                    if year_now_int > year_f_check_int:
                        condition_year = True

        if condition_year == True and condition_month == True and condition_day == True:
            condition = False
        else:
            print(error_message_ivalid)
            date = input()

    date_ret = datetime.datetime.strptime(date, "%d/%m/%Y")
    return date_ret

# Example
test = chdate(birth_date, "Ingrese una fecha válida en el formato indicado [dd/mm/aaaa]", "Eres muy joven para este test", "Vuelve a intentarlo luego de nacer")
print(test)

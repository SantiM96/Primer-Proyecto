import datetime

def check_date(date, error_message_invalid):
    check = [["0", "1", "2", "3"], ["0", "1", "2"], ["0", "1"]]
    all_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    condition = True
    while condition:
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
                if date_list[0] in all_numbers and date_list[1] in all_numbers and date_list[3] in all_numbers and date_list[4] in all_numbers and date_list[6] in all_numbers and date_list[7] in all_numbers and date_list[8] in all_numbers and date_list[9] in all_numbers:
                    condition_numbers = True

                # Check year
                if condition_numbers:
                    date_now = datetime.datetime.now()
                    year_f_check_str = date_list[6] + date_list[7] + date_list[8] + date_list[9]
                    year_f_check_int = int(year_f_check_str)
                    year_now_int = date_now.year
                    if year_now_int <= year_f_check_int:
                        condition_year = True



        if condition_year == True and condition_month == True and condition_day == True:
            condition = False
        else:
            print(error_message_invalid)
            date = input()

    date_ret = datetime.datetime.strptime(date, "%d/%m/%Y")
    return date_ret
def check(day, possible_list, text):
    condition_check = True
    while condition_check:
        if day not in possible_list:
            print(text)
            day = input().upper()
        if day in possible_list:
            condition_check = False
    return day

def alarm():
    possible_list_days = ["L", "MA", "MI", "J", "V", "S", "D"]
    possible_list_question = ["T", "LV", "P"]
    yes_not_list = ["SI", "NO"]
    days_list = []
    print("¿A que hora desea la alarma?")
    hour = input()
    print("Que día desea que suene ( Todos [T] - Lunesa a Viernes [LV] Personalizado [P] )")
    answer = input().upper()
    answer = check(answer, possible_list_question, "Ingrese una opción válida\n( Todos [T] -"
                                                    " Lunesa a Viernes [LV] Personalizado [P] )")
    if answer == "P":
        print("Ingrese un día \n( Lunes [L] - Martes [Ma] - Miercoles [Mi]"
              " - Jueves [J] - Viernes [V] - Sábado [S] - Domingo [D] )")
        answer = input().upper()
        answer = check(answer, possible_list_days, "Ingrese una opción válida\n( Lunes [L] - Martes [Ma] - Miercoles"
                                                   " [Mi] - Jueves [J] - Viernes [V] - Sábado [S] - Domingo [D] )")
        days_list.append(answer)
        condition = True
        while condition:
            print("¿Desea agregar otro día? [Si/No]")
            answer = input().upper()
            answer = check(answer, yes_not_list, "Ingrese una opción válida [Si/No]")
            if answer == "SI":
                print("Ingrese un día \n( Lunes [L] - Martes [Ma] - Miercoles [Mi]"
                      " - Jueves [J] - Viernes [V] - Sábado [S] - Domingo [D] )")
                answer = input().upper()
                answer = check(answer, possible_list_days, "Ingrese una opción válida\n( Lunes [L] - Martes [Ma] - Miercoles"
                                                           " [Mi] - Jueves [J] - Viernes [V] - Sábado [S] - Domingo [D] )")
                days_list.append(answer)
            else:
                condition = False
    elif answer == "LV":
        days_list.append("L")
        days_list.append("MA")
        days_list.append("MI")
        days_list.append("J")
        days_list.append("V")
    else:
        days_list = possible_list_days

    print("¿Desea que la alarma suene en una fecha en específico? [Si/No]")
    specific = input().upper()
    specific = check(specific, yes_not_list, "Ingrese una opción válida [Si/No]")
    if specific == "SI":
        print("ingrese la fecha. [dd/mm/aaaa]")
        date_alarm = input()
        date_alarm = check_date(date_alarm, "Ingrese la fecha en el formato indicado [dd/mm/aaaa]")
        date_specific = True

    return hour, days_list, date_alarm, date_specific



hour, day_list, date_alarm, date_specific = alarm()
print(hour)
print(day_list)
print(date_alarm)
print(date_specific)
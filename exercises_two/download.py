from time import sleep

import datetime



NIGHT_STARTS = 19

DAY_STARTS = 8

HOUR_DURATION = 1




def write_file_and_screen(text, file_name):

    with open(file_name, "a") as hours_file:

        hours_file.write("{}{}".format(text, "\n"))

        print(text)

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
def weekdaystr(weekday):
    if weekday == 0:
        weekday = "Lunes"
    elif weekday == 1:
        weekday = "Martes"
    elif weekday == 2:
        weekday = "Miercoles"
    elif weekday == 3:
        weekday = "Jueves"
    elif weekday == 4:
        weekday = "Viernes"
    elif weekday == 5:
        weekday = "Sábado"
    elif weekday == 6:
        weekday = "Domingo"
    return weekday

def alarm():

    possible_list_days = ["L", "MA", "MI", "J", "V", "S", "D"]
    possible_list_question = ["T", "LV", "P", "F"]
    yes_not_list = ["SI", "NO"]
    days_list = []
    days_list_return = []
    date_specific = False
    days_confirmation = True
    date_alarm = datetime.datetime.now()
    date_alarm - datetime.timedelta(hours=1)

    print("¿A que hora desea la alarma?")
    hour = input()
    print("Que día desea que suene ( Todos [T] - Lunesa a Viernes [LV] - Personalizado [P] - Solo fecha específica [F] )")
    answer = input().upper()
    answer = check(answer, possible_list_question, "Ingrese una opción válida\n( Todos [T] - Lunesa a Viernes [LV]"
                                                   " Personalizado [P] - Solo fecha específica [F] )")
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
    elif answer == "T":
        days_list = possible_list_days
    else:
        days_confirmation = False

    if days_confirmation:
        print("Además, ¿Desea que la alarma suene en una fecha en específico? [Si/No]")
        specific = input().upper()
        specific = check(specific, yes_not_list, "Ingrese una opción válida [Si/No]")
    else:
        specific = "SI"

    if specific == "SI":
        print("Ingrese la fecha. Formato: [dd/mm/aaaa]")
        date_alarm = input()
        date_alarm = check_date(date_alarm, "Ingrese la fecha en el formato indicado [dd/mm/aaaa]")
        date_specific = True

    if days_confirmation:
        for day in days_list:
            if day == "L":
                days_list_return.append("Lunes")
            elif day == "MA":
                days_list_return.append("Martes")
            elif day == "MI":
                days_list_return.append("Miercoles")
            elif day == "J":
                days_list_return.append("Jueves")
            elif day == "V":
                days_list_return.append("Viernes")
            elif day == "S":
                days_list_return.append("Sábado")
            elif day == "D":
                days_list_return.append("Domingo")
    else:
        days_list_return.append(False)

    return int(hour), days_list_return, date_alarm, date_specific






def main():

    print("¿Desea programar una alarma? [Si/No]")
    answer = input().upper()
    if answer == "SI":
        hour_alarm, day_list, date_alarm, date_specific = alarm()

    current_time = datetime.datetime.now()

    is_night = False

    while True:

        sleep(HOUR_DURATION)

        current_time += datetime.timedelta(hours=1)

        light_changed = False

        weekday = current_time.weekday()
        weekday = weekdaystr(weekday)

        if (current_time.hour >= NIGHT_STARTS or current_time.hour <= DAY_STARTS) and not is_night:

            is_night = True

            light_changed = True



        elif (current_time.hour > DAY_STARTS and current_time.hour < NIGHT_STARTS) and is_night:

            is_night = False

            light_changed = True



        if light_changed:

            if is_night:

                write_file_and_screen("Se ha hecho de noche", "horas.txt")

            else:

                write_file_and_screen("Se ha hecho de día", "horas.txt")



        write_file_and_screen("La hora actual es {}".format(current_time), "horas.txt")


        if current_time.hour == 0:

            write_file_and_screen("Es {}".format(weekday), "horas.txt")



        if day_list[0] != False:
            if current_time.hour == hour_alarm and weekday in day_list:

                write_file_and_screen("Suena la alarma", "horas.txt")


        if date_specific:

            year_check = current_time.year
            month_check = current_time.month
            day_check = current_time.day
            date_check = datetime.datetime(year=year_check, month=month_check, day=day_check)

            if date_check == date_alarm and current_time.hour == hour_alarm:

                write_file_and_screen("Suena la alarma", "horas.txt")







if __name__ == "__main__":

    main()
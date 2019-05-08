import datetime, random

#It has to be divisible by 1.5
MID_LIFE = 90

TOTAL_PENALIZATION_SMOKE = 8
TOTAL_PENALIZATION_DRINK = 6
TOTAL_PENALIZATION_RUN = 10
discount_life = 0
strmeasure = "[ No(N) / Poco(P) / Seguido(S) / Habitualmente(H) ]"

def do(message):
    answer = ""
    while answer != "N" and answer != "P" and answer != "S" and answer != "H":
        print(message + strmeasure)
        answer = input().upper()
        if answer != "N" and answer != "P" and answer != "S" and answer != "H":
            print("Ingresa una de las respuestas indicadas")
    return answer
def discount(PENALIZATION, message):
    discount = 0
    habit = do(message)
    if habit == "P":
        discount += PENALIZATION / 2 / 2
    elif habit == "S":
        discount += PENALIZATION / 2
    elif habit == "H":
        discount += PENALIZATION
    return int(discount)
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
                if date_list[0] in all_numbers and date_list[1] in all_numbers and date_list[3] in all_numbers and date_list[4] in all_numbers and date_list[6] in all_numbers and date_list[7] in all_numbers and date_list[8] in all_numbers and date_list[9] in all_numbers:
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


print("")
print("     ¡Averigua la fecha de tu muerte!")
print("-------------------------------------------")
print("Ingresa tu fecha de nacimiento [dd/mm/aaaa]")
birth_date = input()
birth_date = chdate(birth_date, "Ingrese una fecha válida en el formato indicado [dd/mm/aaaa]", "Debes tener al menos un año de vida para saber cuando morirás", "Esa fecha aun no llega")

print("")
disc_smoke = discount(TOTAL_PENALIZATION_SMOKE, "¿Fumas?")
disc_drink = discount(TOTAL_PENALIZATION_DRINK, "¿Bebes?")
disc_run = discount(TOTAL_PENALIZATION_RUN, "¿Haces ejercicio?")


discount_life = disc_smoke + disc_drink - disc_run
life = random.randint(int(MID_LIFE/1.5), MID_LIFE)
death_years_old = life - discount_life
death_days_old = death_years_old * 365

# Extra to vary the months between birth and death
ex = (random.randint(1, 12) * 30)
ex = datetime.timedelta(days=ex)

# Dates
death_day = birth_date + ex + datetime.timedelta(days=death_days_old)
rest_year_alive = death_day - datetime.datetime.now()
rest_year_alive = int(rest_year_alive.total_seconds() / 31536000)

if rest_year_alive > 0:
    print("")
    print(death_day.strftime("Te vas a morir a los {} años de edad, el %d del %m del %Y".format(death_years_old)))
    print("Disfruta tus últimos {} años de vida".format(rest_year_alive))
    print("")
else:
    print("")
    print("Ups, eres afortunado, deberías estar muerto")


import datetime, random

#It has to be divisible by 1.5
MID_LIFE = 90

TOTAL_PENALIZATION_SMOKE = 8
TOTAL_PENALIZATION_DRINK = 6
TOTAL_PENALIZATION_RUN = 10
discount_life = 0
strmeasure = "[ No(N) / Poco(P) / Seguido(S) / Habitualmente(H) ]"
condition = True
n = 0
index = 0
date_list_digit = []
checklists = [["0", "1", "2", "3"], ["0", "1", "2"], ["0", "1"]]


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
def restart():
    print("Ingresa una fecha válida y en el formato indicado [dd/mm/aaaa]")
    n = 0
    index = len(date_list_digit) - 1
    for item in birth_date:
        date_list_digit.pop(index)
        index -= 1

print("")
print("     ¡Averigua la fecha de tu muerte!")
print("-------------------------------------------")
print("Ingresa tu fecha de nacimiento [dd/mm/aaaa]")

while condition == True:
    birth_date = input()
    for item in birth_date:
        n += 1
    if n == 10:
        for item in birth_date:
            date_list_digit.append(item)
        if date_list_digit[2] == "/" and date_list_digit[5] == "/":
            """"""""""""""""""""""""
            if date_list_digit[0] in checklists[0]:
                if date_list_digit[3] in checklists[2]:




                if date_list_digit[0] == "3":
                    if date_list_digit[1] in checklists[1]:





                    else:
                        restart()


            else:
                restart()



            birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")
            condition = False
            """"""""""""""""""""""""
        else:
            print("Ingresa la fecha en el formato indicado [dd/mm/aaaa]")
            n = 0
            index = len(date_list_digit) - 1
            for item in birth_date:
                date_list_digit.pop(index)
                index -= 1
    else:
        print("Ingresa la fecha en el formato indicado [dd/mm/aaaa]")
        n = 0

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


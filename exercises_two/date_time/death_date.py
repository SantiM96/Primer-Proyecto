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

print("")
print("     ¡Averigua la fecha de tu muerte!")
print("-------------------------------------------")
print("Ingresa tu fecha de nacimiento [dd/mm/aaaa]")
birth_date = input()
birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")

print("")
disc_smoke = discount(TOTAL_PENALIZATION_SMOKE, "¿Fumas?")
disc_drink = discount(TOTAL_PENALIZATION_DRINK, "¿Bebes?")
disc_run = discount(TOTAL_PENALIZATION_RUN, "¿Haces ejercicio?")


discount_life = disc_smoke + disc_drink - disc_run
life = random.randint(int(MID_LIFE/1.5), MID_LIFE)
death_years_old = life - discount_life
death_days_old = death_years_old * 365

# Extra to vary the months between birth and death
if disc_smoke != 0:
    death_days_old += 47
if disc_drink != 0:
    death_days_old += 54
if disc_run != 0:
    death_days_old += 23

# Dates
death_day = birth_date + datetime.timedelta(days=death_days_old)
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


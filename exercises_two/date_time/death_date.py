import datetime, random

#It has to be divisible by 1.5
MID_LIFE = 80

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
print("¡Averigua la fecha de tu muerte!")
print("--------------------------------")
print("Ingresa tu fecha de nacimiento [dd/mm/aaaa]")

disc_smoke = discount(TOTAL_PENALIZATION_SMOKE, "¿Fumas?")
disc_drink = discount(TOTAL_PENALIZATION_DRINK, "¿Bebes?")
disc_run = discount(TOTAL_PENALIZATION_RUN, "¿Haces ejercicio?")

discount_life = disc_smoke + disc_drink - disc_run
life = random.randint(int(MID_LIFE/1.5), MID_LIFE)
death_years_old = life - discount_life

print(death_years_old)










print("Morirás el")
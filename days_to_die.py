
print("")
days = int(input("Ingrese los días del servidor: "))
print("")

count_day = days
rest_days = 0
day_atack = 0

for day in range(1, 8):
    if count_day % 7 != 0:
        count_day += 1
        rest_days += 1

day_atack = rest_days + days


print("Faltan {} días para la horda. Atacará el día {}".format(rest_days, day_atack))
print("")



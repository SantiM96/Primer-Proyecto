import datetime

print("")
print("Ingrese una fecha pasada.")
year = int(input("Año: "))
month = int(input("Mes: "))
day = int(input("Día: "))

usu_date = datetime.datetime(year=year, month=month, day=day)
now_date = datetime.datetime.now()

past = now_date - usu_date

print("")
print("Han pasado {} horas desde ese día.".format(int(past.total_seconds()/3600)))
print("")
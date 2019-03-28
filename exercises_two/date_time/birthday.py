import datetime

def wday(day):
    if day == 0:
        strday = "Lunes"
    elif day == 1:
        strday = "Martes"
    elif day == 2:
        strday = "Miercoles"
    elif day == 3:
        strday = "Jueves"
    elif day == 4:
        strday = "Viernes"
    elif day == 5:
        strday = "Sabado"
    elif day == 6:
        strday = "Domingo"
    return strday

print("")
print("Ingrese la fecha de su cumpleaños")
month = int(input("Mes: "))
day = int(input("Día: "))

now = datetime.datetime.now()
year_now = now.year
remain = datetime.datetime(year=year_now, month=month, day=day) - datetime.datetime.now()
birthday_day = datetime.datetime(year=year_now, month=month, day=day)
wday(birthday_day.weekday())

print("")
print("Faltan {} días y {} horas para tu cumpleaños. Será un {}".format(remain.days, int(remain.seconds / 3600), wday(birthday_day.weekday())))
print("")

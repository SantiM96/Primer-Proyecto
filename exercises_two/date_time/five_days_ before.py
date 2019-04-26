import datetime
"""Crea un programa que te diga la fecha de cinco días atras"""

print("")
day_before = ""
day_five_before = datetime.datetime.now() - datetime.timedelta(days=5)
day_before_n = day_five_before.weekday()

if day_before_n == 0:
    day_before = "Lunes"
elif day_before_n == 1:
    day_before = "Martes"
elif day_before_n == 2:
    day_before = "Miercoles"
elif day_before_n == 3:
    day_before = "Jueves"
elif day_before_n == 4:
    day_before = "Viernes"
elif day_before_n == 5:
    day_before = "Sabado"
elif day_before_n == 6:
    day_before = "Domingo"

print("Hace cinco días fue {} {}.".format(day_before, day_five_before.strftime("%d del %m del %y")))
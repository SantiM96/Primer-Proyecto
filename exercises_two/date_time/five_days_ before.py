import datetime
"""Crea un programa que te diga la fecha de cinco días atras"""

print("")

day_five_before = datetime.datetime.now() - datetime.timedelta(days=5)

print("Hace cinco días fue ")
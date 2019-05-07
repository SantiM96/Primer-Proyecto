from time import sleep
import random

phrases = ["No soy un completo inútil, por lo menos sirvo de mal ejemplo.", "Yo pienso que es mejor no pensar.",
           "Esta obsesión de suicidio me está matando.", "¡¡Antes de perder la vida, prefiero la muerte!!",
           "Hay un mundo mejor, pero es carísimo.", "El que ríe de ultimo no entendió el chiste."]

while True:
    number_random = random.randint(0, (len(phrases) - 1))
    print("\n", phrases[number_random])
    sleep(3)
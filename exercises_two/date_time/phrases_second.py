from time import sleep
import random

list_cheerful = ["Las cosas son bellas si se las ama", "Hay una sola forma de felicidad en la vida: amar y ser amado",
                 "Aquellos que quieren cantar siempre encuentran una canción",
                 "Cuando eres fiel a ti mismo en lo que haces, cosas fascinantes ocurren"]
list_furniture = ["Silla", "Mesa", "Cama", "Ropero", "Escritorio"]
list_drinks = ["Coca Cola", "Sprite", "Mirinda", "Pomelo", "Pepsi"]
list_hate = ["Si se incendiase tu casa y yo tuviese una botella de agua entre mis manos, me la bebería",
             "Se ve que lo que se lleva es la hipocresía, y tú eres de los que van a la moda. ",
             "Odiamos a una persona cuando no hemos aprendido a olvidar, cuando no sabemos dejar de sufrir. ",
             "Que una persona odie a otra es suficiente para que este sentimiento se adueñe de toda la humanidad. "]
list_foods = ["Pollo", "Panchos", "Filete", "Papas", "Arroz", "Galletas", "Pan"]

def trans_list(number):
    list = ""
    if number == 1:
        list = list_cheerful
    elif number == 2:
        list = list_furniture
    elif number == 3:
        list = list_drinks
    elif number == 4:
        list = list_hate
    elif number == 5:
        list = list_foods
    return list
print("")
for number in range(1, 5):
    list_select = trans_list(number)
    sleep(1)
    random_number = random.randint(0, (len(list_select) - 1))
    print("\n" +list_select[random_number])
print("")
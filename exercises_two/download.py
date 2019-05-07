from time import sleep

import datetime



NIGHT_STARTS = 19

DAY_STARTS = 8

HOUR_DURATION = 1




def write_file_and_screen(text, file_name):

    with open(file_name, "a") as hours_file:

        hours_file.write("{}{}".format(text, "\n"))

        print(text)

def alarm():

    print("¿A que hora desea la alarma?")
    hour = input()
    print("Que día desea que suene ( Todos [T] - Lunesa a Viernes [LV] Personalizado [P] )")
    answer = input().upper()
        if answer == "P":
            condition = True
            while condition:
                print("Ingrese un día o escriba \"Listo\" para continuar\n( Lunes [L] - Martes [Ma] - Miercoles [Mi]"
                        " - Jueves [J] - Viernes [V] - Sábado [S] - Domingo [D] )")
                input()





def main():

    answer = input("¿Desea programar una alarma? [Si/No]")
    answer.upper()
    if answer == "SI":
        alarm()

    current_time = datetime.datetime.now()

    is_night = False

    while True:

        sleep(HOUR_DURATION)

        current_time += datetime.timedelta(hours=1)

        light_changed = False



        if (current_time.hour >= NIGHT_STARTS or current_time.hour <= DAY_STARTS) and not is_night:

            is_night = True

            light_changed = True



        elif (current_time.hour > DAY_STARTS and current_time.hour < NIGHT_STARTS) and is_night:

            is_night = False

            light_changed = True



        if light_changed:

            if is_night:

                write_file_and_screen("Se ha hecho de noche", "horas.txt")

            else:

                write_file_and_screen("Se ha hecho de día", "horas.txt")



        write_file_and_screen("La hora actual es {}".format(current_time), "horas.txt")





if __name__ == "__main__":

    main()
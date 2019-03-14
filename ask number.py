import getpass

number_2 = 0
print("")
number_1 = input("Ingrese el número a adivinar: ")
print("")
print("")

while number_1 != number_2:
    number_2 = input("¡Ingrese un número para ganar su premio!: ")
    if number_1 != number_2:
        print("¡Has perdido")
        print("")

print("")
print("¡Has ganado una palmadita en la espalda!")
print("")
print("")
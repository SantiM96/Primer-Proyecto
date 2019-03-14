
result = 0

print("")
print("Bienvenido al conversor de unidades entre Celsius y Farenheit")
print("")

unity_1 = input("Ingrese la unidad que desea cambiar( C / F ): ").upper()
if unity_1 == "C":
    unity_2 = "F"
elif unity_1 == "F":
    unity_2 = "C"
else:
    print("Ingrese un valor de los indicados( C / F )")

if unity_1 == "C":
    value_1 = input("Ingrese el valor en grados Celsius a convertir: ")
    result = 1.8 * value_1 + 32
    print("{} grados Celsius equivale a {} ".format(unity_1, unity_2))
elif unity_1 == "F":
    result = (value_1 - 32)/1.8


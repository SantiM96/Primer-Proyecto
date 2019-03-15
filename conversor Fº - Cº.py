
print("")
print("Bienvenido al conversor de unidades entre Celsius y Farenheit")
print("")

unity_1 = input("Ingrese la unidad que desea cambiar( C / F ): ").upper()
while unity_1 != "C" and unity_1 != "F":
    unity_1 = input("Ingrese una de las unidades indicadas( C / F )").upper()
print("")

if unity_1 == "C":
    unity_2 = "F"
elif unity_1 == "F":
    unity_2 = "C"

if unity_1 == "C":
    value_1 = float(input("Ingrese el valor en grados Celsius a convertir: "))
    result = 1.8 * value_1 + 32
    print("")
    print(value_1, "º Celsius equivalen a {0:.2f}º Farenheit".format(result))
elif unity_1 == "F":
    value_1 = float(input("Ingrese el valor en grados Farenheit a convertir: "))
    result = (value_1 - 32)/1.8
    print("")
    print(value_1, "º Farenheit equivalen a {0:.2f}º Celsius".format(result))
print("")
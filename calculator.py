
print("")
print("Bienvenido a la calculadora")

result = 0

print("")
number_1 = int(input("Ingrese el primer número: "))
sig = input("¿Que operación desesa realizar?( + : - : X : / )").upper()
number_2 = int(input("Ingrese el segundo número: "))

if sig == "+":
    result = number_1 + number_2
elif sig == "-":
    result = number_1 - number_2
elif sig == "X":
    result = number_1 * number_2
elif sig == "/":
    result = number_1 / number_2

print("")
print("Resultado: {}".format(result))
print("")
print("")


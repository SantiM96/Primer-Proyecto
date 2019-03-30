sueldo = 0

print("")
input("Presione enter para comenzar")
print("")

sueldo = float(input("Ingrese su sueldo neto en pesos para iniciar el cálculo de IRPF: "))
print("")
print("")



if sueldo < 29080:
    print("Usted no pagará IRPF")

elif sueldo > 29080 and sueldo < 41543:
    print("Funcionoooo")


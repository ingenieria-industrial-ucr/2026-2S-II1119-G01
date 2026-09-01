from eii_utils import leer_flotante, limpiar_consola

horas:float=0
salario:float=0
tarifa:float=0

limpiar_consola()
horas = leer_flotante("Digite la cantidad de horas")
tarifa = leer_flotante("Digite la tarifa")

if horas > 40:
    salario = 40 * tarifa + (horas - 40) * tarifa * 1.5
else:
    salario = horas * tarifa

print(f"Su salario es {salario}")
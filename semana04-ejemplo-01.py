from eii_utils import leer_booleano, leer_entero, limpiar_consola

# declaracion de variables
ingresos:int=0
deudas:int=0
historial_limpio:bool=True
resultado:bool=True
#inputs
limpiar_consola()
ingresos = leer_entero('Digite los ingresos: ')
deudas = leer_entero('Digite las deudas: ')
historial_limpio = leer_booleano('Tiene el historial limpio')
#process
resultado = ingresos >= 600000 and deudas < 200000 and historial_limpio
#output
print(resultado)
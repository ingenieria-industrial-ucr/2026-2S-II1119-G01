from eii_utils import leer_booleano, limpiar_consola
# variables
costo:int =  400000
extra_ram:bool = True
extra_ssd:bool = True
extra_garantia:bool = True

#inputs
limpiar_consola()
extra_ram = leer_booleano("Desea RAM adicional")
extra_ssd = leer_booleano("Desea un SSD adicional")
extra_garantia = leer_booleano("Desea garantia adicional")

#process
if extra_ram:
    costo = costo + 35000

if extra_ssd:
    costo = costo + 45000

if extra_garantia:
    costo = costo + 25000

print(f"El costo final es {costo} colones")
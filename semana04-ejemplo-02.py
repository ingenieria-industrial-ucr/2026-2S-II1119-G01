from eii_utils import limpiar_consola, leer_booleano, leer_entero, leer_flotante

nota:float=0
ingresos:int=0
zona_riesgo:bool=True
resultado:bool=True

limpiar_consola()
nota = leer_flotante("Digite su nota: ")
ingresos = leer_entero("Digite los ingresos familiares: ")
zona_riesgo = leer_booleano("Usted vive en zona de riesgo: ")

resultado = nota >= 90 and (ingresos < 400000 or zona_riesgo)

print(resultado)
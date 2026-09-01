from eii_utils import limpiar_consola, leer_entero, imprimir_titulo_decorado

# variables
numero_lote:int = 0

# input
limpiar_consola()
imprimir_titulo_decorado("EVALUADOR DE LOTES",40)
numero_lote = leer_entero("Digite el número de lote")

if numero_lote % 2 == 0:
    print("Lote par")
else:
    print("Lote impar")
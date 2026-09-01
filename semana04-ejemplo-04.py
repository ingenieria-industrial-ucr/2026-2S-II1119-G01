from eii_utils import leer_entero, limpiar_consola, imprimir_mensaje, imprimir_error

# variables
edad:int = 0

#inputs
limpiar_consola()
edad = leer_entero("Digite su edad ")

# process output

if edad >= 18:
    imprimir_mensaje("Acceso permitido")
else:
    imprimir_error("Requiere acompañante")
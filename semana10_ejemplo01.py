from eii_utils import leer_entero, limpiar_consola

limpiar_consola()
x:int = leer_entero("Digite x")
y:int = leer_entero("Digite y")
z:int = leer_entero("Digite z")

def obtener_mayor(a:int, b:int) -> int:
    if a > b:
        return a
    else:
        return b

def obtener_mayores(a:int, b:int, c:int) -> int:
    salida:int = obtener_mayor(a, b)
    salida = obtener_mayor(salida, c)
    return salida

print("Mayor de X o Y es ", obtener_mayor(x, y))
print("Mayor de los tres números es ", obtener_mayores(x,y,z))
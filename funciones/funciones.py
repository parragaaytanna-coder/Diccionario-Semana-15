print ("-------BIENVENIDO AL SISTEMA DE CALIFICACIONES-------")
def calcular_promedio(n1, n2, n3):
    promedio= (n1 + n2 + n3) / 3
    return promedio
n1 = float(input("Ingresa la primera nota: "))
n2 = float(input("Ingresa la segunda nota: "))
n3 = float(input("Ingresa la tercera nota: "))
resultado= calcular_promedio(n1, n2, n3)
print("El promedio es: ", resultado)
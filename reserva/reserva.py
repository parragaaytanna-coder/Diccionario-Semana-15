asientos= [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
f= int(input("Ingrese el numero de fila(0-2): "))
c= int(input("Ingrese el numero de columna(0-3): "))
asientos[f][c]=1
print("Asientos reservados:")
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
estructura = len(muro)
filas = 5
columnas = 5
#Se define con antelación el número de filas y columnas del laberinto
laberinto = [[]]
for l in range(filas - 1):
    laberinto += [[]]

def comparacion(i, j):
    haymuro = False
    for valor in range(estructura):
        if muro[valor] == (i, j):
            laberinto[i].append("X")
            haymuro = True
            break
    if haymuro == False:
        laberinto[i].append(" ")
    return laberinto

for i in range(filas):
    for j in range(columnas):
        comparacion(i, j)

laberinto[filas - 1][len(laberinto[filas - 1]) - 1] = "S"
for z in range(len(laberinto) - 1):
    print(str(laberinto[z]) +  ",")
print(laberinto[len(laberinto) - 1])
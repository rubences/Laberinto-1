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

def despliegue_laberinto():
    for z in range(len(laberinto) - 1):
        print(str(laberinto[z]) +  ",")
    print(laberinto[len(laberinto) - 1])
despliegue_laberinto()

for i in range(filas):
    laberinto[i].append("X")
for i in range(filas):
    laberinto[i] = ["X"] + laberinto[i]
techo_y_suelo = [["X"]]
for i in range(columnas + 1):
    techo_y_suelo[0] += ["X"]
laberinto = techo_y_suelo + laberinto
laberinto += techo_y_suelo
#Se añaden dos filas/columnas al laberinto por cada lado para evitar errores al comparar con las casillas de alrededor

i = 1
j = 1
movimientos = []
condicion = True
while condicion:
    laberinto[i][j] = "*"
    if laberinto[i + 1][j] == "S" or laberinto[i - 1][j] == "S" or laberinto[i][j+ 1] == "S" or laberinto[i - 1][j] == "S":
        if laberinto[i + 1][j] == "S":
            movimientos += ["Abajo"]
        elif laberinto[i - 1][j] == "S":
            movimientos += ["Arriba"]
        elif laberinto[i][j + 1] == "S":
            movimientos += ["Derecha"]
        elif laberinto[i][j - 1] == "S":
            movimientos += ["Izquierda"]
        break
    elif laberinto[i + 1][j] == " " or laberinto[i - 1][j] == " " or laberinto[i][j+ 1] == " " or laberinto[i - 1][j] == " ":
        if laberinto[i + 1][j] == " ":
            movimientos += ["Abajo"]
            i += 1
        elif laberinto[i - 1][j] == " ":
            movimientos += ["Arriba"]
            i -= 1
        elif laberinto[i][j + 1] == " ":
            movimientos += ["Derecha"]
            j += 1
        elif laberinto[i][j - 1] == " ":
            movimientos += ["Izquierda"]
            j -= 1
    else:
        laberinto[i][j] = "*"
        movimientos += ["Sin salida"]
        break

laberinto.pop()
laberinto.pop(0)
for c in range(min(columnas, filas)):
    laberinto[c].pop()
    laberinto[c].pop(0)
#Se elimina la capa de muros que se había añadido tras ya hacer el recorrido
print("")
despliegue_laberinto()
print(movimientos)

#Yo no he contado la posición inicial como un movimiento, y por eso solo salen 3 abajos en la lista en vez de 4
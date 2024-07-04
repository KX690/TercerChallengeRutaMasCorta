from collections import deque

# Definición de la matriz y direcciones
matriz = [
    [0,1,2,3,4,5,6,7,8,9],
    [1,0,0,0,0,0,0,1,1,1],
    [2,0,1,0,1,0,0,1,0,1],
    [3,0,1,0,1,0,0,1,0,0],
    [4,0,1,0,1,0,1,1,1,0],
    [5,0,1,0,1,0,1,0,0,0],
    [6,0,1,0,1,0,1,0,1,0],
    [7,0,0,0,0,0,0,0,0,0],
    [8,0,1,0,1,1,0,1,1,0],
    [9,1,1,0,0,0,0,0,0,0]
]

direcciones = [[1, 0], [0, -1], [-1, 0], [0, 1]]
filas=10
columnas=10
visitado = [[False] * columnas for _ in range(filas)] 
anterior = [[None] * columnas for _ in range(filas)]

class Nodo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def imprimir_matriz(matriz):
    #Imprime la matriz
    for i, fila in enumerate(matriz):
        
        
        for j, celda in enumerate(fila):
            
        
            if i == 0 or j == 0:
                if(j==0):
                    print(f'\033[32m{celda}\033[0m  ', end=' ')
                else:    
                    print(f'\033[32m{celda}\033[0m', end=' ')
                
                if(i==0 and j==9):
                    print()
                    
            elif matriz[i][j]==1:
                print(f'\033[31m{celda}\033[0m', end=' ')
            elif matriz[i][j]=='#':                                         # El # indica el recorrido que uso, se imprime en amarillo
                print(f'\033[33m{celda}\033[0m', end=' ')
            elif matriz[i][j]=='*':                                         # El * indica los obstaculos, se imprime en azul
                print(f'\033[34m{celda}\033[0m', end=' ')
                
            elif matriz[i][j]=='S' or matriz[i][j]=='E':                    # La S indica la llegada y la E indica la salida
                print(f'\033[35m{celda}\033[0m', end=' ')
                
                
            else:
                print(celda, end=' ')
        print()

def bfs(entrada, salida):
    
    cola = deque([entrada])
    visitado[entrada[0]][entrada[1]] = True

    while cola:
        actual = cola.popleft()
        if actual == salida:
            break

        for direccion in direcciones:
            x, y = actual[0] + direccion[0], actual[1] + direccion[1]
            if 0 <= x < filas and 0 <= y < columnas and not visitado[x][y] and matriz[x][y] == 0 and not matriz[x][y] =='*' :
                cola.append((x, y))
                visitado[x][y] = True
                anterior[x][y] = actual

    camino = []
    if visitado[salida[0]][salida[1]]:
        actual = salida
        while actual:
            camino.append(actual)
            actual = anterior[actual[0]][actual[1]]
        camino.reverse()

    return camino

def agregar_interferencia():
    
    obstaculos=int(input("\033[32m¿Cuantos obstaculos desea colocar? \n Obstaculos: \033[0m"))
    
    for i in range(obstaculos):
        
        x_obstaculo=int(input(f"{i+1}. Columna del obstaculo: "))
        y_obstaculo=int(input(f"{i+1}. Fila del obstaculo: "))
        print()
        matriz[y_obstaculo][x_obstaculo]='*'
    
def main():
    imprimir_matriz(matriz)
    print("\t\t \033[31m Inicio \033[0m")
    x_entrada = int(input("Introduzca su posición de entrada en columna: "))
    y_entrada = int(input("Introduzca su posición de entrada en fila: "))
    print()
    entrada = (y_entrada, x_entrada)
    
    matriz[y_entrada][x_entrada]='S'
    print("\t\t \033[31m Fin \033[0m")
    x_salida = int(input("Introduzca su posición de salida en columna: "))
    y_salida = int(input("Introduzca su posición de salida en fila: "))
    print()
    salida = (y_salida, x_salida)
    
    agregar_interferencia()
    
    camino = bfs( entrada, salida)

    if camino:
        
        for (x, y) in camino:
            if (x, y) == entrada :
                matriz[x][y] = 'E'
            elif (x, y) == salida:
                matriz[x][y] = 'S'
            elif (x, y) != entrada or (x, y) != salida:
                matriz[x][y]='#'
        imprimir_matriz(matriz)
        print("\033[32mA llegado a su destino\033[0m")
    else:
        print("\033[31mNo hay forma de llegar al lugar, una pena ='( \033[0m")

if __name__ == "__main__":
    main()

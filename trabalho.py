import numpy as np
import math

def det2x2(matriz):
    det = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    return det

def det3x3(matriz):
    det = matriz[0][0]*matriz[1][1]*matriz[2][2] + matriz[0][1]*matriz[1][2]*matriz[2][0] + \
        matriz[0][2]*matriz[1][0]*matriz[2][1] - (matriz[0][2]*matriz[1][1]*matriz[2][0] + \
        matriz[0][0]*matriz[1][2]*matriz[2][1] + matriz[0][1]*matriz[1][0]*matriz[2][2])
    return det

def del_linha(matriz,linha):
    return np.delete(matriz,(linha),axis=0)
def del_coluna(matriz,coluna):
    return np.delete(matriz,(coluna), axis=1)

def det4x4(matriz):
    matriz1 = del_linha(matriz,0)
    matriz1 = del_coluna(matriz1,0)
    
    matriz2 = del_linha(matriz,1)
    matriz2 = del_coluna(matriz2,0)

    matriz3 = del_linha(matriz,2)
    matriz3 = del_coluna(matriz3,0)

    matriz4 = del_linha(matriz,3)
    matriz4 = del_coluna(matriz4,0)

    det = pow(-1,2)*matriz[0][0]*det3x3(matriz1) + pow(-1,3)*matriz[1][0]*det3x3(matriz2) \
        + pow(-1,4)*matriz[2][0]*det3x3(matriz3) + pow(-1,5)*matriz[3][0]*det3x3(matriz4)
    return det

def inversa(matriz):
    matrizout = []
    matrizout1 = []
    aux1 =[]

    det1 = del_linha(matriz,0)
    det1 = del_coluna(det1,0)

    det2 = del_linha(matriz,0)
    det2 = del_coluna(det2,1)

    det3 = del_linha(matriz,1)
    det3 = del_coluna(det3,0)

    det4 = del_linha(matriz,1)
    det4 = del_coluna(det4,1)

    lista = [det1,det2,det3,det4]
    a = 0
    b = 0
    for z in lista:
        if b == 2:
            b = 0
            a += 1
        aux.append(pow(-1,a+b+2)*z[0][0])
        matrizout.append(aux[:])
        aux.clear()
        b+=1
    matrizout1 = []
    aux1 =[]
    for x in matrizout:
        aux1.append(x[0])
    matrizout1.append([aux1[0],aux1[1]])
    matrizout1.append([aux1[2],aux1[3]])

    def transposta(m):
        matriztransposta = []
        rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
        for row in rez:
            matriztransposta.append(row)
        return matriztransposta
    x=np.array(transposta(matrizout1)) * int(1/det2x2(matriz))
    return x

matriz = []
dimensao = int(input('Qual a dimensão dessa matriz? '))
str=''
aux = []
for x in range(0,dimensao):
    print("Separe os numeros por virgula.")
    print(f'Digite a linha {x+1}: ')
    str = input()
    #'1,2,3,4'
    str_split = str.split(',')
    #['1','2','3','4']
    for i in str_split:
        if i != ' ':
            aux.append(int(i))
            #[1,2,3,4]
    matriz.append(aux[:])
    #[[1,2,3,4]]
    aux.clear()

if dimensao == 2:
    print(f'O determinante da matriz {matriz} é {det2x2(matriz)}')
    print(f'Pv: det = {np.linalg.det(matriz):.2f}')
    print(f'A inversa:\n {inversa(matriz)}')

if dimensao == 3:
    print(f'O determinante da matriz {matriz} é {det3x3(matriz)}')
    print(f'Pv: det = {np.linalg.det(matriz):.2f}')

if dimensao == 4:
    print(f'O determinante da matriz {matriz} é {det4x4(matriz)}')
    print(f'Pv: det = {np.linalg.det(matriz):.2f}')

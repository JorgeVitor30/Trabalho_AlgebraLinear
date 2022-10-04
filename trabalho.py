import numpy as np

def det2x2(matriz):
    det = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    return det

def det3x3(matriz):
    det = matriz[0][0]*matriz[1][1]*matriz[2][2] + matriz[0][1]*matriz[1][2]*matriz[2][0] + \
        matriz[0][2]*matriz[1][0]*matriz[2][1] - (matriz[0][2]*matriz[1][1]*matriz[2][0] + \
        matriz[0][0]*matriz[1][2]*matriz[2][1] + matriz[0][1]*matriz[1][0]*matriz[2][2])
    return det

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

def del_linha(matriz,linha):
    return np.delete(matriz,(linha),axis=0)
def del_coluna(matriz,coluna):
    return np.delete(matriz,(coluna), axis=1)

def printamatriz(matriz):
    cont = 0
    for x in matriz:
        print(f"{'|':<3}", end='')
        for y in x:
            print(f'{y:<6.1f}', end='')
            cont += 1
            if cont == len(x):
                print(f"{'|':<3}")
        cont = 0

def transposta(m):
    matriztransposta = []
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    for row in rez:
        matriztransposta.append(row)
    return matriztransposta

def inversa2x2(matriz):
    if det2x2(matriz) == 0:
        return print('  Não possui matriz inversa. Determinante = 0.')

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
    aux2 = []
    for z in lista:
        if b == 2:
            b = 0
            a += 1
        aux2.append(pow(-1,a+b+2)*z[0][0])
        matrizout.append(aux2[:])
        aux2.clear()
        b+=1
    matrizout1 = []
    aux1 =[]
    for x in matrizout:
        aux1.append(x[0])
    matrizout1.append([aux1[0],aux1[1]])
    matrizout1.append([aux1[2],aux1[3]])
    x=np.array(transposta(matrizout1)) * float(1/det2x2(matriz))
    return printamatriz(x)

def inversa3x3(matriz):


    matrizout = []
    matrizout1 = []
    aux1 =[]
    
    det1 = del_linha(matriz,0)
    det1 = del_coluna(det1,0)
    
    det2 = del_linha(matriz,0)
    det2 = del_coluna(det2,1)
    
    det3 = del_linha(matriz,0)
    det3 = del_coluna(det3,2)
    
    det4 = del_linha(matriz,1)
    det4 = del_coluna(det4,0)
    
    det5 = del_linha(matriz,1)
    det5 = del_coluna(det5,1)
    
    det6 = del_linha(matriz,1)
    det6 = del_coluna(det6,2)
   
    det7 = del_linha(matriz,2)
    det7 = del_coluna(det7,0)
    
    det8 = del_linha(matriz,2)
    det8 = del_coluna(det8,1)
    
    det9 = del_linha(matriz,2)
    det9 = del_coluna(det9,2)
   
    lista = [det2x2(det1),det2x2(det2),det2x2(det3),det2x2(det4),det2x2(det5)\
            ,det2x2(det6),det2x2(det7),det2x2(det8),det2x2(det9)]
    

    a = 0
    b = 0
    aux2 = []
    for z in lista:
        if b == 3:
            b = 0
            a += 1
        aux2.append(pow(-1,a+b+2)*z)
        matrizout.append(aux2[:])
        aux2.clear()
        b+=1

    matrizout1 = []
    aux1 =[]
    for x in matrizout:
        aux1.append(x[0])
    matrizout1.append([aux1[0],aux1[1],aux1[2]])
    matrizout1.append([aux1[3],aux1[4],aux1[5]])
    matrizout1.append([aux1[6],aux1[7],aux1[8]])

    x = np.array(transposta(matrizout1)) * float(1/det3x3(matriz))
    return printamatriz(x)

def inversa4x4(matriz):
    matrizout = []
    matrizout1 = []
    aux1 =[]
    
    det1 = del_linha(matriz,0)
    det1 = del_coluna(det1,0)
    
    det2 = del_linha(matriz,0)
    det2 = del_coluna(det2,1)
    
    det3 = del_linha(matriz,0)
    det3 = del_coluna(det3,2)
    
    det4 = del_linha(matriz,0)
    det4 = del_coluna(det4,3)
    
    det5 = del_linha(matriz,1)
    det5 = del_coluna(det5,0)
    
    det6 = del_linha(matriz,1)
    det6 = del_coluna(det6,1)
   
    det7 = del_linha(matriz,1)
    det7 = del_coluna(det7,2)
    
    det8 = del_linha(matriz,1)
    det8 = del_coluna(det8,3)
    
    det9 = del_linha(matriz,2)
    det9 = del_coluna(det9,0)
    
    det10 = del_linha(matriz,2)
    det10 = del_coluna(det10,1)
    
    det11 = del_linha(matriz,2)
    det11 = del_coluna(det11,2)
    
    det12 = del_linha(matriz,2)
    det12 = del_coluna(det12,3)
    
    det13 = del_linha(matriz,3)
    det13 = del_coluna(det13,0)
    
    det14 = del_linha(matriz,3)
    det14 = del_coluna(det14,1)
    
    det15 = del_linha(matriz,3)
    det15 = del_coluna(det15,2)
    
    det16 = del_linha(matriz,3)
    det16 = del_coluna(det16,3)
    
    
   
    lista = [det3x3(det1),det3x3(det2),det3x3(det3),det3x3(det4),det3x3(det5)\
            ,det3x3(det6),det3x3(det7),det3x3(det8),det3x3(det9),det3x3(det10)\
            ,det3x3(det11),det3x3(det12),det3x3(det13),det3x3(det14),det3x3(det15),det3x3(det16)]
    
    a = 0
    b = 0
    aux2 = []
    for z in lista:
        if b == 4:
            b = 0
            a += 1
        aux2.append(pow(-1,a+b+2)*z)
        matrizout.append(aux2[:])
        aux2.clear()
        b+=1
        
    matrizout1 = []
    aux1 =[]
    for x in matrizout:
        aux1.append(x[0])
    matrizout1.append([aux1[0],aux1[1],aux1[2],aux1[3]])
    matrizout1.append([aux1[4],aux1[5],aux1[6],aux1[7]])
    matrizout1.append([aux1[8],aux1[9],aux1[10],aux1[11]])
    matrizout1.append([aux1[12],aux1[13],aux1[14],aux1[15]])

    x = np.array(transposta(matrizout1)) * float(1/det4x4(matriz))
    return printamatriz(x)

def mudancadebase2x2(base1,base2):
    a = [[base2[0][0],base2[1][0]],[base2[0][1],base2[1][1]]]
    b = base1[0]

    #A função solve resolve sistema de equações
    resultado = np.linalg.solve(a,b)
    valor_x1 = resultado[0]
    valor_y1 = resultado[1]

    a = [[base2[0][0],base2[1][0]],[base2[0][1],base2[1][1]]]
    b = base1[1]

    resultado = np.linalg.solve(a,b)
    valor_x2 = resultado[0]
    valor_y2 = resultado[1]

    matriz = [[valor_x1,valor_x2],[valor_y1,valor_y2]]
    return printamatriz(matriz)

def mudancadebase3x3(base1,base2):
    matriz = []
    a = [[base2[0][0],base2[1][0],base2[2][0]],[base2[0][1],base2[1][1],base2[2][1]],\
    [base2[0][2],base2[1][2],base2[2][2]]]
    for x in range(3):
        b = base1[x]
        resultado1 = list(np.linalg.solve(a,b))
        matriz.append(resultado1[:])
        resultado1.clear()
    return printamatriz(matriz)

def mudancadebase4x4(base1,base2):
    matriz = []
    a = [[base2[0][0],base2[1][0],base2[2][0],base2[3][0]],[base2[0][1],base2[1][1],base2[2][1],base2[3][1]],
    [base2[0][2],base2[1][2],base2[2][2],base2[3][2]],[base2[0][3],base2[1][3],base2[2][3],base2[3][3]]]
    for x in range(4):
        b = base1[x]
        resultado1 = list(np.linalg.solve(a,b))
        matriz.append(resultado1[:])
        resultado1.clear()
    return printamatriz(matriz)


resp = input('1. Determintante e Inversa.\n2. Matriz de mudança de base\n=>')
if resp == '1':
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
        print('-'*50)
        print("A matriz: ")
        print()
        printamatriz(matriz)
        print()
        print(f'O determinante da matriz é {det2x2(matriz)}')
        print()
        print(f'Pv: det = {np.linalg.det(matriz):.2f}')
        print()
        print('A inversa:')
        print()
        inversa2x2(matriz)
        print()
        print('-'*50)
    if dimensao == 3:
        print('-'*50)
        print("A matriz: ")
        print()
        printamatriz(matriz)
        print()
        print(f'O determinante da matriz é {det2x2(matriz)}')
        print()
        print(f'Pv: det = {np.linalg.det(matriz):.2f}')
        print()
        print('A inversa:')
        print()
        inversa3x3(matriz)
        print()
        print('-'*50)
    if dimensao == 4:
        print('-'*50)
        print("A matriz: ")
        print()
        printamatriz(matriz)
        print()
        print(f'O determinante da matriz é {det4x4(matriz)}')
        print()
        print(f'Pv: det = {np.linalg.det(matriz):.2f}')
        print()
        print('A inversa:')
        print()
        inversa4x4(matriz)
        print()
        print('-'*50)
if resp == '2':
    dimensao = int(input('Qual a dimensão das bases? '))
    aux = []
    str=''
    base1 = []
    base2 = []
    print("Separe os numeros por virgula.")
    print("Base 1:")
    for x in range(dimensao):
        print(f'Digite a linha {x+1}: ')
        str=input()
        str_split = str.split(',')
        for i in str_split:
            if i != ' ':
                aux.append(int(i))
        base1.append(aux[:])
        aux.clear()
    print("Separe os numeros por virgula.")
    print("Base 2:")
    for x in range(dimensao):
        print(f'Digite a linha {x+1}: ')
        str=input()
        str_split = str.split(',')
        for i in str_split:
            if i != ' ':
                aux.append(int(i))
        base2.append(aux[:])
        aux.clear()

    if dimensao == 2:
        print('-'*50)
        print("A base1: ")
        printamatriz(base1)
        print("A base2: ")
        printamatriz(base2)
        print()
        print("A matriz de mudança de base: ")
        print()
        mudancadebase2x2(base1,base2)
        print()
        print('-'*50)
    if dimensao == 3:
        print('-'*50)
        print("A base1: ")
        printamatriz(base1)
        print("A base2: ")
        printamatriz(base2)
        print()
        print("A matriz de mudança de base: ")
        print()
        mudancadebase3x3(base1,base2)
        print()
        print('-'*50)
    if dimensao == 4:
        print('-'*50)
        print("A base1: ")
        printamatriz(base1)
        print("A base2: ")
        printamatriz(base2)
        print()
        print("A matriz de mudança de base: ")
        print()
        mudancadebase4x4(base1,base2)
        print()
        print('-'*50)

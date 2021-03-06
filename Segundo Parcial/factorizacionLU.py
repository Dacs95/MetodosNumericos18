'''
Factorizacion LU

La matriz a se puede descomponer en dos matrices

    A = L U

Sistema a resolver

x1 + 2x2 + 4x3 = 11
4x1 + x2 - x3 = 0
2x1 + 5x2 + 2x2 = 3

'''



def createMatrix(m,n,v):
    C = []
    for i in range(m):
        C.append([])
        for j in range(n):
            C[i].append(v)
    return C

A = createMatrix(3,3,0)
A[0] = [1 , 1 , 1]
A[1] = [1 , -1 , 0]
A[2] = [-1 , 0 , 1]

U = createMatrix(3,3,0)
U[0] = [1,1,1]
U[1] = [1,-1,0]
U[2] = [-1,0,1]

L = createMatrix(3,3,0)
L[0] = [1,0,0]
L[0] = [0,1,0]
L[0] = [0,0,1]

for i in range(3):
    # a es mi pivote
    a = U[i][i]
    if a == 0:
        print("La matriz no tiene LU")
    for j in range(i+1,3):
        # Obtener el valor abajo de la columna del pivote
        b = U[j][i]
        # c -> factor que se va a multiplicar 
        c = (-1 * b)/a
        L[j][i] = -1*c
        # T temporal
        T = createMatrix(1,3,0)
        for k in range(3):
            T[0][k] = c * U[i][k]
        for k in range(3):
            U[j][k] += T[0][k] 

print(L)
print(U)

#Generar la matriz z 
Z = createMatrix(3,1,0)
C = createMatrix(3,1,0)
C[0] = [20]
C[1] = [5]
C[2] = [4]

for i in range(3):
    Z[i][0] = C[i][0]
    for j in range(3):
        if i == j:
            break
        Z[i][0] -= L[i][j] * Z[j][0]
print(Z)

#Encontrar los resultados en B  utilizando Z y U

B = createMatrix(3,1,0)
for i in range(2,-1,-1):
    B[i][0] = Z[i][0]
    for j in range(2,-1,-1):
        if i == j:
            B[i][0] = B[i][0] / U[i][j]
            break
        B[i][0] -= U[i][j] * B[j][0]
print(B)
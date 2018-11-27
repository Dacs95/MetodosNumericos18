#Método de Newton-Rapson
def createMatrix(m,n,v):
    C = []
    for i in range(m):
        C.append([v]*n)
    return C

def getDimensions(A):
    return (len(A),len(A[0]))

def copyMatrix(B):
    m,n = getDimensions(B)
    A = createMatrix(m,n,0)
    for i in range(m):
        for j in range(n):
            A[i][j] = B[i][j]
    return A

def sumaMatrix(A,B):
    Am,An = getDimensions(A)
    Bm,Bn = getDimensions(B)
    if Am != Bm or An != Bn:
        print("Error las dimensiones deben ser iguales")
        return []
    C = createMatrix(Am,An,0)
    for i in range(Am):
        for j in range(An):
            C[i][j] = A[i][j] + B[i][j]
    return C

def restaMatrix(A,B):
    Am,An = getDimensions(A)
    Bm,Bn = getDimensions(B)
    if Am != Bm or An != Bn:
        print("Error las dimensiones deben ser iguales")
        return []
    C = createMatrix(Am,An,0)
    for i in range(Am):
        for j in range(An):
            C[i][j] = A[i][j] - B[i][j]
    return C

def multMatrix(A,B):
    Am,An = getDimensions(A)
    Bm,Bn = getDimensions(B)
    if An != Bm:
        print("Error las dimensiones deben ser conformable")
        return []
    C = createMatrix(Am,Bn,0)
    for i in range(Am):
        for j in range(Bn):
            for k in range(An):
                    C[i][j] += A[i][k] * B[k][j]
    return C
    
def getAdyacente(A,r,c):
    Am,An = getDimensions(A)
    C = createMatrix(Am-1,An-1,0)
    for i in range(Am):
        if i == r:
            continue
        for j in range(An):
            if j == c:
                continue
            ci = 0
            cj = 0
            if(i < r):
                ci = i
            else:
                ci = i - 1
            if(j < c):
                cj = j
            else:
                cj = j - 1
            C[ci][cj] = A[i][j]
    return C

def detMatrix(A):
    m,n = getDimensions(A)
    if m != n:
        print("La matriz no es cuadrada")
        return []
    if m == 1:
        return A[0][0]
    if m == 2:
        return A[0][0]*A[1][1] - A[1][0]*A[0][1]
    det = 0
    for j in range(m):
        det += ((-1)**j)*A[0][j]*detMatrix(getAdyacente(A,0,j))
    return det


def getMatrizTranspuesta(A):
    m,n = getDimensions(A)
    C = createMatrix(n,m,0)
    for i in range(m):
        for j in range(n):
            C[j][i] = A[i][j]
    return C

def getMatrizAdjunta(A):
    m,n = getDimensions(A)
    if m != n:
        print("La matriz no es cuadrada")
        return []
    C = createMatrix(m,n,0)
    for i in range(m):
        for j in range(n):
            C[i][j] = ((-1)**(i+j))*detMatrix(getAdyacente(A,i,j))
    return C

def getMatrizInversa(A):
    m,n = getDimensions(A)
    if m != n:
        print("La matriz no es cuadrada")
        return []
    detA = detMatrix(A)
    if detA == 0:
        print("La matriz no tiene inversa")
        return []
    At = getMatrizTranspuesta(A)
    adjA = getMatrizAdjunta(At)
    invDetA = 1/detA
    C = createMatrix(m,n,0)
    for i in range(m):
        for j in range(n):
            C[i][j] = invDetA * adjA[i][j]
    return C

##########
# Ejemplo
# x^2 + y^2 = 10 => u
# x^2 - y^2 = 1 => v

def dudx(x,y):
    return 2*x

def dudy(x,y):
    return 2*y

def dvdx(x,y):
    return 2*x

def dvdy(x,y):
    return -2*y

def u(x,y):
    return x**2 + y**2 - 10

def v(x,y):
    return x**2 - y**2 - 1

J = [[dudx,dudy],[dvdx,dvdy]]
F = [[u],[v]]
B = [[1],[1]]
E = 0.01

for i in range(100):
    Ji = createMatrix(2,2,0)
    Jin,Jim = getDimensions(Ji)
    for k in range(Jin):
        for j in range(Jim):
            Ji[k][j] = J[k][j](B[0][0],B[1][0])
    #print(Ji)
    Jinv = getMatrizInversa(Ji)
    #print(Jinv)
    Fi = createMatrix(2,1,0)
    for k in range(2):
        Fi[k][0] = F[k][0](B[0][0],B[1][0])
    Bi = restaMatrix(B,multMatrix(Jinv,Fi))
    Be = restaMatrix(B,Bi)
    if abs(Be[0][0]) < E and abs(Be[1][0]):
        B = Bi
        break
    B = Bi

print("La solucion es",B)
print("u",u(B[0][0],B[1][0]))
print("v",v(B[0][0],B[1][0]))
La solucion es [[2.3452100730812657], [2.1213206700707965]]
u 1.1672151448038903e-05
v 8.901612223333188e-06
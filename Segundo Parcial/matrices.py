#funciones de creacion y operaciones entre matrices.

def createMatrix(m,n,v):
    C = []
    for i in range(m):
        C.append([])
        for j in range(n):
            C[i].append(v)
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

def sumMatrix(A,B):
    Am,An = getDimensions(A)
    Bm,Bn = getDimensions(B)
    if Am != Bm or An != Bn:
        print("Las matrices no son de las mismas dimensiones")
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
        print("Las matrices no son de las mismas dimensiones")
        return []
    C = createMatrix(Am,An,0)
    for i in range(Am):
        for j in range(An):
            C[i][j] = A[i][j] - B[i][j]
    return C

def multiplyMatrix(A,B):
    Am,An = getDimensions(A)
    Bm,Bn = getDimensions(B)
    if An != Bm:
        print("Las dimensiones deben ser conformable")
        return []
    C = createMatrix(Am,Bn,0)
    for i in range(Am):
        for j in range(Bn):
            C[i][j] = 0
            for k in range(An):
                C[i][j] += A[i][k] * B[k][j]
    return C

def detMatrix(A):
    m,n = getDimensions(A)
    if m!=n:
        print("Matriz no es cuadrada")
        return []
    if (n==1):
        return A[0][0]
    if (n==2):
        return (A[0][0]*A[1][1]) - (A[1][0]*A[0][1])
    det = 0
    for j in range(m):
        det += (-1)**j*A[0][j]*detMatrix(getAdyacente(A,0,j))
    return det

def getAdyacente(A,r,c):
    Am,An=getDimensions(A)
    C=createMatrix(Am-1,An-1,0)
    for i in range(Am):
        if i==r:
            continue
        for j in range(An):
            if j==c:
                continue
            if(i<r):
                ci=i
            else:
                ci=i-1
            C[i][j]=A[i][j]     
    return C
            
def getMatrizTranspuesta(A):
    m,n = getDimensions(A)
    C = createMatrix(n,m,0)
    for i in range(m):
        for j in range(n):
            C[j][i] = A[i][j]
    return C
            
def getMatrizAdjunta(A):
    m,n = getDimensions(A)
    if m != n :
        print("La matriz no es cuadrada")
        return []
    C = createMatrix(m,n,0)
    for i in range(m):
        for j in range(n):
            C[i][j] = ((-1)**(i+j))*detMatrix(getAdyacente(A,i,j))
    return C

def getMatrizInversa(A):
    m,n = getDimensions(A)
    if m != n :
        print("La matriz no es cuadrada")
        return []
    detA = detMatrix(A)
    if detA == 0:
        print("La matriz no tiene inversa")
        return []
    At = getMatrizTranspuesta(A)
    adjA = getMatrizAdjunta(At)
    invDetA = 1 / detA
    C = createMatrix(m,n,0)
    for i in range(m):
        for j in range(n):
            C[i][j]= invDetA * adjA[i][j]
    return C


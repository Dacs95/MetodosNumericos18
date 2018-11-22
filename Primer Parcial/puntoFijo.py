#Método de Punto Fijo
'''
Se despeja el polinomio dado, y 
se usa un valor inicial para la
primera aproximación.

Se repite el proceso hasta que 
el error sea menor al solicitado.
''' 

def xnew(xprev):
    return (2*xprev**2 + 3)/5
x0 = 0
iteraciones = 1
for i in range(100):
    x1 = xnew(x0)
    if abs(x1-x0)< 0.000001:
        break
    x0=x1
    iteraciones += 1
print ("La raiz es %.5f" %x1)
print("Número de iteraciones %d"%iteraciones)
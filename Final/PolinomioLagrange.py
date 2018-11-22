'''
Métodos numéricos
Polinomio de Lagrange

Daniel Contreras Segura 

'''
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x = [0,0.33,0.66,1]
y = [1,1.391,1.935,2.718]

pL = ''
for k in range(len(x)):
    pL += str(y[k]) + ' * ('
    Lxk = 1
    for j in range(len(x)):
        if k == j:
            continue
        pL += '(x - %f)*' %(x[j])
        Lxk *= x[k] - x[j]
    
    pL = pL[:-1] + '/%f) +'%(Lxk)
pL = pL[:-1]

#print(pL) #Visualizar el polinomio

expr = sympify(pL)
print(expand(expr))

plt.plot(x,y,'ro')
x2 = np.linspace(0,1,100)
y2 = []
x = symbols('x')
for i in range(len(x2)):
    y2.append(expr.subs(x,x2[i]))
plt.plot(x2,y2)
plt.show()
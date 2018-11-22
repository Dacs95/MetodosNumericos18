#Método Grafico 

'''
Buscamos la raiz de la funcion al tabular 
y  graficar los valores de una función  y 
buscar cuando el valor de y = 0
'''
import numpy as np
import matplotlib.pyplot as plt

def y2(x):
    return 2*x**2 - 5*x + 3

xArray = np.linspace(0,2,100)
print(xArray)
yArray = np.zeros(100)
for i in range (len(xArray)):
    yArray[i] = y2(xArray[i])
plt.plot(xArray,yArray)
plt.grid()
plt.show()
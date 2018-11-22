import math
import numpy as np
import matplotlib.pyplot as plt

def fun(x):
    return x**3 - 7*x**2 + 14*x - 6
'''
def fun(x):
    return x**2 - 10

def fun(c):
    return (667.38/c)*(1- math.exp(-6.81*c)) -40
'''
#imprimir la funcion
xarray = np.linspace(10,25,100)
yarray = np.zeros(100)

for i in range(100):
    yarray[i] = fun(xarray[i])

plt.plot(xarray,yarray)
plt.grid()
plt.show()

#Elegir valores iniciales x0 y x1
#Donde haya un cambio de signo

x0 = 4
x1 = 0

for i in range(100):
    f0 = fun(x0)
    f1 = fun(x1)
    if f0*f1 > 0:
        print("No hay raiz en este rango")
        break
    #x = (x0 + x1)/2
    x = x0 - (f0*(x1-x0)/(f1-f0))
    fx = fun(x)
    if fx*f1 < 0:
        x0 = x
    else:
        x1 = x
    if abs(fx) < 0.005:
        break
print(fun(x0))
print("La raiz es %.3f"%x0)



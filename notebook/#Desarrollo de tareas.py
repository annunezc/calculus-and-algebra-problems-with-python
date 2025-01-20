#Desarrollo de tareas

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Pregunta 1

def distancia(t): 
    return (10*t)

t = np.linspace(0,12,5,100) # Domain
print(distancia(t))

plt.plot(t,distancia(t))
plt.show()

#Ejercicio 2

def distancia(t,a):
    return 1/2*a*t**2

x=np.linspace(0,10,1000)
plt.plot(x,distancia(x,2))
plt.show()
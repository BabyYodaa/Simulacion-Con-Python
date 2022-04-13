# -*- coding: utf-8 -*-
"""
Created on Mon May 10 10:40:26 2021

@author: María Fernanda
"""
#Una fruta al por menor, vendedor vende algo de fruta y hace un pedido de Y unidades todos los días. 
#Cada unidad que se vende da una ganancia de 60 centavos y las unidades que no se venden al final del día se desechan 
#con una pérdida de 40 centavos por unidad. La demanda, d , en un día cualquiera se distribuye uniformemente en [20, 305]. 
#¿Cuántas unidades debería pedir el vendedor para maximizar la ganancia esperada?

#Vamos a denotar la ganancia como g . Cuando intenta crear ecuaciones basadas en la descripción del problema anterior, 
#s denota el número de unidades vendidas, mientras que d denota la demanda, como se muestra en la siguiente ecuación


import numpy as np
from math import log
import matplotlib.pyplot as plt


x=[]
y=[]
#Ecuación que define el Beneficio
def generateProfit(d):

   global s

   if d >= s: 
     return 0.6*s
   else:
     return 0.6*d - 0.4*(s-d)

# estamos ejecutando la simulación para d en [20,305]
maxprofit=0

for s in range (20, 305):
# Ejecutamos una simulación para n = 1000 
  # Incluso si ejecutamos para n = 10.000 el resultado sería
  # sería casi el mismo
  for i in range(1,1000):

    
   # generar un valor aleatorio de d 
     d = np.random.randint(100,high=200)

    # para este valor aleatorio de d, encontrar el beneficio y
     # actualizar el beneficio máximo
     profit = generateProfit(d)
     if profit > maxprofit:
        maxprofit = profit
  
    # almacenar el valor de s para ser trazado en el eje X 
  x.append(s)

  #almacenar el valor de maxprofit trazado en el eje Y 
  y.append(log(maxprofit))  # se traza en escala logarítmica
plt.plot(x,y)
plt.xlabel('Unidades de frutas vendidas')
plt.ylabel('Beneficio máximo obtenido')
plt.title('Beneficio máximo de ventas')
print ("Beneficio máximo:", maxprofit)






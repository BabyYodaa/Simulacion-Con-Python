# -*- coding: utf-8 -*-
"""
Created on Wed May 19 6:23:50 2021


@author: María Fernanda
"""

import numpy as np
import random
import pandas as pd

#Se tiene que el vendedor de frutas planea realizar como proyecto de ampliación de su mercancia,
#el cultivo de hierbas y frutas de todo tipo, para dicho proyecto, estará basado en simulación de Montecarlo

#N representa el número de puntos que generamos. 
#Estos son los números aleatorios que nos ayudarán a definir el tiempo de las labores del cultivo
N = 2000
#La variable TotalTime es una lista que contendrá las N evaluaciones 
#del tiempo total necesario para completar el cultivo
TotalTime=[]
#Finalmente, la variable T es una matriz con N filas y seis columnas 
#y contendrá las N evaluaciones del tiempo necesario para completar cada labor individual.
T =  np.empty(shape=(N,6))
#Estimación del tiempo de la tarea
LTimes=[[3,5,9],

           [2,6,8],

           [3,5,9],

           [4,6,10],

           [3,5,9],

           [2,6,8]]
#Esta matriz contiene los tres tiempos para cada fila representativa de las seis labores: 
#tiempo optimo, tiempo deporable y Tiempo probable.

#generar el valor de separación de la distribución triangular
Lh=[]

for i in range(6):

    Lh.append((LTimes[i][1]-LTimes[i][0])/(LTimes[i][2]-LTimes[i][0]))

#Dos bucles for y una estructura condicional if para desarrollar la simulación de MonteCarlo   
for p in range(N):

    for i in range(6):

        trian=random.random()

        if (trian < Lh[i]):

            T[p][i] = LTimes[i][0] + np.sqrt(trian*(LTimes[i][1]- LTimes[i][0])*(LTimes[i][2]-LTimes[i][0]))

        else:

           T[p][i]=(LTimes[i][2]-np.sqrt((1-trian))*(LTimes[i][2]-LTimes[i][1])*(LTimes[i][2]-LTimes[i][0]))
#Finalmente, para cada de las N iteraciones, calculamos una estimación del tiempo total para la ejecución del cultivo                 
TotalTime.append( T[p][0]+ np.maximum(T[p][1],T[p][2]) +np.maximum(T[p][3],T[p][4]) + T[p][5])
                 
data=pd.DataFrame(T,columns=['SelecTipoSemilla', 'CalidadSemilla', 'Siembra','Abono', 'Riego','Fumigación'])

pd.set_option('display.max_columns', None)  
#La función describe() genera una serie de estadísticas descriptivas
# que devuelven información útil sobre la dispersión y la forma de distribución de un conjunto de datos.

print(data.describe())  
hist = data.hist(bins=20)

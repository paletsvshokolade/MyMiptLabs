import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#функция для подгонки
linear = lambda x,a,b:a*x+b
x=np.linspace(0,500,500)

#Данные
l50vd = np.array([58,110,98,80,69,49,42,35,56,76])
y1=l50ma = np.array([46.57,87.72,78.44,64.12,55.51,39.572,34.028,28.307,44.746,60.65])
x1=l50vr = l50vd*4

l30vd = np.array([31,50,63,75,84,90,97,108,93,55])
y2=l30ma = np.array([41.03,66.6,83.09,99.73,110.45,118.41,128.04,142.3,122.75,72.18])
x2=l30vr = l30vd*4

l20vd = np.array([38,40,47,52,57,63,68,72,60,48])
y3=l20ma = np.array([75.8,79.74,93.77,103.6,112.8,125.46,134.34,141.92,119.09,96.02])
x3=l20vr = l20vd*4

#подгонка
cfc1,pcov=curve_fit(linear,x1,y1)
cfc2,pcov=curve_fit(linear,x2,y2)
cfc3,pcov=curve_fit(linear,x3,y3)
a1,b1=cfc1
a2,b2=cfc2
a3,b3=cfc3

#обычные графики
plt.plot(l50vr,l50ma, marker='o',label='l=50см')
plt.plot(l30vr,l30ma, marker='o',label='l=30см',color='purple')
plt.plot(l20vr,l20ma, marker='o',label='l=20см')
#подогнанные графики
plt.plot(x,linear(x,a1,b1),color='red')
plt.plot(x,linear(x,a2,b2),color='red')
plt.plot(x,linear(x,a3,b3),color='red')

plt.xlabel('V - напряжение в мВ')
plt.ylabel('I - сила тока в мкА')
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.legend()

plt.show()
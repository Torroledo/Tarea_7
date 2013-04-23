import pylab
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.fftpack import fft , fftfreq
data= pylab.loadtxt('RungeKuttaEdoDataSolution.txt')
t=data[:,0]*(1.5*(10**6))
r=data[:,1]*(1.7*(10**12))
v=data[:,2]*(1.13*(10**6))

# obtener radio de equilibrio 
maximo=max(r)
minimo=min(r)
prom= (maximo+minimo)/2
puntos=[]
# encontrar periodo
for i in range (len(t)):
    if (r[i]>r[i-1]):
        if r[i]>r[i+1]: 
            puntos.append(t[i])
#periodo promedio
per=0
for i in range (len (puntos)-1):
    per+=puntos[i+1]-puntos[i]

periodo= per/ (len (puntos)-1)
periodo_dias= periodo /86400

#imprimir el mensaje 
archivo=open("period_amplitude.txt", "w")
archivo.write("El periodo de oscilacion es: %f dias \nEl radio de equilibrio es: %f cm\n"%(periodo_dias, prom))
archivo.close()

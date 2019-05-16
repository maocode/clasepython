import matplotlib.pyplot as plt
import numpy as np
def m(x):
    return np.sin(x)#Tambien para las funsiones cos,log10 y otras
x=np.linspace(0,10,100)
plt.plot(x,m(x))
plt.xlabel('Tiempo')
plt.ylabel('posicion')
plt.title('FUNSION SENO')
plt.grid()
plt.savefig('funsionseno.png')






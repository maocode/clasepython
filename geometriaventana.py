#========Definiendo la geometria de nuestra ventana=======
from tkinter import *
v=Tk()#llamamos a la clase Tk
v.title("GEOMETRIA DE VENTANA")
#====DIMENCIONES DE NUESTRA VENTANA=======
v.geometry("400x300+600+400")#ancho de la ventana por el largo mas margen isquierda y derecha
v.mainloop()

#=====ADICIONANDO UN WIDGETS LABEL A NUESTRA VENTANA =====

from tkinter import *
v=Tk()
v.title("GUI Interfaz Grafica de Usuario")#Titulo de Nuestra ventana
v.geometry("600x400")#largo y alto
#===========LABEL=================
mensaje= Label(v,text="HOLA MUNDO")
#===========Posicion==============
mensaje.place(x=300, y=150)
v.mainloop()

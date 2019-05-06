#=====ADICIONANDO UN WIDGETS LABEL Y BUTTON A NUESTRA VENTANA =====

from tkinter import *
#====Creamos un funcion para nuestro boton

def boton_click():
   mensaje["text"]="BIENVENIDO AL SISTEMA"
   mensaje["bg"]="#d65a31"
   mensaje["fg"]="#e8e8e8"
   mensaje["font"]="Arial"
#===== Fin de la Funcion
   
def botonsalir_click():
       global v
       v.destroy()

v=Tk()
v.title("GUI Interfaz Grafica de Usuario")#Titulo de Nuestra ventana
v.geometry("600x200+600+500")#largo y alto


#===========LABEL=================
mensaje= Label(v,text="HOLA MUNDO",fg="#e8e8e8")
#===========Posicion==============
mensaje.place(x=300, y=150)
#==========BUTTON=================
boton=Button(v,width=10,text="Saludar",command=boton_click)#llamamos la Funcion boton_click
boton.place(x=300, y=75)#posicionamos nuestro boton
botonsalir=Button(v,width=10,text="Salir",command=botonsalir_click)#llamamos la Funcion command=botonsalir_click
botonsalir.place(x=410, y=75)#posicionamos nuestro boton


v.mainloop()



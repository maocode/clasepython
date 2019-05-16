#========Agregando Entry y Button=======
from tkinter import *
import math
v=Tk()#llamamos a la clase Tk
v.title("TEOREMA DE PITAGORAS")
v.geometry("600x300+600+400")#ancho de la ventana por el largo mas margen isquierda y derecha

#====FUNCIONES CALCULAR- BORAR - CERRAR =======

#funciones para calcular el Teorema de Pitagoras  
def btn_calcula():
    if(str(txt1.get()).isnumeric() and str(txt2.get()).isnumeric()):
       #asignamos el valor de text1 y txt2 a dos variable
        num1=int(txt1.get())
        num2=int(txt2.get())
        # h = math.sqrt(a**2 + b**2)
        num3=math.sqrt(num1**2+num2**2)
       
        
        etqres["text"]=num3
    else:
        etqres["text"]="Valores no validos..."

#funcion Borar Valores
def btn_reset():
    txt1.delete(0, END)
    txt2.delete(0, END)
    etqres["text"]="0"
    txt1.focus_set()
    
        
#funcion cerrar ventana
def btn_salir():
    global v
    v.destroy()

#====FUNCIONES CALCULAR- BORAR - CERRAR  FIN=======

 #====WIDGET LABEL - BUTTON - ENTRY =======   
    
#Labels
etq=Label(v,text="Digite el Primer valor:")
etq.place(x=20, y=100)
etq2=Label(v,text="Digite el Segundo valor:")
etq2.place(x=20, y=150)
etqres=Label(v,text="0")
etqres.place(x=450, y=150)

#casilla de texto 1
txt1=Entry(v)
txt1.place(x=200, y=100)
#casilla de texto 2
txt2=Entry(v)
txt2.place(x=200, y=150)
#botones boton1 boton2 boton3
btn1=Button(v,width=10,text="calcular", command=btn_calcula )
btn1.place(x=150, y=200)
btn2=Button(v,width=10,text="Borrar", command=btn_reset)
btn2.place(x=250, y=200)
btn3=Button(v,width=10,text="Salir",command=btn_salir)
btn3.place(x=350, y=200)



v.mainloop()


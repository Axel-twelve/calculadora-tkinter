
"""Calculadoras mediante el modelo MVC con las librerías Tkinter 
"""


import tkinter as tk ##libreria de tkinter para el lanzamiento de ventanas
from tkinter import ttk ##librería más moderna de tkinter temática
#import TTKBootstrap as tb
##creamos las 3 clases como el MVC


class View(tk.Tk): ##clase vista y heredamos tk
    

    
    #operator=''
    #text_input = StringVar()


    def __init__(self, controller):#añadimos parametros
        super().__init__()
        self.controller=controller ##acceder a la clase controller
        self.mi_frame()
        self.value_Var=tk.StringVar()
        self.title('Mi calculadora_hola') ##titulo de la ventana
        self.titulo_etiqueta()
        self.geometry('600x500')## definimos tamaño de la ventana
        self.boton()
        self.boton2()

    def mi_frame(self):
        self.main_frame=ttk.Frame(self)##creamos el marco o ventana para que salte 
        self.main_frame.pack()#padx=30, pady=30)

    def titulo_etiqueta(self):
        self.la=ttk.Label(self.main_frame, text='Calculadora Hisoka', font=('Arial', 18))
        self.la.pack()#padx=30, pady=50)
    
    numeros= ['1', '2', '3', '4', '5', '6', '7']##botones para que aparezacan
    
    def boton(self):
        for numero in self.numeros:
            oneButton = ttk.Button(self.main_frame, text=numero)
            oneButton.pack(side='left', padx=5, pady=5)


  

    numer2=['8', '9', '0','+','*','/','-','=']

    def boton2(self):##función para que aparezcan todos los botones
        row_num=1
        col_num = 0

        for numero1 in self.numer2:          
            oneButton = ttk.Button( text=numero1,width=25)#command=lambda num=numero: addToEq(1))
            oneButton.place(x=100, y=60)
            oneButton.pack(side='left')#,padx=1, pady=1)
            col_num += 1
            if col_num >3:
                col_num = 0
                row_num += 1

     
            

            
    
    def main(self):###función para lanzar la ventana
        self.mainloop()


class Model: ##clase modelo
    def __init__(self):
        pass

class Controller:##clase controlador
    def __init__ (self):
        self.model=Model()##llamamos a las otras clases
        self.view=View(self)


    def main (self):
        #print('inseles')
        self.view.main()#3llamamos a la funcion de View
   

if __name__=='__main__': ## creamos la inicialización del modelo
    calculator=Controller() ##probando el modelo
    calculator.main() ##llamamos a la funcion del modelo
    

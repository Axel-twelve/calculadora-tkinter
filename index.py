
"""Calculadoras mediante el modelo MVC con las librerías Tkinter 
"""


import tkinter as tk ##libreria de tkinter para el lanzamiento de ventanas
from tkinter import ttk ##librería más moderna de tkinter temática
from tkinter.constants import SUNKEN

##creamos las 3 clases como el MVC


class View(tk.Tk): ##clase vista y heredamos tk
    

    
    #operator=''
    #text_input = StringVar()


    def __init__(self, controller):#añadimos parametros
        super().__init__()
        self.controller=controller ##acceder a la clase controller
        self.mi_frame12()
        self.mi_frame4()
        self.mi_frame()
        self.mi_frame1()
        self.mi_frame2()
        self.value_Var=tk.StringVar()
        self.title('Mi calculadora_hola') ##titulo de la ventana
        #self.titulo_etiqueta()
        self.cuadro()
        self.geometry('500x350')## definimos tamaño de la ventana
        self.boto52()
        self.boton()
        self.boton1()
        self.simbolos()
        self.bot()
        self.mas()
        self.menos()
        
        
    def mi_frame12(self):
        self.main_fr=ttk.Frame(self, height=200, width=100)##creamos el marco o ventana para que salte 
        self.main_fr.pack()#padx=30, pady=30)

    def mi_frame(self):
        self.main_frame=ttk.Frame(self, height=200, width=100)##creamos el marco o ventana para que salte 
        self.main_frame.pack()#padx=30, pady=30)
    
    def mi_frame1(self):
        self.main_frame1=ttk.Frame(self, height=200, width=100)##creamos el marco o ventana para que salte 
        self.main_frame1.pack()#padx=30, pady=30)

    def mi_frame2(self):
        self.main_frame2=ttk.Frame(self)##creamos el marco o ventana para que salte 
        self.main_frame2.pack()#padx=30, pady=30

    def mi_frame4(self):
        self.main_frame3=ttk.Frame(self)# height=200, width=100)##creamos el marco o ventana para que salte 
        self.main_frame3.pack()#padx=30, pady=30)

    def cuadro(self):
        self.rr=tk.Entry(self.main_fr, font=("default, 11"), insertontime=0, bd=5, width=21, borderwidth=10, foreground="#ff0000", highlightthickness=5, highlightcolor="#f5d0d0", highlightbackground="#f5d0d0")#,textvariable=self.value_Var, state='disable')
        self.rr.grid()#side=tk.LEFT)


    def titulo_etiqueta(self):
        self.la=ttk.Label(self.main_frame, text='Calculadora Hisoka', font=('Arial', 18))
        self.la.pack()#padx=30, pady=50)
    
    number=['1','2','3','4','5','6','7','8','9','/']
    simbols=['0','X', '+','/','C','-','=']
    #number= ['4', '5', '6']# '6', '7']##botones para que aparezacan
    
    def boton(self):
        for numero in self.number:
             if numero > '3' and numero < '7':   
                oneButton = tk.Button(self.main_frame, text=numero,width=5, padx=10, pady=10, font=("Arial", 20))
                oneButton.pack(side='left')#, padx=5,pady=5)
    
    def bot(self):
        for numero in self.simbols:
            if numero == '/':
                oneButton = tk.Button(self.main_frame, text=numero,width=5, padx=10, pady=10, font=("Arial", 20), bg='green')
                oneButton.pack(side='left')#, padx=5,pady=5)


    #numeros= ['1', '2', '3', '-']

    def boton1(self):
        for numero in self.number:
            if numero > '0' and numero < '4':
                oneButton1 = tk.Button(self.main_frame1, text=numero,width=5, padx=10, pady=10, font=("Arial", 20))
                oneButton1.pack(side='left')#, padx=10,pady=10)
    
    def mas(self):
        for numero in self.simbols:
            if numero == '+':
                oneButton = tk.Button(self.main_frame1, text=numero,width=5, padx=10, pady=10, font=("Arial", 20), bg='green')
                oneButton.pack(side='left')#, padx=5,pady=5)

    
    def simbolos(self):
        for numero in self.simbols:
            if numero == '0' or numero == 'X' or numero == 'C' or numero =='=':    
                oneButton1 = tk.Button(self.main_frame2, text=numero,width=5, padx=10, pady=10, font=("Arial", 20))#, bg='blue')
                oneButton1.pack(side='left')#,ipadx=20,ipady=30, anchor=tk.E)# padx=10,pady=10)
    
    #numb= ['7', '8', '9','%']

    def boto52(self):
        for numero in self.number:
            if numero > '6' and numero <= '9':    
                oneButton1 = tk.Button(self.main_frame3, text=numero,width=5, padx=10, pady=10, font=("Arial", 20))#, bg='blue')
                oneButton1.pack(side='left')#,ipadx=20,ipady=30, anchor=tk.E)# padx=10,pady=10)

    def menos(self):
        for numero in self.simbols:
            if numero == '-':
                oneButton = tk.Button(self.main_frame3, text=numero,width=5, padx=10, pady=10, font=("Arial", 20), bg='green')
                oneButton.pack(side='left')#, padx=5,pady=5)

    def boton_grid(self):
        bdot = tk.Button(self.main_frame3,activebackground='#73f5d7', bg="#f5f0f0", text=".", padx=22, pady=15)#, command=lambda: insrt("."))
        bdot.grid(row=1, column=3)

        

            
    
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
    

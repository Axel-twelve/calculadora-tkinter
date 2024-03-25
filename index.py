
"""Calculadoras mediante el modelo MVC con las librerías Tkinter 
"""


import tkinter as tk ##libreria de tkinter para el lanzamiento de ventanas
from tkinter import ttk ##librería más moderna de tkinter temática



##creamos las 3 clases como el MVC
class View(tk.Tk): ##clase vista y heredamos tk
     
    #operator=''
    #text_input = StringVar()

    def __init__(self, controller):#añadimos parametros
        super().__init__()
        self.controller=controller ##acceder a la clase controller
        self.mi_frame12()
        self.framegrid()
        self.mi_frame3()
        self.mi_frame()
        self.mi_frame1()
        self.mi_frame2()
        #self.framedrid()
        self.value_Var=tk.StringVar()
        self.title('Mi calculadora_hola') ##titulo de la ventana
        #self.titulo_etiqueta()
        self.cuadro()
        self.geometry('500x450')## definimos tamaño de la ventana
        self.boton_6a9()
        self.boton_3a7()
        self.boton_0a4()
        self.simbolos()
        
        
    
        
    ### ventanas 
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

    def mi_frame3(self):
        self.main_frame3=ttk.Frame(self)# height=200, width=100)##creamos el marco o ventana para que salte 
        self.main_frame3.pack()#padx=30, pady=30)

    def framegrid(self):
        self.frame_grid=ttk.Frame(self)# height=200, width=100)##creamos el marco o ventana para que salte 
        self.frame_grid.pack()#padx=30, pady=30)


    ##pantalla de calculadora
    def cuadro(self):
        self.rr=tk.Entry(self.main_fr, font=("default, 11"), insertontime=0, bd=5, width=21, borderwidth=10, foreground="#ff0000", highlightthickness=5, highlightcolor="#f5d0d0", highlightbackground="#f5d0d0",textvariable=self.value_Var, state='disable')
        self.rr.grid()#side=tk.LEFT)

    
    number=['1','2','3','4','5','6','7','8','9','+','/','-']
    simbols=['0','X', '+','/','.','-','%','C','=']
    
    ##botones de numero 4 al 7 y /
    def boton_3a7(self):
        for numero in self.number:
            if numero > '3' and numero < '7':   
                oneButton = tk.Button(self.main_frame, text=numero,width=5, padx=10, pady=10, font=("Arial", 20),command=lambda num=numero: self.controller.click_boton(num))
                oneButton.pack(side='left')#, padx=5,pady=5)
            elif numero =='/':
                oneButton1 = tk.Button(self.main_frame, text=numero,width=5, padx=10, pady=10, font=("Arial", 20),command=lambda num=numero: self.controller.click_boton(num), bg='lightblue')#, bg='blue')
                oneButton1.pack(side='left')
    
    
    #numero 1 al 3 y +
    def boton_0a4(self):
        for numero in self.number:
            if numero > '0' and numero < '4':
                oneButton1 = tk.Button(self.main_frame1, text=numero,width=5, padx=10, pady=10, font=("Arial", 20), command=lambda num=numero: self.controller.click_boton(num))
                oneButton1.pack(side='left')#, padx=10,pady=10)
            elif numero =='+':
                oneButton1 = tk.Button(self.main_frame1, text=numero,width=5, padx=10, pady=10, font=("Arial", 20),command=lambda num=numero: self.controller.click_boton(num), bg='lightblue')#, bg='blue')
                oneButton1.pack(side='left')
    

    
     
    #simbolos 
    def simbolos(self):
        for numero in self.simbols:
            if numero == '.':    
                oneButton1 = tk.Button(self.main_frame2, text=numero,width=5, padx=10, pady=10, font=("Arial", 20),command=lambda num=numero: self.controller.click_boton(num), bg='lightblue')#, bg='blue')
                oneButton1.pack(side='left')

            elif numero =='=':
                oneButton1 = tk.Button(self.main_frame2, text=numero,width=11, padx=10, pady=10, font=("Arial", 20),command=lambda num=numero: self.controller.click_boton(num), bg='pink')
                oneButton1.pack(side='left')

            elif numero =='0':
                oneButton1 = tk.Button(self.main_frame2, text=numero,width=6, padx=10, pady=10, font=("Arial", 20),command=lambda num=numero: self.controller.click_boton(num))#, bg='blue')
                oneButton1.pack(side='left')

            elif numero =='X' or numero =='%':
                oneButton1 = tk.Button(self.frame_grid, text=numero,width=5, padx=10, pady=10, font=("Arial", 20),command=lambda num=numero: self.controller.click_boton(num), bg='lightblue')
                oneButton1.pack(side='left')
            
            elif numero =='C':
                oneButton1 = tk.Button(self.frame_grid, text=numero,width=10, padx=10, pady=10, font=("Arial", 20),command=lambda num=numero: self.controller.click_boton(num), bg='orange')
                oneButton1.pack(side='left')
    


    def boton_6a9(self):
        for numero in self.number:
            if numero > '6' and numero <= '9':    
                oneButton1 = tk.Button(self.main_frame3, text=numero,width=5, padx=10, pady=10, font=("Arial", 20), command=(lambda num=numero: self.controller.click_boton(num)))
                oneButton1.pack(side='left')#,ipadx=20,ipady=30, anchor=tk.E)# padx=10,pady=10)
            elif numero =='-':
                oneButton1 = tk.Button(self.main_frame3, text=numero,width=5, padx=10, pady=10, font=("Arial", 20),command=(lambda num=numero: self.controller.click_boton(num)), bg='lightblue')
                oneButton1.pack(side='left')



    def main(self):###función para lanzar la ventana
        self.mainloop()

#def boton_arriba(self):
     #   tk.Button(self.frame_grid,activebackground='#73f5d7', bg="#f5f0f0", text="%", padx=50, pady=15).grid(row=6, column=1)# command=lambda num='.': self.controller.click_boton('')).grid(row=6, column=2)
      #  #tk.Button(self.frame_grid,activebackground='#73f5d7', bg="#f5f0f0", text="0", padx=50, pady=15,command=lambda num='0': self.controller.click_boton(num)).grid(row=6, column=0)#, columnspan=2) indica cuantas columnas ocupa
       # tk.Button(self.frame_grid,activebackground='#73f5d7', bg="#f5f0f0", text="x", padx=50, pady=15 ).grid(row=6, column=3)#, columnspan=1)
        #tk.Button(self.frame_grid,activebackground='#73f5d7', bg="#f5f0f0", text="=", padx=50, pady=15 ).grid(row=6, column=4, rowspan=2)
          
##tengo dos opciones una usar el pack pero no se acomodarán como me gusta o la otra es usar el grid
    #otra opcion es aplicar if y elif, en los if irían los nunmero sy en los elif los imbolos

class Model: ##clase modelo
    def __init__(self):
        self.previous_value =''
        self.value=''
        self.operator=''
        
        
    def operaciones(self, numero):
        if numero == 'C':
            self.value = ''
            self.previous_value = ''
            self.operator = ''
        
        
        elif numero == '=':
            value = self._evaluate()
            #if '.0' in str(value):
             #   value = int(value)
            self.value = str(value)
        
        elif numero >='0' and numero <='9':  
            self.value += str(numero)

        #else:
         #   if self.value:
          #      self.operator = numero
           #     self.previous_value = self.value
            #    self.value = ''
        
        return self.value
    
    def _evaluate(self):
        return eval(self.previous_value+self.operator + self.value)

        
class Controller:##clase controlador
    def __init__ (self):
        self.model=Model()##llamamos a las otras clases
        self.view=View(self)


    def main (self):
        
        self.view.main()#llamamos a la funcion de View
   
    def click_boton(self, numero):
        resultado=self.model.operaciones(numero)

        self.view.value_Var.set(resultado)


if __name__=='__main__': ## creamos la inicialización del modelo
    calculator=Controller() ##probando el modelo
    calculator.main() ##llamamos a la funcion del modelo
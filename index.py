
"""Calculadoras mediante el modelo MVC con las librerías Tkinter 
"""

import tkinter as tk ##libreria de tkinter para el lanzamiento de ventanas
from tkinter import ttk ##librería más moderna de tkinter temática



##creamos las 3 clases como el MVC
class View(tk.Tk): ##clase vista y heredamos tk
    def __init__(self, controller):#añadimos atributo
        super().__init__()
        self.controller=controller ##acceder a la clase controller
        self.mi_frame1()##primera fila
        self.mi_frame2()##segunda fila
        self.mi_frame3()##tercera fila
        self.mi_frame4()##cuarta fila
        self.mi_frame5()##quinta fila
        self.mi_frame6()##sexta fila
        self.value_Var=tk.StringVar() ##cambia cada vez que lo llamamos
        self.title('Calculadora Hisoka') ##titulo de la ventana
        self.cuadro()#instancia de la calculadora
        self.geometry('450x425')## definimos tamaño de la ventana
        self.configure(background='black')
        self.boton_num_oper()    
        
        ##pack, grid and place son 3 geometrías las cuales ayudaran al posicionamiento de los widgets

    ### ventanas 
        
    def cuadro(self):#  ##pantalla de calculadora
        self.rr=tk.Entry(self.main_frame1, font=("default, 11"), insertontime=0, bd=5, width=21, borderwidth=10, foreground="#ff0000", highlightthickness=5, highlightcolor="#f5d0d0", highlightbackground="#f5d0d0",textvariable=self.value_Var, state='disable')
        self.rr.grid()

    def mi_frame1(self):
        self.main_frame1=ttk.Frame(self)##creamos el marco para cada fila de la interfaz 
        self.main_frame1.pack()##

    def mi_frame2(self):
        self.main_frame2=ttk.Frame(self)
        self.main_frame2.pack()
    
    def mi_frame3(self):
        self.main_frame3=ttk.Frame(self)
        self.main_frame3.pack()

    def mi_frame4(self):
        self.main_frame4=ttk.Frame(self)
        self.main_frame4.pack()

    def mi_frame5(self):
        self.main_frame5=ttk.Frame(self)
        self.main_frame5.pack()

    def mi_frame6(self):
        self.main_frame6=ttk.Frame(self)
        self.main_frame6.pack()

    number=['1','2','3','4','5','6','7','8','9','0']
    simbols=['*', '+','/','.','-','%','C','=']
    
    #ciclo para todos los botones
    def boton_num_oper(self):
        for numero in self.number:
            if numero > '0' and numero < '4':
                oneButton1 = tk.Button(self.main_frame5, text=numero,width=5, padx=10, pady=10, font=("Arial", 20), command=lambda num=numero: self.controller.click_boton(num))
                oneButton1.pack(side='left')

            elif numero > '6' and numero <= '9':    
                oneButton1 = tk.Button(self.main_frame3, text=numero,width=5, padx=10, pady=10, font=("Arial", 20), command=lambda num=numero: self.controller.click_boton(num))
                oneButton1.pack(side='left')
            
            elif numero > '3' and numero < '7':   
                oneButton = tk.Button(self.main_frame4, text=numero,width=5, padx=10, pady=10, font=("Arial", 20),command=lambda num=numero: self.controller.click_boton(num))
                oneButton.pack(side='left')
            elif numero =='0':
                oneButton1 = tk.Button(self.main_frame6, text=numero,width=5, padx=10, pady=10, font=("Arial", 20),command=lambda num=numero: self.controller.click_boton(num))
                oneButton1.pack(side='left')
            
        for numero in self.simbols:
            if numero == '.':    
                oneButton1 = tk.Button(self.main_frame6, text=numero,width=5, padx=10, pady=10, font=("Arial", 20),command=lambda num=numero: self.controller.click_boton(num), bg='lightblue')
                oneButton1.pack(side='left')
            elif numero =='/':
                oneButton1 = tk.Button(self.main_frame4, text=numero,width=5, padx=10, pady=10, font=("Arial", 20),command=lambda num=numero: self.controller.click_boton(num), bg='lightblue')
                oneButton1.pack(side='left')
            elif numero =='-':
                oneButton1 = tk.Button(self.main_frame5, text=numero,width=5, padx=10, pady=10, font=("Arial", 20),command=lambda num=numero: self.controller.click_boton(num), bg='lightblue')
                oneButton1.pack(side='left')
            elif numero =='+':
                oneButton1 = tk.Button(self.main_frame3, text=numero,width=5, padx=10, pady=10, font=("Arial", 20),command=(lambda num=numero: self.controller.click_boton(num)), bg='lightblue')
                oneButton1.pack(side='left')
            elif numero =='=':
                oneButton1 = tk.Button(self.main_frame6, text=numero,width=11, padx=10, pady=10, font=("Arial", 20),command=lambda num=numero: self.controller.click_boton(num), bg='pink')
                oneButton1.pack(side='left')
            elif numero =='*' or numero =='%':
                oneButton1 = tk.Button(self.main_frame2, text=numero,width=5, padx=10, pady=10, font=("Arial", 20),command=lambda num=numero: self.controller.click_boton(num), bg='lightblue')
                oneButton1.pack(side='left')
            
            elif numero =='C':
                oneButton1 = tk.Button(self.main_frame2, text=numero,width=10, padx=10, pady=10, font=("Arial", 20),command=lambda num=numero: self.controller.click_boton(num), bg='orange')
                oneButton1.pack(side='left')
    

    def main(self):###función para lanzar la ventana y llamando a tk para que comienza a iniciar todo el codigo de arriba
        self.mainloop()


##tengo dos opciones una usar el pack pero no se acomodarán como me gusta o la otra es usar el grid
    #otra opcion es aplicar if y elif, en los if irían los nunmero sy en los elif los imbolos

class Model: ##clase modelo
    def __init__(self):
        self.previous_value =''##creamos variables a usar
        self.value=''
        self.operator=''
        
        
    def operaciones(self, numero):
        if numero == 'C':##borrador
            self.value = ''
            self.previous_value = ''
            self.operator = ''
        
        
        elif numero == '=':##devolver resultado
            value = self._evaluate()
            #if '.0' in str(value):
             #   value = int(value)
            self.value = str(value)
        
        elif numero >='0' and numero <='9':  #devolver números
            self.value += numero

    
        else: #función para los operadores
            if self.value:
                self.operator = numero
                self.previous_value = self.value
                self.value = ''
        
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
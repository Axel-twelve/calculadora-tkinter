
"""Calculadoras mediante el modelo MVC con las librerías Tkinter 
"""


import tkinter as tk ##libreria de tkinter para el lanzamiento de ventanas
from tkinter import ttk ##librería más moderna de tkinter temática

##creamos las 3 clases como el MVC


class View(tk.Tk): ##clase vista y heredamos tk
    
    def __init__(self, controller):
        super().__init__()
        self.controller=controller ##acceder a la clase controller
        self.title('Mi calculadora') ##titulo de la ventana


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
    

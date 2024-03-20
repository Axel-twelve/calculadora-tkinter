
"""Calculadoras mediante el modelo MVC con las librerías Tkinter 
"""


import tkinter as tk ##libreria de tkinter para el lanzamiento de ventanas
from tkinter import ttk ##librería más moderna de tkinter


##creamos las 3 clases como el MVC

lista=['hola', 'q show', 'what']

class View: ##clase vista 
    def __init__(self):
        pass

    def imprimir(self):
        for i in lista:
            print(i)
    
     
   

class Model: ##clase modelo
    def __init__(self):
        pass

class Controller:##clase controlador
    def __init__ (self, numero):
        self.numero=numero
        
    def main (self):
        print('este es el main')

    def intro (self):
        print(self.numero)




if __name__=='__main__': ## creamos la inicialización del modelo
    hola=input('que show')
    calculator=Controller(hola) ##probando el modelo
    vista=View()
    vista.imprimir()###llamamos a la funcion del modelo
    calculator.main()
    calculator.intro()
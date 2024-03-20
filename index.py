
"""Calculadoras mediante el modelo MVC con las librerías Tkinter 
"""


import tkinter as tk ##libreria de tkinter para el lanzamiento de ventanas
from tkinter import ttk ##librería más moderna de tkinter temática

##creamos las 3 clases como el MVC


class View(tk.Tk): ##clase vista y heredamos tk
    
    def __init__(self, controller):
        super().__init__()
        self.controller=controller ##acceder a la clase controller
    

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
     

    
    ###para guardarlo
    ## debes de correr primero el código 
    ### te vas a la llave y te aparecera uun numero
    ### le daras en el mas y arriba le picas en el cuadrito para guardar
    ### de ahi en los 3 puntitos
    ## le picas al cuadrito de arriba
        

#grabar unas historias del contenido que haces en hisoka
#redacto -- instagram



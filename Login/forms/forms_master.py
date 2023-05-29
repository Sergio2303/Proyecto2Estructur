import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl

class MasterPanel: 
    
    #acá se modificaran las propiedades del titulo al igual que, ancho y alto de la ventana. 
    def _init_(self): 
        self.ventana = tk.TK()
        self.ventana.title('Master panel')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg = '#fcfcfc')
        self.ventana.resizable(width=0, height=0)

        logo =utl.leer_imagen("./imagenes/logo.png", (200, 200))

        #colocar imagen en etiqueta de forma que ambas estnen centradas y de buen tamaño
        
        label = tk.Label( self.ventana, image=logo,bg='##ffffff' )
        label.place(x=0,y=0,relwidth=1, relheight=1)
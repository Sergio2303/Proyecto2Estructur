import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.forms_master import MasterPanel

class App:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Login')
        self.ventana.geometry('800x500') #tamaño del login 
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana,800,500)
        self.ventana.mainloop()

        logo =utl.leer_imagen("Login\imagenes\logo.jpg", (200, 200))
        
        #panel para el logo, acontinuacion se colocora el logo en una area en especifico. 
       




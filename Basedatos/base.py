#22808, Sergio Palacios
#
#librerias
#libreria para conectarse con la base de datos
from neo4j import GraphDatabase 
#libreria para ventana en python
from tkinter import *
from tkinter import messagebox



#Login:
class Programa(Tk):
    def __init__(self ) :
        Tk.__init__(self)
        #configuracion de ventana 
        self.geometry("750x400")
        self.config(bg="#bde0fe") 
        self.resizable(width=0, height=0)
        self.title("Login")
        #objetos de ventana
        Label(text="Iniciar sesión", fg="#457b9d", bg="#bde0fe", font=("Times New Roman",28)).place(x=270,y=40)
        self.l1=Label(text="Ingrese su usuario:")
        self.l1.place(x=300,y=120)
        self.l1.config(bg="#bde0fe")
        self.l2=Label(text="Ingrese su contraseña:")
        self.l2.place(x=300,y=170)
        self.l2.config(bg="#bde0fe")
        self.e1=Entry(width=20)
        self.e1.place(x=300,y=140)
        self.e2=Entry(width=20)
        self.e2.place(x=300,y=190)
        #boton
        btn1= Button(self, text="Iniciar Sesion", command=self.iniciarSesion, width=16, height=2)
        btn1.place(x=300,y=227)
        btn1.config(bg="#a2d2ff") 
        #termina la ventana
        self.mainloop()
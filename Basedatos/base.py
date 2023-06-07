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
    
    def iniciarSesion(self):
        #obtener el usuario y contraseña 
        self.usuario= (self.e1.get())
        self.contrasena= (self.e2.get())
        #conexion a la base de datos y tambien verificar usuarios
        self.uri = "" 
        self.user = "neo4j"
        self.password = "" 
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))
           # En esta parte se verifica la sesion, tambien que la base de datos este activa y que esta tenga los datos correctos
        with self.driver.session() as session:
            resultado = session.run("MATCH (u:User {name: $name, password: $password}) RETURN u", name=self.usuario, password=self.contrasena)
            registro = resultado.single()
            if registro:
                # se revisa que los usuarios y contraseñas sean correctas
                messagebox.showinfo("Iniciar sesión", "Inicio de sesión exitoso, bienvenido "+ self.usuario + "!")
            
                self.destroy()
                #se pasa a la nueva ventana
                ventana2= Menu(self.usuario, self.driver) 
                #acá se mandan como parametros el usuario y el driver de la conexion de la base de datos

            else:
                # aca se verifica si el usuario o contraseña son incorrectos
                messagebox.showerror("Iniciar sesión", "Usuario o contraseña incorrectos")

                
class Menu(Tk):
    #Se utilizan los dos parametros para mantener la sesion iniciada
    def _init_(self, usuario, driver):
        Tk._init_(self)
        #configuracion
        self.geometry("750x400")
        self.config(bg="#bde0fe")
        self.resizable(width=0, height=0)
        self.title("Menu Principal")
        #objetos de la ventana
        Label(text="Menu Principal", fg="#457b9d", bg="#bde0fe", font=("Times New Roman",28)).place(x=270,y=40)
        btn2= Button(self, text="Ver recomendaciones",width=20, command=self.recomendar)
        btn2.place(x=310,y=120)
        btn2.config(bg="#a2d2ff") 
        #instanciar el usuario como parametro
        self.usuario= usuario 
        #instanciar el driver como parametro 
        self.driver= driver 
        #fin 
        self.mainloop()

    def recomendar(self):
        #Consulta en base de datos y confirmar que siga abierta la sesion
        with self.driver.session() as session:
            #resultado de la consulta
           
            resultado = session.run('MATCH (u:User {name: "'+self.usuario+'"})-[:ESCUCHA]->(g:Genero)<-[:ESCUCHA]-(ou:User)-[:ESCUCHA]->(rg:Genero)<-[:TIENE_GENERO]-(c:Cancion) WHERE NOT (u)-[:ESCUCHA]->(rg) WITH DISTINCT c.nombreCancion AS cancion, COLLECT(DISTINCT rg.nombre) AS generos RETURN cancion, generos')
            #lista= [cancion, genero]
            resultado=list(resultado)
            print(resultado)
            
            #crear un listbox (objeto para mostrar la lista resultado)solo se instancia
            listbox= Listbox(self)
            listbox.place(x=220,y=160)
            listbox.config(width=60, background="#caf0f8")
            
            #recorrer con el for 
            for registro in resultado:
                cancion = registro["cancion"] 
                generos = ", ".join(registro["generos"]) #porque es una lista
                #enseña los resultados 
                listbox.insert(END, f" cancion: {cancion} - generos: - {generos}")

v= Programa() 
#regresa al inicio de sesion
        
        

    
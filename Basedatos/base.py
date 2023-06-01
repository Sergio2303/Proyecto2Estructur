from colorama import Fore, Back, Style
import tkinter as tk
from tkinter import messagebox
from neo4j import GraphDatabase

#Conexión a la base de datos Neo4j
driver = GraphDatabase.driver("neo4j+s://2b702678.databases.neo4j.io", auth=("neo4j", "WR5R6xVto1O91dI_Y9prNnro8rvMR6swaeFmZHMaNVY"))
# Crear una instancia de la ventana principal
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

#Obtencion de los grafos
def obtener_grafo_genero():
    with driver.session() as session:
        result = session.run(
            "MATCH (genero:Genero)<-[r]-(Canciones) "
            "RETURN genero, type(r), Canciones"
        )
        
        #Guardar los datos con un ciclo
        for record in result:
            genero_node = record["genero"]
            related_node = record["Canciones"]
            #Muestra de resultados
            print(Fore.WHITE +Back.BLACK +f"Género: {genero_node['Genero']}")
            print(Fore.BLUE +Back.BLACK +f"Nodo Relacionado: {related_node}\n")
           
       

#Ejemplo de uso
obtener_grafo_genero()
root.destroy()

#Cerrar la conexión al finalizar
driver.close()
#creamos el padre
class Animal():
    #creamos erl metodo contructor
    def __init__(self,nombre,edad,habitat,tamaño,color):
        self.nombre= nombre
        self.edad=edad
        self.habitat=habitat
        self.tamaño=tamaño
        self.color=color
        
        #crear un metodo
        def imprimir_dato (self):
            info =f"nombre:{self.nombre},edad:{self.edad},habitat:{self.habitad},tamaño{self.tamaño},color:{self.color}"
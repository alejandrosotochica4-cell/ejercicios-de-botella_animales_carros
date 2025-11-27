class vehiculo:
    def _init_(self,modelo,color,motor,numero_puertas,capacidad_pasajeros,tipo_conbustible):
        self.modelo=modelo
        self.color=color
        self.motor=motor
        self.numero_puertas=numero_puertas
        self.capacidad_pasajeros=capacidad_pasajeros
        self.tipo_conbustible=tipo_conbustible
    
    def arranque(self):
        print("el motor arranco")
    
    def apagado(self):
        print("el motor esta apagado")
    
    def aceleracion_frenado(self):
        print("el vehiculo acelera y frena bien")
    
    def sistema_direccion(self):
        print("sistema de direccion en buen estado")
    
    def climatizacion(self):
        print("climatizacion del vehiculo") 
    
    def tipo_de_seguridad(self):
        print("seguridad media")
    
    def imprimir(self):
        print(f"modelo: {self.modelo}")
        print(f"color:{self.color}")
        print(f"motor: {self.motor}")
        print(f"numero de puertas:{self.numero_puertas}")
        print(f"capacidad de pasajeros:{self.capacidad_pasajeros}")
        print(f"tipo de conbustible:{self.tipo_conbustible}")           
            
        
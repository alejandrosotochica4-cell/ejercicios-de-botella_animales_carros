from  clase_vehiculo import vehiculo
#....clase hija2

class clase_vehiculo2(vehiculo):
    
    def __init__(self,capacidad_pasajeros,tipo_conbustible,):
        super().__init__(capacidad_pasajeros,tipo_conbustible,)
        
    
    def sistemas_ventanas(self):
        print("se an vendido varios modelos de este tipo")
    
    def sistema_espejo(self):
        return super().sistema_espejo()
    


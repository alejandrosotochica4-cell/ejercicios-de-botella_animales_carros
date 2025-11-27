from  clase_vehiculo import vehiculo
#....clase hija

class clase_vehiculo1(vehiculo):
    
    def __init__(self, modelo,color,motor,numero_puertas,):
        super().__init__(modelo,color,motor,numero_puertas)
        
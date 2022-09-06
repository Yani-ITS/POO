class Automovil:
    def __init__(self, marca, modelo, color, año, patente, chasis, motor, observaciones):
        self.marca= marca
        self.modelo= modelo
        self.color= color
        self.año= año
        self.patente= patente
        self.chasis= chasis
        self.motor= motor
        self.observaciones= observaciones
        
        @property
        def marca (self):
            return self.marca
        
        @property
        def modelo(self):
            return self.modelo
        
        @property
        def color(self):
            return self.color
        
        @property
        def patente(self):
            return self.patente
        
        @property
        def año(self):
            return self.año
        
        @property
        def chasis(self):
            return self.chasis
        
        @property
        def motor(self):
            return self.motor
        
        @property
        def observaciones(self):
            return self.observaciones 
        
        @observaciones.setter
        def observaciones(self, unaObservacion):
            self.observaciones= unaObservacion
            
        @motor.setter
        def motor (self, unMotor):
            self.motor= unMotor
            
        @chasis.setter
        def chasis(self, unChasis):
            self.chasis= unChasis
            
        @año.setter
        def año(self, unAño):
            self.año= unAño
            
        @patente.setter
        def patente(self, unPatente):
            self.patente= unPatente
        
        @color.setter
        def color(self, unColor):
            self.color= unColor    
            
        @modelo.setter
        def modelo(self, unModelo):
            self.modelo= unModelo
            
        @marca.setter
        def marca(self, unaMarca):
            self.marca= unaMarca
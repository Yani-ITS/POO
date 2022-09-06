class Agencia:
    def __init__(self, nombre, direccion, telefono, localidad):
        self.nombre= nombre
        self.direccion= direccion
        self.telefono= telefono
        self.localidad= localidad
        
        @property
        def nombre(self):
            return self.nombre 
        
        @property
        def direccion(self):
            return self.direccion
        
        @property
        def telefono(self):
            return self.telefono
        
        @property
        def localidad(self):
            return self.localidad
        
        @localidad.setter
        def localidad (self, unaLocalidad):
            self.localidad= unaLocalidad
            
        @telefono.setter
        def telefono(self, unTelefono):
            self.telefono= unTelefono
            
        @direccion.setter
        def direccion(self, unaDireccion):
            self.direccion= unaDireccion
            
        @nombre.setter
        def nombre(self, unNombre):
            self.nombre= unNombre
            
            
        
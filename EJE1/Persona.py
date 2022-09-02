class Persona:
    def __init__(self,nombre , apellido, dni, telefono, email, f_nac, direccion):
        self.nombre= nombre
        self.apellido= apellido
        self.dni= dni
        self.telefono= telefono
        self.email= email
        self.f_nac= f_nac
        self.direccion= direccion
        
        @property
        def nombre (self):
            return self.nombre
        
        @property
        def apellido(self):
            return self.apellido
        
        @property
        def dni(self):
            return self.dni
        
        @property
        def telefono(self):
            return self.telefono
        
        @telefono.setter
        def 
        
        @dni.setter
        def dni(self, unDni):
            self.dni= unDni    
            
        @apellido.setter
        def apellido(self, unApellido):
            self.apellido= unApellido
            
        @nombre.setter
        def nombre(self, unNombre):
            self.nombre= unNombre
            
        
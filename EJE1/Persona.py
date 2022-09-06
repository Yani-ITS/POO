from datetime import date


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
        
        @property
        def email(self):
            return self.email
        
        @property
        def f_nac(self):
            return self.f_nac
        
        @property
        def direccion(self):
            return self.direccion
        
        @direccion.setter
        def direccion (self, unaDireccion):
            self.direccion= unaDireccion
            
        @f_nac.setter
        def f_nac(self, unaFecha):
            self.f_nac= unaFecha
            
        @email.setter
        def email(self, unEmail):
            self.email= unEmail
            
        @telefono.setter
        def telefono(self, unTelefono):
            self.telefono= unTelefono
        
        @dni.setter
        def dni(self, unDni):
            self.dni= unDni    
            
        @apellido.setter
        def apellido(self, unApellido):
            self.apellido= unApellido
            
        @nombre.setter
        def nombre(self, unNombre):
            self.nombre= unNombre
            
        def edad():
            edad= date - self.f_nac
            return edad
        
            
        
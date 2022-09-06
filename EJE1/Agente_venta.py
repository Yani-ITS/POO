from EJE1.Persona import Persona


class AgenteVenta (Persona):
    def __init__(self, nombre, apellido, dni, telefono, email, f_nac, direccion, legajo):
        super().__init__(nombre, apellido, dni, telefono, email, f_nac, direccion)
        self.legajo= legajo
        
    @property
    def legajo(self):
        return self.legajo
    
    @legajo.setter
    def legajo(self, unLegajo):
        self.legajo= unLegajo
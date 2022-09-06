from EJE1.Agencia import Agencia


class Sucursal(Agencia):
    def __init__(self, nombre, direccion, telefono, localidad, nro_sucursal):
        super().__init__(nombre, direccion, telefono, localidad)
        self.nro_sucursal= nro_sucursal
        
    @property
    def nro_sucursal(self):
        return self.nro_sucursal
    
    @nro_sucursal.setter
    def nro_sucursal(self, unaSucursal):
        self.nro_sucursal= unaSucursal
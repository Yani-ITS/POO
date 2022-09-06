from EJE1.Automovil import Automovil
from EJE1.Cliente import Cliente


class Poliza(Cliente, Automovil):
    def __init__(self, nombre, apellido, dni, telefono, email, f_nac, direccion, nro_cliente, marca, modelo, color, año, patente, chasis, motor, observaciones, NroPoliza):
        super(Cliente).__init__(nombre, apellido, dni, telefono, email, f_nac, direccion, nro_cliente)
        super(Automovil).__init__(marca, modelo, color, año, patente, chasis, motor, observaciones)
        self.NroPoliza= NroPoliza
        
        @property
        def NroPoliza(self):
            return self.NroPoliza
        
        @NroPoliza.setter
        def NroPoliza(self, unaPoliza):
            self.NroPoliza= unaPoliza
    
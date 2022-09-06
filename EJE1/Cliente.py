from EJE1.Persona import Persona


class Cliente(Persona):
    def __init__(self, nombre , apellido, dni, telefono, email, f_nac, direccion, nro_cliente):
        super.__init__(nombre , apellido, dni, telefono, email, f_nac, direccion)
        self.nro_cliente= nro_cliente
        
        @property
        def nro_cliente(self):
            return self.nro_cliente
        
        @nro_cliente.setter
        def nro_cliente(self, unNumero):
            self.nro_cliente= unNumero
            

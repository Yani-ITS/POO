class Venta:
    def __init__(self, fecha_venta, valor, id_venta):
        self.fecha_venta= fecha_venta
        self.valor= valor
        self.id_venta= id_venta
        
        @property
        def fecha_venta(self):
            return self.fecha_venta
        
        @property
        def valor(self):
            return self.valor 
        
        @property
        def id_venta(self):
            return self.id_venta
        
        @id_venta.setter
        def id_venta(self, idVenta):
            self.id_venta= idVenta
            
        @valor.setter
        def valor (self, unValor):
            self.valor= unValor
            
        @fecha_venta.setter
        def fecha_venta(self, diaVenta):
            self.fecha_venta= diaVenta
            
        def registroVenta(): 
            
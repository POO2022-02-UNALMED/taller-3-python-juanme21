class TV:
    _numTV = 0

    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado

        self.canal = 1
        self.precio = 500
        self.volumen = 1
        self.control = ...
        TV._numTV += 1
    
    def getMarca(self):
        return self.marca
    
    def setMarca(self, marca):
        self.marca=marca

    def getPrecio(self):
        return self.precio
    
    def setPrecio(self, precio):
        self.precio=precio
    
    def getControl(self):
        return self.control
    
    def setControl(self, control):
        self.control=control
    
    def getVolumen(self):
        return self.volumen
    
    def setVolumen(self, volumen):
        self.volumen=volumen
    
    def getCanal(self):
        return self.canal
    
    def setCanal(self, canal):
        self.canal=canal

    @classmethod
    def getNumTV(cls):
        return cls._numTV

    @classmethod
    def setNumTV(cls, numtv):
        cls._numTV = numtv

    def turnOn(self):
        self.estado = True
    
    def turnOff(self):
        self.estado = False
    
    def getEstado(self):
        return self.estado

    def canalUp(self):
        if (1 <= self.canal < 120) and self.estado:
            self.canal += 1
            
    def canalDown(self):
        if (1 < self.canal <= 120) and self.estado:
            self.canal -= 1
    
    def volumenUp(self):
        if (0 <= self.volumen < 7) and self.estado:
            self.volumen += 1
            
    def volumenDown(self):
        if (0 < self.volumen <= 7) and self.estado:
            self.volumen -= 1
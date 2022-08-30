from televisores.TV import TV


class Control:
    def __init__(self):
        pass

    def enlazar(self, tv):
        self.tv = tv
        tv.setControl(self)

    def setTv(self, tv):
        self.tv = tv
    
    def getTv(self):
        return self.tv

    def turnOn(self):
        self.tv.estado = True
    
    def turnOff(self):
        self.tv.estado = False
    
    def canalUp(self):
        self.tv.canalUp()
            
    def canalDown(self):
        self.tv.canalDown()

    def setCanal(self, canal):
        self.tv.canal=canal

    def volumenUp(self):
        self.tv.volumenUp()

    def volumenDown(self):
        self.tv.volumenDown()
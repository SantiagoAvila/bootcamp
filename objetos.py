class condicion_estandar:
    temperaturastandar= 20 
    presionstandar= 1
    def __init__(self,temperatura,presion):
        self.temperatura=temperatura
        self.presion=presion
        print("la temperatura actual es de",self.temperatura,"grados centigrados")
        print("la presion actual es de ",self.presion,"atm, siendo la estandar")
    def set_temperatura(self,cantidad):
        self.temperatura = cantidad
    def set_presion(self,cantidad):
        self.presion=cantidad

condicion_estandar(22,1)

meteorologia_estandar=condicion_estandar(22,1.01)

meteorologia_actual=condicion_estandar(25,1.03)

condicion_estandar(27,1.01)



class Trex()


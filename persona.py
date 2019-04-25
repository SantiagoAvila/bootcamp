class personas:
    def __init__(self,nombre,edad):
        self.Nombre=nombre
        self.edad=edad
        print("Mi nombre es",self.Nombre,"y tengo",self.edad,"años")
    def set_Nombre(self,cantidad):
        self.Nombre = cantidad
    def set_edad(self,cantidad):
        self.edad=cantidad

    def cumple_años(self):
        i=1
        a=2019
        while i<11:
            self.edad=self.edad+1
            print(self.edad,"años en",a)
            i=i+1
            a=a+1
    def calcular_años(self,en_cuantos_años,año_actual):
        self.año_actual=año_actual
        self.en_cuantos=en_cuantos_años
        z=self.edad+self.en_cuantos
        b=self.año_actual+self.en_cuantos
        print("en el año",b,"tendra ",z,"años")

pepito = personas("Santiago",25)

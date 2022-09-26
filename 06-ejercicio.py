class Vehiculo:
    # color=None
    # ruedas=None
    # puertas=None
    #constructor
    def __init__(self,c,ruedas,puertas):
        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas

class Coche(Vehiculo):
    # velocidad=None
    # cilindrada=None
    def __init__(self,color,ruedas,puertas,velocidad,cilindrada):
        self.color=color
        self.ruedas=ruedas
        self.puertas =puertas
        self.velocidad=velocidad
        self.cilindrada=cilindrada
        print("Soy de color",self.color,"con ",self.ruedas," ruedas","y ",self.puertas,"Puertas",
        "y mi velocidad es de ",self.velocidad,"km/h","con cilindrage ",self.cilindrada)
    

carro=Coche("rojo",4,2,320,2.5)



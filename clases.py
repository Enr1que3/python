class Dino:
    #propiedad
    encendido=True

    #metodos(Funcones)
    #usar self es como usar this el  cual hace referencia a 
    #las varibles privadas(propiedades)
    def  apaga():
        self.encendido=False

#instanciar una clase significa crear un objeto

#crear objeto
d=Dino()
d.enceiende=False #se puede sobreescrir en cualquier momentos
print(d.enceiende)



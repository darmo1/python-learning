class MiPerro:
    patas= 4
    #self se agrega para crear la referencia de la instancia de la clase
    def __init__(self, nombre):
        self.nombre = nombre
        print(nombre)
    
    @classmethod
    def hablar(cls):
        print('Guau', f'{self.nombre} dice : Guau')

    @classmethod
    def factory(cls, name):
        return cls(name)



mi_perro = MiPerro('Dog Name')

mi_perro.hablar()

##FACTORY METHOD : ES CREAR INSTANCIAS PARA UNA DETERMINADA CLASE
perro_3 = MiPerro.factory()


#Propiedades y metodos privados

class miCat:
    def __init__(self, name, age):
        self.__name = name  #__name es una propiedad privada
        self.age = age

    @property
    def nombre(self):
        return self.__name
    
    @nombre.setter
    def nombre(self, nombre):
        if nombre.strip():
            self.__nombre = nombre
        return  

    def hablar(self):
        print(f'{self.__name} tiene {self.age}')

    @classmethod
    def factory(cls):
        return cls() 
class Coche:
    marca = ''
    color = 'Blanco'
    velocidad = 0
    __encendido = False

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def encender(self):
        self.encendido = True

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def getEncendido(self):
        return self.__encendido

class CocheDeportivo(Coche):
    cv = 60

    def __init__(self, marca, color, cv):
        self.marca = marca
        self.color = color
        self.cv = cv
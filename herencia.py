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

coche_lujo = CocheDeportivo('BMW', 'rojo', 100)
print(f'Marca: { coche_lujo.marca }, y es de color { coche_lujo.color }, con { coche_lujo.cv } caballos de fuerza')
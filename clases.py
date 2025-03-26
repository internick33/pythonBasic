class Coche:
    marca = ''
    color = 'Blanco'
    __encendido = False
    velocidad = 0

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def encender(self):
        self.encendido = True

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def getEncendido(self):
        return self.__encendido

coche2 = Coche('BMW', 'rojo')
coche2.encender()
coche2.velocidad = 500

print(f'Coche lujo: {coche2.marca} y es de color: {coche2.color}')

if coche2.getEncendido():
    print(f'El coche lujo esta encendido y va a una velocidad de: {coche2.velocidad} km/h')
else:
    print('El coche1 esta apagado')


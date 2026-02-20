class Pista:

    def __init__(self, km):
        self.km = km

class Ciclista:

    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

class Itinerario:

    def __init__(self, ubicacion,fecha):
        self.ubicacion=ubicacion
        self.fecha=fecha

if __name__ == '__main__':
    print()
from abc import ABC, abstractmethod


class Modalidad(ABC):
    def __init__(self, nombre, requiere_vehiculo):
        self.nombre = nombre
        self.requiere_vehiculo = requiere_vehiculo

    def get_info_basica(self):
        vehiculo_txt = "Sí" if self.requiere_vehiculo else "No"
        return f"Modalidad: {self.nombre} | Requiere vehículo: {vehiculo_txt}"

    @abstractmethod
    def calcular_tiempo(self, distancia_km):
        pass

    @abstractmethod
    def equipamiento(self):
        pass


class Ciclismo(Modalidad):
    def __init__(self):
        super().__init__(nombre="Ciclismo", requiere_vehiculo=True)
        self.velocidad_media = 20

    def calcular_tiempo(self, distancia_km):
        tiempo = distancia_km / self.velocidad_media
        return f"{tiempo:.1f} horas pedaleando"


class Senderismo(Modalidad):
    def __init__(self):
        super().__init__(nombre="Senderismo", requiere_vehiculo=False)
        self.velocidad_media = 5

    def calcular_tiempo(self, distancia_km):
        tiempo = distancia_km / self.velocidad_media
        return f"{tiempo:.1f} horas caminando"


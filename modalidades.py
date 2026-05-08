from abc import ABC, abstractmethod
from typing import Self

class Modalidad(ABC):
    def __init__(self, nombre: str, requiere_vehiculo: bool):
        self.nombre = nombre
        self.requiere_vehiculo = requiere_vehiculo

    def get_info_basica(self):
        vehiculo_txt = "Sí" if self.requiere_vehiculo else "No"
        return f"Modalidad: {self.nombre} | Requiere vehículo: {vehiculo_txt}"

    @abstractmethod
    def calcular_tiempo(self, distancia_km: float) -> str:
        pass

    @abstractmethod
    def equipamiento(self):
        pass


class Ciclismo(Modalidad):
    def __init__(self):
        super().__init__(nombre="Ciclismo", requiere_vehiculo=True)
        self.velocidad_media = 20

    def calcular_tiempo(self, distancia_km: float) -> str:
        if distancia_km <= 0:
            raise ValueError(f"La distancia debe ser mayor a 0. Valor recibido: {distancia_km} km.")
        tiempo = distancia_km / self.velocidad_media
        return f"{tiempo:.1f} horas pedaleando"

    def equipamiento(self) -> list[str]:
        return [
            "Casco homologado",
            "Bidón de agua",
            "Ropa reflectante",
        ]

class Senderismo(Modalidad):
    def __init__(self):
        super().__init__(nombre="Senderismo", requiere_vehiculo=False)
        self.velocidad_media = 5

    def calcular_tiempo(self, distancia_km: float) -> str:
        if distancia_km <= 0:
            raise ValueError(f"La distancia debe ser mayor a 0. Valor recibido: {distancia_km} km.")
        tiempo = distancia_km / self.velocidad_media
        return f"{tiempo:.1f} horas caminando"

    def equipamiento(self) -> list[str]:
        return [
            "Botas de montaña",
            "Mochila",
            "Bastones de trekking",
            "Mapa o GPS",
            "Agua y comida"
        ]


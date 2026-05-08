from abc import ABC

NivelEntrada = int | str | None
Nivel = int | None

class Persona(ABC):
    nombre: str
    _edad: int
    _dni: str
    def __init__(self, nombre: str, edad: int, dni: str):
        self.nombre = nombre
        self._edad = edad
        self._dni = dni

    def __str__(self) -> str:
        return f'Perfil de {self.nombre}: \n Edad: {self._edad}\n Dni: {self._dni}'








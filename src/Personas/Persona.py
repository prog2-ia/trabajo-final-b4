from abc import ABC
from src.Exceptions.customexceptions import DNIInvalidoException

NivelEntrada = int | str | None
Nivel = int | None

class Persona(ABC):
    def __init__(self, nombre: str, edad: int, dni: str):
        if not dni or len(dni)!= 9:
            raise DNIInvalidoException(f'El DNi {dni} no es válido. Debe tener 9 caracteres')
        self.nombre = nombre
        self._edad = edad
        self._dni = dni

    def __str__(self) -> str:
        return f'Perfil de {self.nombre}: \n Edad: {self._edad}\n Dni: {self._dni}'

    @property
    def edad(self) -> int:
        return self._edad

    @property
    def dni(self) -> str:
        return self._dni








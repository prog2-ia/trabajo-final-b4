from Persona import Persona, NivelEntrada
from Usuario import Usuario

class Staff(Persona):
    _rol: str
    def __init__(self, nombre: str, edad: int, dni: str, rol: str):
        super().__init__(nombre, edad, dni)
        self._rol = rol

    def __str__(self) -> str:
        str_per = super().__str__()
        return str_per + f'\n Rol: {self._rol}'

    def __repr__(self) -> str:
        return f'Staff(nombre={self.nombre}, edad={self.edad}, dni={self.dni}, rol={self._rol})'

    def cambiar_nivel_ciclismo(self, usuario: Usuario, nivel: NivelEntrada) -> str:
        usuario.poner_nivel_ciclismo(nivel)
        return f'{self.nombre} ha cambiado el nivel de ciclismo de {usuario.nombre}'

    def cambiar_nivel_senderismo(self, usuario: Usuario, nivel: NivelEntrada) -> str:
        usuario.poner_nivel_senderismo(nivel)
        return f'{self.nombre} ha cambiado el nivel de senderismo de {usuario.nombre}'


from abc import ABC, abstractmethod
from Persona import Usuario, Staff
import random

Nivel = int | None

#Pista abstracta: La dificultad funciona: (0=Sencilla, 1=Media, 2=Difícil)
class Pista(ABC):

    _nombre: str
    _dificultad: int
    _longitud: float
    _participantes: list
    _max_personas: int
    _terreno: str
    _puntos_interes: list[str]
    _clima: str
    _abierta: bool
    _staff: str | None


    def __init__(self, nombre: str, dificultad: int, longitud: float, max_personas: int, terreno: str, puntos_interes: list[str] | None = None) -> None:
        self._nombre = nombre
        self._dificultad = dificultad
        self._longitud = longitud
        self._participantes = []
        self._max_personas = max_personas
        self._terreno = terreno
        if puntos_interes is None:
            self._puntos_interes = []
        else:
            self._puntos_interes = puntos_interes

        # El clima se asigna aleatoriamente al crear la pista
        self._clima = random.choice(['Soleado', 'Nublado', 'Lluvia'])
        self._abierta = True
        self._staff = None

    @abstractmethod
    # Cada tipo de pista valida el usuario según su actividad, por eso es abstracta
    def participa(self, usuario: Usuario):
        pass

    def hay_plazas(self) -> bool:
        return len(self._participantes) < self._max_personas

    def ya_inscrito(self, usuario: Usuario) -> bool:
        if usuario in self._participantes:
            return True
        else:
            return False

    def cancelar(self, usuario: Usuario) -> str:
        if usuario in self._participantes:
            self._participantes.remove(usuario)
            return f'❌ El usuario {usuario.nombre} ha cancelado su inscripción ❌'
        return f'⚠️ El usuario {usuario.nombre} no estaba inscrito ⚠️'

    def lista_participantes(self) -> list[str] | str:
        if not self._participantes:
            return f'No hay participantes en la pista {self._nombre}'
        part = []
        for i in self._participantes:
            part.append(i.nombre)
        return part

    def plazas(self) -> int:
        return self._max_personas - len(self._participantes)

    def cambiar_clima(self) -> str:
        self._clima = random.choice(['Soleado', 'Nublado', 'Lluvia'])
        return f'Nuevo clima de la pista {self._nombre}: {self._clima}'

    def asignar_staff(self, staff: Staff) -> str:
        self._staff = staff.nombre
        return f'El staff {staff.nombre} se ha asignado asignado a la pista {self._nombre}'

    def cerrar_pista(self) -> str:
        self._abierta = False
        return 'La pista está cerrada'

    def abrir_pista(self) -> str:
        self._abierta = True
        return 'La pista está abierta'

    def __add__(self, punto_interes: str) -> 'Pista':

        if punto_interes not in self._puntos_interes:
            self._puntos_interes.append(punto_interes)

        return self

    def __len__(self) -> int:
        return len(self._participantes)

#Añadir y quitar usuarios con += y -=:
    def __iadd__(self, usuario: Usuario) -> 'Pista':

        self.participa(usuario)

        return self

    def __isub__(self, usuario: Usuario) -> 'Pista':

        self.cancelar(usuario)

        return self

    def __str__(self) ->  str:
        if self._dificultad == 2:
            dif = 'Difícil'
        elif self._dificultad:
            dif = 'Media'
        else:
            dif = 'Sencilla'
        if self._abierta:
            estado = 'Abierta'
        else:
            estado = 'Cerrada'
        if self._staff is None:
            hay_staff = 'No hay ningún staff asignado'
        else:
            hay_staff = self._staff
        return (f'Pista: {self._nombre}\n Dificultad: {dif}\n Longitud: {self._longitud} km\n Máximo de personas: {self._max_personas}\n'
                f' Terreno: {self._terreno}\n Puntos de interés: {self._puntos_interes}\n Clima: {self._clima}\n'
                f' Estado: {estado}\n Plazas disponibles: {self._max_personas - len(self._participantes)} \n Staff: {hay_staff}')

    def __repr__(self) -> str:
        return (f'Pista(nombre={self._nombre}, dificultad={self._dificultad}, longitud={self._longitud}, max_personas={self._max_personas}, '
                f'terreno={self._terreno}), puntos_interes={self._puntos_interes}, clima={self._clima}, abierta = {self._abierta}, staff= {self._staff}')



class PistaCiclismo(Pista):
    def participa(self, usuario: Usuario) -> str:
        if not self._abierta:
            return f'❌ La pista {self._nombre} está cerrada ❌'

        elif not self.hay_plazas():
            return f'❌ No hay plazas disponibles en la pista {self._nombre} ❌'

        elif self.ya_inscrito(usuario):
            return f'⚠️ El usuario {usuario.nombre} ya está inscrito ⚠️'

        elif usuario.nivel_ciclismo is None:
            return f'❌ El usuario {usuario.nombre} no es ciclista ❌'

        elif usuario.nivel_ciclismo < self._dificultad:
            return f'❌ El usuario {usuario.nombre} no tiene el nivel suficiente para inscribirse en la pista ❌'

        else:
            self._participantes.append(usuario)
            return f'El usuario {usuario.nombre} ha sido inscrito correctamente en la pista {self._nombre} 🚴‍'



class PistaSenderismo(Pista):
    def participa(self, usuario: Usuario) -> str:
        if not self._abierta:
            return f'❌ La pista {self._nombre} está cerrada ❌'

        elif not self.hay_plazas():
            return f'❌ No hay plazas disponibles en la pista {self._nombre} ❌'

        elif self.ya_inscrito(usuario):
            return f'⚠️ El usuario {usuario.nombre} ya está inscrito ⚠️'

        elif usuario.nivel_senderismo is None:
            return f'❌ El usuario {usuario.nombre} no es senderista ❌'

        elif usuario.nivel_senderismo < self._dificultad:
            return f'❌ El usuario {usuario.nombre} no tiene el nivel suficiente para inscribirse en la pista ❌'

        else:
            self._participantes.append(usuario)
            return f'El usuario {usuario.nombre} ha sido inscrito correctamente en la pista {self._nombre} 🚶‍♂️‍'



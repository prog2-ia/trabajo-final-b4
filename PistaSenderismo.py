from Usuario import Usuario
from Pista import Pista
from customexceptions import PistaCerradaException, SinPlazasException, YaInscritoException, ActividadNoCompatibleException, NivelInsuficienteException


class PistaSenderismo(Pista):
    def participa(self, usuario: Usuario) -> str:
        if not self._abierta:
            raise PistaCerradaException(f'La pista {self._nombre} está cerrada.')

        if not self.hay_plazas():
            raise SinPlazasException(f'No hay plazas disponibles en la pista {self._nombre}')

        if self.ya_inscrito(usuario):
            raise YaInscritoException(f'El usuario {usuario.nombre} ya está inscrito.')

        if usuario.nivel_senderismo is None:
            raise ActividadNoCompatibleException(f'El usuario {usuario.nombre} no es senderista.')

        if usuario.nivel_senderismo < self._dificultad:
            raise NivelInsuficienteException(f'El usuario {usuario.nombre} no tiene el nivel suficiente para inscribirse en la pista.')

        else:
            self._participantes.append(usuario)
            return f'El usuario {usuario.nombre} ha sido inscrito correctamente en la pista {self._nombre} 🚶‍♂️‍'

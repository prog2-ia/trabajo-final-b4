from Persona import Usuario
from Pista import Pista


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

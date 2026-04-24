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


# El nivel funciona : (0=Principiante, 1=Aficionado, 2=Experto)
class Usuario(Persona):
    nivel_ciclismo: Nivel
    nivel_senderismo: Nivel
    def __init__(self, nombre: str, edad: int, dni: str, nivel_ciclismo: NivelEntrada = None, nivel_senderismo: NivelEntrada = None):
        super().__init__(nombre, edad, dni)
        self.nivel_ciclismo = self._validar_nivel(nivel_ciclismo)
        self.nivel_senderismo = self._validar_nivel(nivel_senderismo)

    def _validar_nivel(self, nivel: NivelEntrada) -> Nivel:
        # Convierte niveles en texto a 0,1 o 2 y valida que el nivel sea correcto
        if isinstance(nivel, str):
            nivel=nivel.lower()
            if nivel in ('principiante', 'aficionado', 'experto'):
                if nivel == 'principiante':
                    nivel = 0
                elif nivel == 'aficionado':
                    nivel = 1
                else:
                    nivel = 2
        if nivel not in (None, 0, 1, 2):
            print('⚠️ Nivel inválido. Se asignará "None" ⚠️')
            return None
        else:
            return nivel

    def __str__(self) -> str:
        if self.nivel_ciclismo is None:
            if self.nivel_senderismo is None:
                no_niv = 'No está registrado con ningún nivel'
            else:
                no_niv = ''

            niv_cic = ''
        else:
            no_niv = ''

            if self.nivel_ciclismo == 0:
                n = 'Principiante'
            elif self.nivel_ciclismo == 1:
                n = 'Aficionado'
            else:
                n = 'Experto'
            niv_cic = f'\n      Nivel de ciclista: {n}'

        if self.nivel_senderismo is None:
            niv_sen = ''
        else:
            if self.nivel_senderismo == 0:
                n = 'Principiante'
            elif self.nivel_senderismo == 1:
                n = 'Aficionado'
            else:
                n = 'Experto'
            niv_sen = f'\n      Nivel de senderista: {n}'
        str_per = super().__str__()
        return str_per + f' \n Nivel: {niv_cic}{niv_sen}{no_niv}'

    def __repr__(self) -> str:
        return f'Usuario(nombre={self.nombre}, edad={self._edad}, dni={self._dni} nivel_ciclismo={self.nivel_ciclismo}, nivel_senderismo={self.nivel_senderismo})'

    def poner_nivel_ciclismo(self, nivel: NivelEntrada) -> str:
        self.nivel_ciclismo = self._validar_nivel(nivel)

        return f'El nivel de ciclismo de {self.nombre} es {self.nivel_ciclismo}'

    def poner_nivel_senderismo(self, nivel: NivelEntrada) -> str:
        self.nivel_senderismo = self._validar_nivel(nivel)

        return f'El nivel de senderismo de {self.nombre} es {self.nivel_senderismo}'



class Staff(Persona):
    _rol: str
    def __init__(self, nombre: str, edad: int, dni: str, rol: str):
        super().__init__(nombre, edad, dni)
        self._rol = rol

    def __str__(self) -> str:
        str_per = super().__str__()
        return str_per + f'\n Rol: {self._rol}'

    def __repr__(self) -> str:
        return f'Staff(nombre={self.nombre}, edad={self._edad}, dni={self._dni}, rol={self._rol})'

    def cambiar_nivel_ciclismo(self, usuario: Usuario, nivel: NivelEntrada) -> str:
        usuario.poner_nivel_ciclismo(nivel)
        return f'{self.nombre} ha cambiado el nivel de ciclismo de {usuario.nombre}'

    def cambiar_nivel_senderismo(self, usuario: Usuario, nivel: NivelEntrada) -> str:
        usuario.poner_nivel_senderismo(nivel)
        return f'{self.nombre} ha cambiado el nivel de senderismo de {usuario.nombre}'




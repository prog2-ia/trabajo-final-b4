#EXCEPCIONES DE VEHÍCULO:
class VehiculoException(Exception):
    pass

class VehiculoAveriadoException(VehiculoException):
    pass

class VehiculoOcupadoException(VehiculoException):
    pass

class CapacidadExcedidaException(VehiculoException):
    pass

class VehiculoYaLibreException(VehiculoException):
    pass

#EXCEPCIONES DE MODALIDAD:
class ModalidadException(Exception):
    pass

class EquipamientoIncompletoException(ModalidadException):
    pass

class VehiculoIncompatibleException(ModalidadException):
    pass

class VehiculoFaltaException(ModalidadException):
    pass

#EXCEPCIONES DE USUARIO:
class UsuarioException(Exception):
    pass

class NivelInvalidoException(UsuarioException):
    pass

class DNIInvalidoException(UsuarioException):
    pass

#EXCEPCIONES DE PISTA:
class PistaException(Exception):
    pass

class PistaCerradaException(PistaException):
    pass

class SinPlazasException(PistaException):
    pass

class YaInscritoException(PistaException):
    pass

class NivelInsuficienteException(PistaException):
    pass

class ActividadNoCompatibleException(PistaException):
    pass

class NoInscritoException(PistaException):
    pass
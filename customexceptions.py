#EXCEPCIONES DE VEHICULO
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

class ModalidadException(Exception):
    pass

class EquipamientoIncompletoException(ModalidadException):
    pass

class VehiculoIncompatibleException(ModalidadException):
    pass

class VehiculoFaltaException(ModalidadException):
    pass


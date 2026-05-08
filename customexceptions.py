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


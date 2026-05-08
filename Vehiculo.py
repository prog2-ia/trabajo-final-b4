from abc import ABC, abstractmethod


class Vehiculo(ABC):
    def __init__(self, nombre: str, matricula: int, marca: str, modelo: str, anyo: int, estadooptimo=True):
        self.nombre = nombre
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.anyo = anyo
        self.estadooptimo = estadooptimo
        self.reparacion = False
        self.disponible = True
        self.historial_reparaciones = []

    def __str__(self):
        return f'Vehiculo de {self.nombre}: \n matrícula: {self.matricula} \n marca: {self.marca} \n modelo: {self.modelo} \n anyo: {self.anyo}'

    @abstractmethod
    def mantenimiento(self, fecha: str, detalles: str) -> bool:
        pass

    def reporteaveria(self):
        self.reparacion = True
        return f"El vehículo {self.matricula} ha reportado una avería."

    def iniciar_uso(self, usuario) ->bool:
        if self.estadooptimo == False:
            print(f"❌ Error: El vehículo {self.matricula} no se puede usar. No está en estado óptimo")
            return False

        if not self.disponible:
            print(f"❌ Error: El vehículo {self.matricula} ya está siendo utilizado por otra persona.")
            return False

        self.disponible = False
        print(f"✅ La persona '{self.nombre}' ha empezado a usar el vehículo {self.matricula}.")
        return True

    def finalizar_uso(self):
        if not self.disponible:
            self.disponible = True
            print(f"🔄 El vehículo {self.matricula} ha sido devuelto y vuelve a estar disponible.")
        else:
            print(f"⚠️ El vehículo {self.matricula} ya estaba libre.")


class Bici(Vehiculo):
    def __init__(self, nombre: str, matricula: int, marca: str, modelo: str, anyo: int, tipo_bici: str, marchas: int, estadooptimo=True):
        super().__init__(nombre, matricula, marca, modelo, anyo, estadooptimo)
        self.tipo_bici = tipo_bici
        self.marchas = marchas
        self.estado_cadena = "Óptimo"
        self.presion_ruedas = "Óptima"
        self.pastillas_freno = "Nuevas"

        if tipo_bici == 'carretera':
            self.velocidad_media_estimada = 20
        else:
            self.velocidad_media_estimada = 10

    def mantenimiento(self, fecha: str, detalles: str) -> bool:
        print(
            f'Estado actual de la bici: \n cadenas:{self.estado_cadena} \n pastillas:{self.pastillas_freno} \n presion de ruedas:{self.presion_ruedas}')

        if self.estado_cadena != 'Óptimo':
            self.estado_cadena = 'Óptimo'
        if self.presion_ruedas != 'Óptima':
            self.presion_ruedas = 'Óptima'
        if self.pastillas_freno != 'Nuevas':
            self.pastillas_freno = 'Nuevas'

        registro = f"{fecha} Mantenimiento realizado de la bici {self.matricula}: {detalles}"
        self.historial_reparaciones.append(registro)
        print(f"Registro guardado para {self.matricula}: {detalles}")
        self.estadooptimo = True

        return True

    def __str__(self):
        generica = super().__str__()
        return f"{generica} | Tipo: {self.tipo_bici}, {self.marchas} marchas."

    def pedalear(self):
        print(
            f"El ciclista está pedaleando en la {self.marca} {self.modelo} a una velocidad media de {self.velocidad_media_estimada} km/h.")


class VehiculoStaff(Vehiculo):
    def __init__(self, nombre: str, matricula: int, marca: str, modelo: str, anyo: int, tipo_vehiculo: str, cap_pasajeros: int, energia='Gasolina',
                 combustible=50, estadooptimo=True):
        super().__init__(nombre, matricula, marca, modelo, anyo, estadooptimo)
        self.tipo_vehiculo = tipo_vehiculo
        self.cap_pasajeros = cap_pasajeros
        self.energia = energia
        self.combustible = combustible
        self.pasajeros = []
        self.estado_aceite = 'Limpio'
        self.presion_neumaticos = 'Óptima'

    def __str__(self):
        generica = super().__str__()
        return f"{generica} | Tipo: {self.tipo_vehiculo}, Capacidad: {self.cap_pasajeros} pasajeros."

    def embarcar_pasajero(self, persona_staff: str) -> None:
        if len(self.pasajeros) < self.cap_pasajeros:
            self.pasajeros.append(persona_staff)
            print(f"El pasajero {persona_staff} ha subido al vehículo {self.matricula}.")
        else:
            print(f"Vehículo {self.matricula} lleno. No se pudo embarcar a {persona_staff}.")

    def mostrar_personal_bordo(self):
        if self.pasajeros:
            print(f"Personal a bordo del {self.matricula}:")
            for i in self.pasajeros:
                print(f"- {i}")
        else:
            print(f"El vehículo {self.matricula} no tiene pasajeros.")

    def mantenimiento(self, fecha: str, detalles: str) -> bool:
        print(f"Estado actual del vehículo de staff {self.matricula}:")
        print(f"- Combustible: {self.combustible}%")
        print(f"- Aceite: {self.estado_aceite}")
        print(f"- Neumáticos: {self.presion_neumaticos}")

        if self.combustible < 50:
            self.combustible = 50

        if self.estado_aceite != 'Limpio':
            self.estado_aceite = 'Limpio'

        if self.presion_neumaticos != 'Óptima':
            self.presion_neumaticos = 'Óptima'

        registro = f"[{fecha}] Mantenimiento del vehículo {self.matricula}: {detalles}"
        self.historial_reparaciones.append(registro)
        print(f"✅ Registro guardado para {self.matricula}: {detalles}")

        self.estadooptimo = True

        return True
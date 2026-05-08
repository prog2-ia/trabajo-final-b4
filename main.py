from Usuario import Usuario
from Staff import Staff
from Vehiculo import VehiculoStaff, Bici
from modalidades import Ciclismo, Senderismo

def main():
    medico_carrera = Staff("Ana López", 35, "12345678A", "Médico")
    coordinador = Staff("Luis Pérez", 42, "87654321B", "Coordinador")

    bici_carrera = Bici("Bici de Carlos", "B-001", "Trek", "Emonda", 2023, "carretera", 21)
    furgoneta = VehiculoStaff("Furgo Médica", "1111-ABC", "Ford", "Transit", 2022, "Furgoneta", 5)

    print(bici_carrera)

    bici_carrera.iniciar_uso("Carlos")
    bici_carrera.pedalear()

    print("\nLlevando la bici al taller...")
    bici_carrera.mantenimiento("24/10/2023", "Limpieza de cadena y ajuste de frenos")

    bici_carrera.finalizar_uso()

    print(furgoneta)

    furgoneta.embarcar_pasajero(medico_carrera)
    furgoneta.embarcar_pasajero(coordinador)

    furgoneta.mostrar_personal_bordo()

    print("\nLlevando la furgoneta al taller...")
    furgoneta.mantenimiento("25/10/2023", "Repostaje completo y revisión de presión")


if __name__ == "__main__":
    main()
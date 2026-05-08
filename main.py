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


# 1. Instanciamos la modalidad
ruta_bici = Ciclismo()

# 2. El equipamiento que trae nuestra persona desde el main
mochila_de_juan = ["Casco homologado", "Llaves", "Teléfono", "Bidón de agua"]

try:
    equipamiento_necesario = ruta_bici.equipamiento()

    articulos_faltantes = []
    for articulo in equipamiento_necesario:
        if articulo not in mochila_de_juan:
            articulos_faltantes.append(articulo)

    # Si la lista de faltantes tiene algo (es decir, no está vacía), lanzamos el error
    if len(articulos_faltantes) > 0:
        # Unimos los artículos que faltan con comas para que el mensaje sea claro
        faltan_str = ", ".join(articulos_faltantes)
        raise EquipamientoIncompletoException(f"A Juan le falta equipamiento obligatorio: {faltan_str}")

    print("✅ Juan tiene todo el equipamiento listo. ¡A pedalear!")

except EquipamientoIncompletoException as e:
    print(f"🛑 ACCESO DENEGADO: {e}")

if __name__ == "__main__":
    main()
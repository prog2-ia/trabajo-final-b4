from Usuario import Usuario
from Staff import Staff
from Vehiculo import VehiculoStaff, Bici
from PistaCiclismo import PistaCiclismo
from PistaSenderismo import PistaSenderismo
import interfaz


# --- PERSISTENCIA DE VEHÍCULOS ---
def guardar_vehiculo_en_txt(vehiculo):
    try:
        with open("vehiculos.txt", "a", encoding="utf-8") as fichero:
            if isinstance(vehiculo, Bici):
                linea = f"Bici|{vehiculo.nombre}|{vehiculo.matricula}|{vehiculo.marca}|{vehiculo.modelo}|{vehiculo.anyo}|{vehiculo.tipo_bici}|{vehiculo.marchas}\n"
            elif isinstance(vehiculo, VehiculoStaff):
                linea = f"Staff|{vehiculo.nombre}|{vehiculo.matricula}|{vehiculo.marca}|{vehiculo.modelo}|{vehiculo.anyo}|{vehiculo.tipo_vehiculo}|{vehiculo.cap_pasajeros}\n"
            fichero.write(linea)
    except IOError as e:
        print(f"❌ Error al guardar vehículo: {e}")


def cargar_vehiculos_desde_txt():
    flota = []
    try:
        with open("vehiculos.txt", "r", encoding="utf-8") as fichero:
            for linea in fichero:
                datos = linea.strip().split("|")
                if not datos or len(datos) < 2: continue
                tipo = datos[0]
                if tipo == "Bici":
                    flota.append(
                        Bici(datos[1], int(datos[2]), datos[3], datos[4], int(datos[5]), datos[6], int(datos[7])))
                elif tipo == "Staff":
                    flota.append(VehiculoStaff(datos[1], int(datos[2]), datos[3], datos[4], int(datos[5]), datos[6],
                                               int(datos[7])))
        print(f"✅ Se han cargado {len(flota)} vehículos históricos.")
        return flota
    except FileNotFoundError:
        return []


def inicializar_sistema():
    # Estructuras de datos base que se irán modificando en vivo
    usuarios = {
        "11111111A": Usuario("Juan Ramos", 28, "11111111A", nivel_ciclismo="aficionado",
                             nivel_senderismo="principiante"),
        "22222222B": Usuario("Ana López", 32, "22222222B", nivel_ciclismo="experto", nivel_senderismo="experto")
    }
    personal_staff = {
        "Carlos": Staff("Carlos Gómez", 40, "33333333C", "Coordinador de Rutas"),
        "Lucia": Staff("Lucía Martos", 35, "44444444D", "Mecánica Principal")
    }
    pistas = {
        "Ruta del Valle": PistaCiclismo("Ruta del Valle", dificultad=1, longitud=25.0, max_personas=2,
                                        terreno="Tierra"),
        "Senda de la Roca": PistaSenderismo("Senda de la Roca", dificultad=2, longitud=12.5, max_personas=10,
                                            terreno="Pedregoso")
    }
    return usuarios, personal_staff, pistas


def main():
    usuarios, personal_staff, pistas = inicializar_sistema()
    flota = cargar_vehiculos_desde_txt()

    # Arrancamos la super-interfaz con todos los accesos mutables
    interfaz.menu_principal(flota, usuarios, personal_staff, pistas)


if __name__ == "__main__":
    main()
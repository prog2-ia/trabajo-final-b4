from src.Personas.Usuario import Usuario
from src.Personas.Staff import Staff
from src.Vehiculos.Vehiculo import VehiculoStaff, Bici
from src.Pistas.PistaCiclismo import PistaCiclismo
from src.Pistas.PistaSenderismo import PistaSenderismo
from src import interfaz


# --- PERSISTENCIA DE VEHÍCULOS ---
def guardar_vehiculo_en_txt(vehiculo):
    try:
        with open('vehiculos.txt', 'a', encoding='utf-8') as fichero:
            if isinstance(vehiculo, Bici):
                linea = f'Bici|{vehiculo.nombre}|{vehiculo.matricula}|{vehiculo.marca}|{vehiculo.modelo}|{vehiculo.anyo}|{vehiculo.tipo_bici}|{vehiculo.marchas}\n'
            elif isinstance(vehiculo, VehiculoStaff):
                linea = f'Staff|{vehiculo.nombre}|{vehiculo.matricula}|{vehiculo.marca}|{vehiculo.modelo}|{vehiculo.anyo}|{vehiculo.tipo_vehiculo}|{vehiculo.cap_pasajeros}\n'
            fichero.write(linea)
    except IOError as e:
        print(f'Error al guardar vehículo: {e}')


def cargar_vehiculos_desde_txt():
    flota = []
    try:
        with open('vehiculos.txt', 'r', encoding='utf-8') as fichero:
            for linea in fichero:
                datos = linea.strip().split('|')
                if not datos or len(datos) < 2: continue
                tipo = datos[0]
                if tipo == 'Bici':
                    flota.append(
                        Bici(datos[1], int(datos[2]), datos[3], datos[4], int(datos[5]), datos[6], int(datos[7])))
                elif tipo == 'Staff':
                    flota.append(VehiculoStaff(datos[1], int(datos[2]), datos[3], datos[4], int(datos[5]), datos[6],
                                               int(datos[7])))
        print(f'Se han cargado {len(flota)} vehículos históricos.')
        return flota
    except FileNotFoundError:
        return []


def inicializar_sistema():
    #Usuarios y pistas predeterminados para poder probar las funciones:
    usuarios = {
        '12345678A': Usuario('Don Pepito', 28, '12345678A', nivel_ciclismo='aficionado',nivel_senderismo='principiante'),
        '67676767B': Usuario('José Francisco', 32, '67676767B', nivel_ciclismo='experto', nivel_senderismo='experto')
    }
    personal_staff = {
        'Carlitos': Staff('Carlos Gómez', 40, '87654321S', 'Coordinador de Rutas'),
        'Josemari': Staff('José María Fernández', 35, '10102020T', 'Mecánico')
    }
    pistas = {
        'Ruta chachi molona': PistaCiclismo('Ruta chachi molona', dificultad=1, longitud=25.0, max_personas=2,terreno='Tierra'),
        'Senda guay del Paraguay': PistaSenderismo('Senda guay del Paraguay', dificultad=2, longitud=12.5, max_personas=10,terreno='Montaña')
    }
    return usuarios, personal_staff, pistas


def main():
    usuarios, personal_staff, pistas = inicializar_sistema()
    flota = cargar_vehiculos_desde_txt()

    interfaz.menu_principal(flota, usuarios, personal_staff, pistas)


if __name__ == "__main__":
    main()
from Usuario import Usuario
from Staff import Staff
from Vehiculo import VehiculoStaff, Bici
from modalidades import Ciclismo, Senderismo

def main():
    def guardar_vehiculo_en_txt(vehiculo):
        # Abrimos el archivo en modo 'a' (añadir)
        try:
            with open("vehiculos.txt", "a", encoding="utf-8") as fichero:

                # Comprobamos de qué clase es el vehículo para saber qué atributos tiene
                if isinstance(vehiculo, Bici):
                    # Formateamos los datos separados por el símbolo |
                    linea = f"Bici|{vehiculo.nombre}|{vehiculo.matricula}|{vehiculo.marca}|{vehiculo.modelo}|{vehiculo.anyo}|{vehiculo.tipo_bici}|{vehiculo.marchas}\n"

                elif isinstance(vehiculo, VehiculoStaff):
                    linea = f"Staff|{vehiculo.nombre}|{vehiculo.matricula}|{vehiculo.marca}|{vehiculo.modelo}|{vehiculo.anyo}|{vehiculo.tipo_vehiculo}|{vehiculo.cap_pasajeros}\n"

                fichero.write(linea)
                print(f"Vehículo {vehiculo.matricula} guardado correctamente en el fichero.")

        except IOError as e:
            # Excepción por si hay problemas de permisos o el disco está lleno
            print(f"Error al intentar guardar en el archivo: {e}")

    def cargar_vehiculos_desde_txt():
        flota = []  # Lista donde guardaremos los objetos recuperados

        try:
            # Abrimos en modo 'r' (leer)
            with open("vehiculos.txt", "r", encoding="utf-8") as fichero:
                for linea in fichero:
                    # Quitamos el salto de línea del final y partimos por el separador
                    datos = linea.strip().split("|")

                    tipo = datos[0]

                    if tipo == "Bici":
                        # ¡Ojo! Los números hay que convertirlos de texto a int()
                        nueva_bici = Bici(
                            nombre=datos[1],
                            matricula=int(datos[2]),
                            marca=datos[3],
                            modelo=datos[4],
                            anyo=int(datos[5]),
                            tipo_bici=datos[6],
                            marchas=int(datos[7])
                        )
                        flota.append(nueva_bici)

                    elif tipo == "Staff":
                        nuevo_staff = VehiculoStaff(
                            nombre=datos[1],
                            matricula=int(datos[2]),
                            marca=datos[3],
                            modelo=datos[4],
                            anyo=int(datos[5]),
                            tipo_vehiculo=datos[6],
                            cap_pasajeros=int(datos[7])
                        )
                        flota.append(nuevo_staff)

            print(f"✅ Se han cargado {len(flota)} vehículos del fichero.")
            return flota

        except FileNotFoundError:
            # Si el programa se ejecuta por primera vez, el .txt no existirá
            print("⚠️ No existe el archivo 'vehiculos.txt'. Se iniciará con una flota vacía.")
            return []


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
# Asumimos que ya tienes importadas tus clases Bici, VehiculoStaff
# y tus funciones de ficheros (cargar_vehiculos_desde_txt y guardar_vehiculo_en_txt)
from Vehiculo import Bici, VehiculoStaff


def main():
    from main import cargar_vehiculos_desde_txt, guardar_vehiculo_en_txt
    print("Cargando sistema...")
    # 1. Al arrancar, cargamos lo que ya existe en el txt
    flota = cargar_vehiculos_desde_txt()

    # 2. Iniciamos el bucle del menú
    while True:
        print("\n" + "=" * 30)
        print("🚲 GESTIÓN DE VEHÍCULOS 🚐")
        print("=" * 30)
        print("1. Ver vehículos registrados")
        print("2. Registrar una nueva Bicicleta")
        print("3. Registrar un nuevo Vehículo de Staff")
        print("4. Salir")

        opcion = input("\nElige una opción (1-4): ")

        if opcion == "1":
            print("\n--- FLOTA ACTUAL ---")
            if not flota:
                print("No hay vehículos registrados todavía.")
            else:
                for v in flota:
                    print(v)  # Esto usa tu maravilloso método __str__

        elif opcion == "2":
            print("\n--- NUEVA BICICLETA ---")
            # AQUÍ ES DONDE ESTÁN LOS INPUTS DEL USUARIO
            try:
                nombre = input("Nombre del propietario: ")
                matricula = int(input("Matrícula (número entero): "))
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                anyo = int(input("Año de fabricación: "))
                tipo = input("Tipo (carretera/montaña/urbana): ")
                marchas = int(input("Número de marchas: "))

                # 3. Con los datos del input, creamos el objeto
                nueva_bici = Bici(nombre, matricula, marca, modelo, anyo, tipo_bici=tipo, marchas=marchas)

                # 4. Lo añadimos a la memoria RAM (la lista)
                flota.append(nueva_bici)

                # 5. Lo guardamos en el disco duro (el .txt)
                guardar_vehiculo_en_txt(nueva_bici)

                print("✅ Bicicleta registrada y guardada con éxito.")

            except ValueError:
                # Si el usuario escribe "hola" en vez de un número en la matrícula
                print("❌ Error: Debes introducir un número válido para matrícula, año o marchas.")


        elif opcion == "3":
            print("\n--- NUEVO VEHÍCULO DE STAFF ---")
            try:
                nombre = input("Nombre del responsable: ")
                matricula = int(input("Matrícula (número entero): "))
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                anyo = int(input("Año de fabricación: "))
                tipo_v = input("Tipo de vehículo (Van/4x4/Turismo): ")
                capacidad = int(input("Capacidad de pasajeros: "))
                nuevo_staff = VehiculoStaff(nombre, matricula, marca, modelo, anyo, tipo_v, capacidad)
                flota.append(nuevo_staff)
                guardar_vehiculo_en_txt(nuevo_staff)  # Recuerda modificar main.py para que esto funcione
                print("✅ Vehículo de Staff registrado y guardado con éxito.")

            except ValueError:
                print("❌ Error: Debes introducir un número válido para matrícula, año o capacidad.")

        elif opcion == "4":
            print("Saliendo del programa... ¡Hasta pronto!")
            break  # Rompe el bucle while y termina el programa

        else:
            print("❌ Opción no válida. Inténtalo de nuevo.")


# Ejecutamos el programa
if __name__ == "__main__":
    main()
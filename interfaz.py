from Vehiculo import Bici, VehiculoStaff
from Usuario import Usuario
from Staff import Staff
from PistaCiclismo import PistaCiclismo
from PistaSenderismo import PistaSenderismo
import main
from customexceptions import PistaException, UsuarioException


def menu_principal(flota, usuarios, personal_staff, pistas):
    while True:
        print("\n" + "=" * 40)
        print("   🏔️  SISTEMA DE CONTROL TOTAL DE RUTAS 🏔️")
        print("=" * 40)
        print("1. 🚐 SECCIÓN: Flota y Operaciones de Vehículos")
        print("2. 🥾 SECCIÓN: Pistas, Clima y Rutas")
        print("3. 👥 SECCIÓN: Gestión de Usuarios y Staff")
        print("4. 🚪 Salir del programa")

        opcion = input("\nSelecciona sección (1-4): ")

        if opcion == "1":
            menu_vehiculos(flota)
        elif opcion == "2":
            menu_pistas(pistas, usuarios, personal_staff)
        elif opcion == "3":
            menu_entidades(usuarios, personal_staff)
        elif opcion == "4":
            print("\nApagando sistema central... ¡Hasta la próxima!")
            break
        else:
            print("❌ Selección incorrecta.")


# ==================== SECCIÓN VEHÍCULOS ====================
def menu_vehiculos(flota):
    while True:
        print("\n--- 🚐 CONTROL DE FLOTA ---")
        print("1. Listar vehículos y sus estados")
        print("2. Registrar Bicicleta (.txt)")
        print("3. Registrar Vehículo de Staff (.txt)")
        print("4. Reportar Avería de un vehículo")
        print("5. Pasar Mantenimiento Completo (Limpieza de estados + Log)")
        print("6. Iniciar Uso de un Vehículo")
        print("7. Finalizar Uso / Devolución")
        print("8. Subir pasajero al Staff (Exclusivo Coche Staff)")
        print("9. Ver pasajeros a bordo (Exclusivo Coche Staff)")
        print("10. Volver")

        opc = input("\nAcción: ")

        if opc == "1":
            print("\n" + "•" * 15 + " FLOTA ACTUAL DE VEHÍCULOS " + "•" * 15)
            if not flota:
                print("No hay vehículos registrados todavía.")
            for idx, v in enumerate(flota):
                estado = "Óptimo" if v.estadooptimo else "Averiado/Falta Mantenimiento"
                disp = "Libre" if v.disponible else "En uso"
                rep = "En reparación" if v.reparacion else "Funcionando"
                print(f"\n👉 ÍNDICE [{idx}]")
                print(v)
                print(f"   -> Estado: {estado} | {disp} | {rep}")
            print("\n" + "•" * 57)

        elif opc in ("2", "3"):
            try:
                nom = input("Propietario/Responsable: ")
                mat = int(input("Matrícula (int): "))
                mar = input("Marca: ")
                mod = input("Modelo: ")
                any_ = int(input("Año: "))

                if opc == "2":
                    tipo = input("Tipo (carretera/montaña/urbana): ")
                    m = int(input("Marchas: "))
                    nv = Bici(nom, mat, mar, mod, any_, tipo_bici=tipo, marchas=m)
                else:
                    tipo_v = input("Tipo Vehículo (Van/4x4): ")
                    cap = int(input("Capacidad pasajeros: "))
                    nv = VehiculoStaff(nom, mat, mar, mod, any_, tipo_vehiculo=tipo_v, cap_pasajeros=cap)

                flota.append(nv)
                main.guardar_vehiculo_en_txt(nv)
                print("✅ Guardado con éxito.")
            except ValueError:
                print("❌ Error en campos numéricos.")

        elif opc in ("4", "5", "6", "7", "8", "9"):
            if not flota:
                print("❌ No hay vehículos registrados en la flota para realizar operaciones.")
                continue

            # --- LISTADO DE AYUDA CON ÍNDICES ---
            print("\n📋 VEHÍCULOS DISPONIBLES EN EL SISTEMA:")
            for i, veh in enumerate(flota):
                tipo_clase = "Bicicleta" if isinstance(veh, Bici) else "Vehículo Staff"
                print(f"  [{i}] Matrícula: {veh.matricula} | {veh.marca} {veh.modelo} ({tipo_clase} de {veh.nombre})")
            print("-" * 45)

            try:
                idx = int(input(f"Elige el índice del vehículo (0 a {len(flota) - 1}): "))
                v = flota[idx]

                if opc == "4":
                    print(f"\n{v.reporteaveria()}")
                    v.estadooptimo = False
                elif opc == "5":
                    f = input("Fecha de hoy: ")
                    d = input("Detalles del trabajo realizado: ")
                    v.mantenimiento(f, d)
                    v.reparacion = False
                elif opc == "6":
                    u_nom = input("Nombre de la persona que lo toma: ")
                    v.iniciar_uso(u_nom)
                elif opc == "7":
                    v.finalizar_uso()
                elif opc == "8":
                    if isinstance(v, VehiculoStaff):
                        p_staff = input("Nombre del miembro del staff a subir: ")
                        v.embarcar_pasajero(p_staff)
                    else:
                        print("❌ Las bicicletas no llevan pasajeros de staff.")
                elif opc == "9":
                    if isinstance(v, VehiculoStaff):
                        v.mostrar_personal_bordo()
                    else:
                        print("❌ Las bicicletas no tienen cabina de pasajeros.")
            except (ValueError, IndexError):
                print("❌ Selección de índice inválida.")

        elif opc == "10":
            break


# ==================== SECCIÓN PISTAS ====================
def menu_pistas(pistas, usuarios, personal_staff):
    while True:
        print("\n--- 🥾 GESTIÓN DE PISTAS Y CLIMA ---")
        print("1. Ver pistas detalladas (Método __str__ de Pista)")
        print("2. Registrar / Crear nueva Pista")
        print("3. Inscribir Usuario (Operador +=)")
        print("4. Dar de Baja Usuario (Operador -=)")
        print("5. Agregar Punto de Interés Geográfico (Operador +)")
        print("6. Cambiar Clima Dinámico (Random)")
        print("7. Asignar Líder de Staff a la pista")
        print("8. Cerrar Pista por seguridad")
        print("9. Abrir Pista")
        print("10. Volver")

        opc = input("\nAcción: ")

        if opc == "1":
            print("\n" + "▲" * 15 + " ESTADO GENERAL DE LAS PISTAS " + "▲" * 15)
            if not pistas:
                print("No hay pistas creadas todavía.")
            for p in pistas.values():
                print("\n" + p.__str__())
                print(f"   👥 Cantidad de Inscritos reales (len): {len(p)}")
                print(f"   📋 Listado Alfabético: {p.lista_participantes()}")
            print("\n" + "▲" * 60)

        elif opc == "2":
            nom = input("Nombre de la pista única: ")
            try:
                dif = int(input("Dificultad (0=Sencilla, 1=Media, 2=Difícil): "))
                long = float(input("Longitud en km (float): "))
                mx = int(input("Plazas máximas (int): "))
                terr = input("Tipo de terreno: ")
                t_pista = input("¿Tipo de pista? (Ciclismo/Senderismo): ").lower()

                if t_pista == "ciclismo":
                    pistas[nom] = PistaCiclismo(nom, dif, long, mx, terr)
                else:
                    pistas[nom] = PistaSenderismo(nom, dif, long, mx, terr)
                print("✅ Pista dada de alta en el sistema.")
            except ValueError:
                print("❌ Valores numéricos inválidos.")

        elif opc in ("3", "4", "5", "6", "7", "8", "9"):
            if not pistas:
                print("❌ No hay pistas en el sistema para realizar operaciones.")
                continue

            # --- LISTADO DE AYUDA CON LOS NOMBRES DE LAS PISTAS ---
            print("\n🗺️  PISTAS DISPONIBLES EN EL SISTEMA:")
            for name, pista_obj in pistas.items():
                tipo_p = "Ciclismo" if isinstance(pista_obj, PistaCiclismo) else "Senderismo"
                print(f"  📍 {name} ({tipo_p})")
            print("-" * 45)

            p_key = input("Introduce el NOMBRE exacto de la pista: ")
            if p_key not in pistas:
                print("❌ Pista no localizada.")
                continue
            p = pistas[p_key]

            try:
                if opc == "3":
                    # --- LISTADO DE AYUDA DE USUARIOS ---
                    print("\n👥 USUARIOS REGISTRADOS:")
                    for d, u in usuarios.items():
                        print(f"  • DNI: {d} | Nombre: {u.nombre}")
                    print("-" * 35)

                    dni = input("DNI del usuario a inscribir: ")
                    if dni in usuarios:
                        p += usuarios[dni]
                        print("✅ 🚴‍♂️/🚶‍♂️ Procesado con += correctamente.")
                    else:
                        print("❌ El DNI introducido no corresponde a ningún usuario.")

                elif opc == "4":
                    # --- LISTADO DE AYUDA DE INSCRITOS EN ESTA PISTA ---
                    print(f"\n👥 PARTICIPANTES ACTUALES EN {p.nombre}:")
                    participantes = p.lista_participantes()
                    if isinstance(participantes, list):
                        for u_inscrito in p.participantes:
                            print(f"  • DNI: {u_inscrito.dni} | Nombre: {u_inscrito.nombre}")
                    else:
                        print(f"  {participantes}")
                    print("-" * 35)

                    dni = input("DNI del usuario a eliminar: ")
                    if dni in usuarios:
                        p -= usuarios[dni]
                        print("✅ Retirado con -= correctamente.")
                    else:
                        print("❌ El DNI introducido no corresponde a ningún usuario.")

                elif opc == "5":
                    punto = input("Nombre del mirador / punto de interés: ")
                    p+= punto  # Ejecuta __add__
                    print(f"📍 Punto '{punto}' indexado con éxito.")
                elif opc == "6":
                    print(f"\n{p.cambiar_clima()}")
                elif opc == "7":
                    # --- LISTADO DE AYUDA DE MIEMBROS DE STAFF ---
                    print("\n💼 PERSONAL DE STAFF DISPONIBLE:")
                    for name in personal_staff.keys():
                        print(f"  • {name}")
                    print("-" * 35)

                    st_name = input("Nombre del Staff elegido: ")
                    if st_name in personal_staff:
                        print(f"\n{p.assignar_staff(personal_staff[st_name])}")
                    else:
                        print("❌ Ese miembro de staff no existe.")
                elif opc == "8":
                    print(f"\n{p.cerrar_pista()}")
                elif opc == "9":
                    print(f"\n{p.abrir_pista()}")
            except PistaException as e:
                print(f"🛑 EXCEPCIÓN CRÍTICA DE PISTA: {e}")

        elif opc == "10":
            break


# ==================== SECCIÓN ENTIDADES ====================
def menu_entidades(usuarios, personal_staff):
    while True:
        print("\n--- 👥 GESTIÓN DE PERSONAS ---")
        print("1. Listar Usuarios y Staff actuales")
        print("2. Registrar un nuevo Usuario")
        print("3. Registrar un nuevo miembro de Staff")
        print("4. Modificar niveles de un Usuario (Acción del Staff)")
        print("5. Volver")

        opc = input("\nAcción: ")

        if opc == "1":
            print("\n" + "👥" * 10 + " PERFILES DE USUARIOS " + "👥" * 10)
            if not usuarios: print("No hay usuarios registrados.")
            for u in usuarios.values():
                print(f"\n- {u.__repr__()}\n  {u}")

            print("\n" + "💼" * 10 + " EQUIPO DE STAFF " + "💼" * 10)
            if not personal_staff: print("No hay personal de staff registrado.")
            for s in personal_staff.values():
                print(f"\n- {s.__repr__()}\n  {s}")
            print("\n" + "═" * 42)

        elif opc == "2":
            try:
                nom = input("Nombre completo: ")
                ed = int(input("Edad: "))
                dni = input("DNI (9 caracteres): ")
                nc = input("Nivel Ciclismo (Principiante/Aficionado/Experto/None): ")
                ns = input("Nivel Senderismo (Principiante/Aficionado/Experto/None): ")

                nc = None if nc.lower() == "none" else nc
                ns = None if ns.lower() == "none" else ns

                usuarios[dni] = Usuario(nom, ed, dni, nc, ns)
                print("✅ Usuario instanciado.")
            except (ValueError, UsuarioException) as e:
                print(f"❌ Error al crear usuario: {e}")

        elif opc == "3":
            try:
                nom = input("Nombre de pila (ID): ")
                ed = int(input("Edad: "))
                dni = input("DNI: ")
                rol = input("Rol laboral: ")
                personal_staff[nom] = Staff(nom, ed, dni, rol)
                print("✅ Miembro de Staff contratado.")
            except (ValueError, UsuarioException) as e:
                print(f"❌ Error: {e}")

        elif opc == "4":
            if not personal_staff or not usuarios:
                print("❌ Se requiere al menos 1 miembro del Staff y 1 Usuario en memoria para esta acción.")
                continue

            # --- LISTADO DE AYUDA DE STAFF ---
            print("\n💼 PERSONAL DE STAFF AUTORIZADO:")
            for name in personal_staff.keys():
                print(f"  • {name}")
            print("-" * 35)
            st_key = input("Nombre del Staff que autoriza el cambio: ")
            if st_key not in personal_staff:
                print("❌ Staff no válido.")
                continue

            # --- LISTADO DE AYUDA DE USUARIOS ---
            print("\n👥 USUARIOS DISPONIBLES:")
            for d, u in usuarios.items():
                print(f"  • DNI: {d} | Nombre: {u.nombre}")
            print("-" * 35)
            dni_u = input("DNI del usuario a evaluar: ")
            if dni_u not in usuarios:
                print("❌ Usuario no registrado.")
                continue

            st = personal_staff[st_key]
            us = usuarios[dni_u]

            act = input("¿Qué nivel deseas alterar? (Ciclismo/Senderismo): ").lower()
            nuevo_nv = input("Nuevo rango (Principiante / Aficionado / Experto / None): ")
            nuevo_nv = None if nuevo_nv.lower() == "none" else nuevo_nv

            try:
                if "cicli" in act:
                    print(f"\n{st.cambiar_nivel_ciclismo(us, nuevo_nv)}")
                else:
                    print(f"\n{st.cambiar_nivel_senderismo(us, nuevo_nv)}")
            except UsuarioException as e:
                print(f"🛑 Operación denegada por datos inválidos: {e}")

        elif opc == "5":
            break
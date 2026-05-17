Gestión de Usuarios y Pistas de Actividades al Aire Libre
-Álex Piñeiro Núñez, Álex Sánchez Sánchez-


-Descripción del Proyecto-
En el proyecto se permite gestionar de forma integral usuarios, staff, pistas de actividades al aire libre (ciclismo y senderismo) y una flota completa de vehículos con persistencia de datos.

Se puede:
-Registrar usuarios con niveles de ciclismo y senderismo (0=Principiante, 1=Aficionado, 2=Experto).
-Registrar personal de staff y permitir que modifiquen los niveles de los usuarios.
-Crear pistas con diferentes niveles de dificultad, longitud, capacidad y tipo de terreno.
-Inscribir y dar de baja a usuarios en pistas (verificando nivel, plazas, estado de pista y si ya están inscritos).
-Añadir puntos de interés geográfico a las pistas.
-Gestionar el estado de las pistas (abierta/cerrada) y alterar su clima de forma dinámica.
-Administrar una flota de vehículos (Bicicletas y Vehículos de Staff) controlando su estado óptimo, aforos y mantenimientos.
-Guardar y cargar automáticamente el histórico de la flota de vehículos mediante ficheros (.txt).
-Calcular tiempos estimados de ruta y obtener el equipamiento necesario mediante el sistema de Modalidades.
-Interactuar con todas las clases a través de un Menú de Consola interactivo.


------------------------------------------------------------------

Para que funcione:

-Instalar los requisitos (pip install -r requirements.txt)
-Ejecutar el archivo 'main.py' para lanzar la interfaz interactiva.
-Importar las clases necesarias si se quiere usar mediante código:
	from src.Personas.Usuario import Usuario
	from src.Personas.Staff import Staff
	from src.Pistas.PistaCiclismo import PistaCiclismo
	from src.Pistas.PistaSenderismo import PistaSenderismo
	from src.Vehiculos.Vehiculo import Bici, VehiculoStaff
	from src.Modalidades.modalidades import Ciclismo, Senderismo


------------------------------------------------------------------

Tutorial (Uso por código):

-Crear usuarios, se pide nombre, edad, dni y puede tener nivel de ciclismo y/o senderismo:
(El nivel puede ser tanto 0, 1 o 2 como principiante, aficionado o experto, funcionan igual)

	Usuario con nivel de ciclismo y senderismo:
		Pepito = Usuario('Pepito', 25, '12345678A', nivel_ciclismo='aficionado', nivel_senderismo='principiante')

	Usuario sin nivel:
		Juanito = Usuario('Juanito', 67, '87654321B', nivel_senderismo=0)


-Crear Staff, que piden nombre, edad, dni y rol:

	Jorgito = Staff("Jorgito", 40, '11223344C', 'Monitor')


-Crear pistas, tanto de senderismo como de ciclismo, funcionan igual:
(Las dificultades pueden ser 0, 1 o 2)

	Pista de ciclismo:
		pista1 = PistaCiclismo('Pista Chachiguay', dificultad=1, longitud=15, max_personas=10, terreno='Montañoso')

	Pista de senderismo:
		pista2 = PistaSenderismo('Pista Cho', 0, 5, 20, terreno='Bosque')


-Asignar staff a una pista (de base se crean sin staff):

	pista1.asignar_staff(Jorgito)


-Inscribir y dar de baja usuarios en pistas (Usando sobrecarga de operadores += y -=):
	
	Inscribir:
		pista2 += Juanito
	
	Dar de baja:
		pista2 -= Juanito

	Se verifica mediante Excepciones Personalizadas que se cumplan todos los requisitos de acceso.


-Añadir Puntos de Interés a una pista (Usando sobrecarga de operador +):
	
		pista1 + "Mirador del Águila"


-Modificar nivel de usuario siendo staff:

	Jorgito.cambiar_nivel_ciclismo(Pepito, "experto")


-Consultar lista de participantes y plazas restantes:

	pista1.lista_participantes()
	pista2.plazas()


-Cambiar el clima (Se elige de forma aleatoria):

	pista1.cambiar_clima()


-Abrir y cerrar pista:

	pista1.cerrar_pista()
	pista1.abrir_pista()


-Crear y gestionar Vehículos (Con persistencia en vehiculos.txt):

	bici1 = Bici('Bici Alquiler', 101, 'Orbea', 'Alma', 2022, 'montaña', 21)
	furgo = VehiculoStaff('Transporte Staff', 999, 'Ford', 'Transit', 2020, 'Furgoneta', 4)

	bici1.iniciar_uso("Pepito")
	furgo.embarcar_pasajero("Jorgito")
	bici1.reporteaveria()


-Modalidades deportivas y cálculos (Controlando que la distancia no sea negativa):

	ruta_bici = Ciclismo()
	
	print(ruta_bici.calcular_tiempo(30))
	print(ruta_bici.equipamiento())


También están implementados los métodos __str__ y __repr__ para poder visualizar la información completa de todas las entidades.

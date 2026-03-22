Gestión de Usuarios y Pistas de Actividades al Aire Libre
-Álex Piñeiro Núñez, Álex Sánchez Sánchez-


-Descripción del Proyecto-
En el proyecto se permite gestionar usuarios, staff y pistas de actividades al aire libre tanto de ciclismo como de senderismo.

Se puede:
-Registrar usuarios con niveles de ciclismo y senderismo.
-Asignar staff a pistas y permitir que modifiquen los niveles de los usuarios.
-Crear pistas con diferentes niveles de dificultad, longitud y capacidad.
-Inscribir usuarios en pistas según su nivel y disponibilidad.
-Gestionar el estado de las pistas y el clima.



------------------------------------------------------------------

Para que funcione:

-Instalar los requisitos (pip install -r requirements.txt)
-Importar las clases necesarias:
	from Persona import Usuario, Staff
	from Pista import PistaCiclismo, PistaSenderismo


------------------------------------------------------------------

Tutorial:

-Crear usuarios, se pide nombre, edad, dni y puede tener nivel de ciclismo y/o senderismo:
(El nivel puede ser tanto 0, 1 o 2 como principiante, aficionado o experto, funcionan igual)

	Usuario con nivel de ciclismo y senderismo:
		Pepito = Usuario('Pepito', 25, '12345678A', nivel_ciclismo='aficionado',nivel_senderismo='principiante')

	Usuario sin nivel:
		Juanito = Usuario('Juanito', 67, '87654321B',nivel_senderismo=0)


-Crear Staff, que piden nombre, edad, dni y rol:

	Jorgito = Staff("Jorgito", 40, '11223344C', 'Monitor')


-Crear pistas, tanto de senderismo como de ciclismo, funcionan igual:
(Las dificultades pueden ser 0, 1 o 2)

	Pista de ciclismo:
		pista1 = PistaCiclismo('Pista Chachiguay', dificultad=1, longitud=15, max_personas=10, terreno='Montañoso')

	Pista de senderismo:
		pista2 = PistaSenderismo('Pista Cho', 0, 5, 20, terreno='Bosque de pistachos')


-Asignar staff a una pista (de base se crean sin staff):

	pista1.asignar_staff(Jorgito)


-Inscribir usuarios en pistas:

	pista2.participa(Juanito)

	Se verifica que se cumplan todos los requisitos (El usuario no esté ya inscrito, que queden plazas, que tenga el nivel suficiente, etc...)


-Modificar nivel de usuario siendo staff:

	Jorgito.cambiar_nivel_ciclismo(Pepito, "EXPERTO")


-Consultar lista de participantes:

	pista1.lista_participantes()


-Consultar las plazas restantes:

	pista2.lista_participantes()


-Cambiar el clima (Se elige tanto al llamar al método como al crearse la pista de forma aleatoria):

	pista1.cambiar_clima()


-Abrir y cerrar pista:

	pista1.cerrar_pista()
	pista1.abrir_pista()


También están implementados los métodos __str__ y __repr__ para poder visualizar la información de los usuarios y pistas.
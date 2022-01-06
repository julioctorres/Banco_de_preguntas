from usuario import Usuario
from categoria import Categoria
from preguntas import Preguntas


while (True):
            #### Menu de inicialización de cada usuario

    print("""\n             Nota: Señor usuario, si desea hacer algun cambio en el cuestionario
             por favor dirigirse a la carpeta que se encuentra en formato json. 
             Alli encontrara las cinco preguntas por categorias  \n             
        """)

    print("""Señor Usuario, por favor ingrese alguna de las siguientes opciones: \n 
            
            1) Agregar Usuario \n
            2) Inicio del cuestionario \n
            3) Fin del juego \n
        """)

    seleccion = int(input())

    if seleccion == 1: ##### Agregamos un nuevo usuario 
        
        Usuario.Crear_Usuario()

    elif seleccion == 2: ##### Damos la inicializacion al banco de preguntas

        Preguntas.Banco_de_preguntas()

    elif seleccion == 3: ### Se culmina el juego 

        print("\n Adios \n") 
        exit()

    else: ## El usuario ingresa mal el digito
        print("Ingreso un nuemero equivocado \n") 

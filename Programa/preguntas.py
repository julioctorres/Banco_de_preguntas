from categoria import Categoria
from puntuacion import Puntuacion


class Preguntas:
    
    def __init__(self, pregunta):
        self.pregunta = pregunta

    def Banco_de_preguntas(): ## Se crea el banco de preguntas 
        if Categoria.Categoria_fin == 1:
            print("En esta primera serie, las preguntas seran relacionadas con aritmetica basica.")
            pregunta = int(input("Ingrese un numero de 1 a 5"))    
            ### Se inicializa la ronda uno de preguntas
            if pregunta == 1: ### selecciona una de las cinco preguntas de la categoria seleccionadas por el usuario
                print ("""
                            ¿Cuanto es 426/2?
                            
                            1) 210
                            2) 213
                            3) 142
                            4) 100
                """) ### Realiza la pregunta 
                respuesta = int(input()) ## Solicita al usuario un numero de repsuesta
                
                if respuesta == 2: # Pregunta si la respuesta fue acertada o no
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1 ## avanzamos de categoria
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1  ## Seguimos en la acomulacion de puntos
                        
                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados ) ## despedida al usuario por haber errado la pregunta
                
            elif pregunta == 2: ### selecciona una de las cinco preguntas  seleccionadas por el usuario
                print ("""
                            ¿Cuanto es 168*2?
                            
                            1) 340
                            2) 420
                            3) 126
                            4) 336
                """)
                respuesta = int(input()) # ## Solicita al usuario un numero de repsuesta
                if respuesta == 4: # Pregunta si la respuesta fue acertada o no
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1 ## avanzamos de categoria
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1 ## Seguimos en la acomulacion de puntos
                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados ) ## despedida al usuario por haber errado la pregunta
                
            elif pregunta == 3: ### selecciona una de las cinco preguntas  seleccionadas por el usuario
                print ("""
                            ¿Cuanto es 5+2*6?
                            
                            1) 40
                            2) 18
                            3) 17
                            4) 42
                """)
                respuesta = int(input()) # ## Solicita al usuario un numero de repsuesta
                
                if respuesta == 3: # Pregunta si la respuesta fue acertada o no
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1 ## avanzamos de categoria
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1 ## Seguimos en la acomulacion de puntos
                    
                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )
                
            elif pregunta == 4:
                print ("""
                            ¿Cuanto es 458+122?
                            
                            1) 580
                            2) 579
                            3) 581
                            4) 578
                """)
                respuesta = int(input())
                
                if respuesta == 1: # Pregunta si la respuesta fue acertada o no
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1

                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )


            elif pregunta == 5:
                print ("""
                            ¿Cuanto es raiz_cuadrada_de(16)?
                            
                            1) 5
                            2) 6
                            3) 4
                            4) 3
                """)
                respuesta = int(input())
                
                if respuesta == 3: # Pregunta si la respuesta fue acertada o no
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1
                
                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )

##############################################################################################################    
        if Categoria.Categoria_fin == 2:
            print("En estra segunda serie, las preguntas seran relacionadas con aritmetica avanzada.")
            pregunta = int(input("Ingrese un numero de 1 a 5"))    
           
            if pregunta == 1: ### selecciona una de las cinco preguntas de la categoria seleccionadas por el usuario
                print ("""
                            ¿Cuanto es 12-(-5+5)-14?
                            
                            1) -5
                            2) 5
                            3) 0
                            4) 6
                """)
                respuesta = int(input())
               
                if respuesta == 1:
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1
                        
                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )
                
            elif pregunta == 2:
                print ("""
                            ¿Cuanto es 9-(7*10-9)?
                            
                            1) 54
                            2) 48
                            3) 50
                            4) -52
                """)
                respuesta = int(input())
                
                if respuesta == 4:
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1
                
                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )
                
            elif pregunta == 3:
                print ("""
                            ¿Cuanto es 12.85  -1.3(43.42 - 12.79)?
                            
                            1) -30
                            2) -25.1546
                            3) -26.9690
                            4) -26
                """)
                respuesta = int(input())
                
                if respuesta == 3:
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1                    
                
                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )
                
            elif pregunta == 4:
                print ("""
                            ¿Cuanto es (10/8)-(2/3 - 5/2)?
                            
                            1) 37/12
                            2) 14/9
                            3) 8/9
                            4) 3/12
                """)
                respuesta = int(input())
                
                if respuesta == 1:
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1

                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )


            elif pregunta == 5:
                print ("""
                            ¿Cuanto es (8/6)(4/9 + 8/2))?
                            
                            1) 159/27
                            2) 161/27
                            3) 160/27
                            4) 150/15
                """)
                respuesta = int(input())
                
                if respuesta == 3:
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1

                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )
    
########################################################################################################################################    
        if Categoria.Categoria_fin == 3:
            print("En estra tercera serie, las preguntas seran relacionadas con algebra basica.")
            pregunta = int(input("Ingrese un numero de 1 a 5"))    
            
            if pregunta == 1: ### selecciona una de las cinco preguntas de la categoria seleccionadas por el usuario
                print ("""
                            ¿Cual es el valor de x cuando 2x + 3x = 5?
                            
                            1) 0
                            2) 1
                            3) 2
                            4) 3
                """)
                respuesta = int(input())
                
                if respuesta == 2:
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1
                        
                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )
                
            elif pregunta == 2:
                print ("""
                            ¿Cuanto es Cual es el valor de x cuando 2x + 3x = 10?
                            
                            1) 0
                            2) 5
                            3) 15
                            4) 2
                """)
                respuesta = int(input())
                
                if respuesta == 4:
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1
                
                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )
                
            elif pregunta == 3:
                print ("""
                            ¿Cual es el valor de x cuando 2x + 3x = 15?
                            
                            1) 0
                            2) 2
                            3) 3
                            4) 4
                """)
                respuesta = int(input())
                
                if respuesta == 3:
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1

                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )
                
            elif pregunta == 4:
                print ("""
                            ¿Cual es el valor de x cuando 2x + 3x = 20?
                            
                            1) 4
                            2) 3
                            3) 2
                            4) 1
                """)
                respuesta = int(input())
                
                if respuesta == 1:
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1
                
                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )


            elif pregunta == 5:
                print ("""
                            ¿Cual es el valor de x cuando 2x + 3x = 25?
                            
                            1) 2
                            2) 3
                            3) 5
                            4) 6
                """)
                respuesta = int(input())
                
                if respuesta == 3:
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1

                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )

 ###################################################################################################################################   
        if Categoria.Categoria_fin == 4: ### selecciona una de las cinco preguntas de la categoria seleccionadas por el usuario
            print("En esta cuarta serie, las preguntas seran relacionadas con Cultura general.")
            pregunta = int(input("Ingrese un numero de 1 a 5"))    
            if pregunta == 1:
                print ("""
                            ¿Cuántos litros de sangre tiene una persona adulta?
                            
                            1) 2 y 4
                            2) 4 y 6
                            3) 7
                            4) 0.5
                """)
                respuesta = int(input())
               
                if respuesta == 2:
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1
                        
                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )
                
            elif pregunta == 2:
                print ("""
                            ¿Quién es el autor de la frase "Pienso, luego existo"?
                            
                            1) Platón
                            2) Francis Bacon
                            3) Socrates
                            4) Descartes
                """)
                respuesta = int(input())

                if respuesta == 4:
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1                
                
                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )
                
            elif pregunta == 3:
                print ("""
                            ¿Cuál es el país más grande y el más pequeño del mundo?
                            
                            1) China y Nauru
                            2) Canadá y Mónaco
                            3) Rusia y Vaticano
                            4) India y San Marino
                """)
                respuesta = int(input())
                
                if respuesta == 3:
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1

                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )
                
            elif pregunta == 4:
                print ("""
                            ¿Cuál es el grupo de palabras escritas correctamente?
                            
                            1) Metamorfosis, extranjero, diversidad, equilibrio
                            2) Metamorfosis, extranjero, diversidac, equilivrio
                            3) Metaformosis, estranjero, diversidad, ekilibrio
                            4) Metamorfosis, extrangero, dibersidad, equilibrio
                """)
                respuesta = int(input())

                if respuesta == 1:
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1

                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )


            elif pregunta == 5:
                print ("""
                            ¿Cuál es el libro más vendido en el mundo después de la Biblia?
                            
                            1) El Señor de los Anillos
                            2) El principito
                            3) Don Quijote de la Mancha
                            4) Cien años de Soledad

                """)
                respuesta = int(input())

                if respuesta == 3:
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1

                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )

#####################################################################################################################################    
        if Categoria.Categoria_fin == 5: ### selecciona una de las cinco preguntas de la categoria seleccionadas por el usuario
            print("En estra primera serie, las preguntas seran relacionadas con cultura general.")
            pregunta = int(input("Ingrese un numero de 1 a 5"))    
            if pregunta == 1:
                print ("""
                            ¿Cuántos decimales tiene el número pi π?
                            
                            1) Dos
                            2) Cien
                            3) Infinitos
                            4) Mil
                """)
                respuesta = int(input())

                if respuesta == 2:
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1
                        
                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )
                
            elif pregunta == 2:
                print ("""
                            La sal común está formada por dos elementos, ¿cuáles son?
                            
                            1) Sodio y potasio
                            2) Sodio y carbono
                            3) Potasio y cloro
                            4) Sodio y cloro
                """)
                respuesta = int(input())

                if respuesta == 4:
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1      

                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )
                
            elif pregunta == 3:
                print ("""
                            ¿Cuántos jugadores por equipo participan en un partido de voleibol?
                            
                            1) 4 jugadores
                            2) 7 jugadores
                            3) 6 jugadores
                            4) 5 jugadores
                """)
                respuesta = int(input())

                if respuesta == 3:
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1

                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )
                
            elif pregunta == 4:
                print ("""
                            ¿Cuáles son los representantes más destacados de la literatura renacentista?
                            
                                1) Miguel de Cervantes, William Shakespeare, Luis de Camões.
                                2) Leonardo da Vinci, Miguel Angel Buonarroti, Sandro Boticelli
                                3) Caravaggio, Bernini, Borromini
                                4) Goethe, Victor Hugo, Gustavo Adolfo Bécquer
                """)
                respuesta = int(input())

                if respuesta == 1:
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1

                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )


            elif pregunta == 5:
                print ("""
                            ¿Quién pintó la obra "Guernica"?
                            
                            1) Paul Cézanne
                            2) Diego Rivera
                            3) Pablo Picasso
                            4) Salvador Dalí
                """)
                respuesta = int(input())

                if respuesta == 3:
                    print("Repuesta   ACERTADA, pasas a la siguiente ronda")
                    Categoria.Categoria_fin = Categoria.Categoria_fin + 1
                    Puntuacion.puntos_acomulados = Puntuacion.puntos_acomulados + 1
                    print("FELICITACIONES, ACABA DE RESPONDER CORRECTAMENTE, SU PUNTUACION ES:  ", Puntuacion.puntos_acomulados )
                else:
                    print("Respuesta equivocada, Su puntuacion es:  ", Puntuacion.puntos_acomulados )
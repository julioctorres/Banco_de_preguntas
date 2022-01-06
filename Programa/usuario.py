import json
 
class Usuario:
    
    def __init__(self, nombre):
        self.nombre = nombre # Se crean los atributos
        self.id = ()
        self.puntos = ()

    def Crear_Usuario():
        nombre = input("Ingrese su nombre:  ") # Se solicita el nombre del usuario
        id = int(input("Ingrese su id:  "))    # Se solicita el id del nuevo usuario
        puntos = print("En el momento sus puntos son 0")
        return nombre + " " + str(id) + " " + str(puntos)

    def __init__ (self, datos):

        ## Guardamos los datos de el nuevo usuario para tener una trazabilidad de cada usuario asignado
        fileName = "my-data.json"
        jsonObject = {
            "Nombre": self.nombre,
            "Id": self.id,
            "Puntos": self.puntos,
        }

        file = open(fileName, "w")
        json.dump(jsonObject, file)
        file.close()
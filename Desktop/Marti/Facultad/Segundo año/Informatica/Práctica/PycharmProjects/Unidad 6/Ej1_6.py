class Esfera:
    def __init__(self, radio):
        self.__nombre = "Esfera"      #nombre predeterminado por el nombre de la clase #puse en privado con __
        self.radio = radio          #def la radio porque puede variar
    pass

class Cubo:
    def __init__(self, lado):
        self.nombre = "Cubo"
        self.lado = lado
    pass

class PrismaRectangular:
    def __init__(self, base, altura, profundidad):
        self.nombre = "PrismaRectangular"
        self.base = base
        self.altura = altura
        self.profundidad = profundidad
    pass

print(Cubo(4).lado)

#Médicos
[{"user_id":'raquel','password':'supersec456'},
{"user_id":'irma','password':'supersec789',},
{"user_id":'pablo','password':'supersec012'},
{"user_id":'pedro','password':'supersec345'},
{"user_id":'juan','password':'supersec678'},
{"user_id":'alfredo','password':'supersec901'}]

#Pacientes
{"user_id":'sofia','password':'supersec46'},
{"user_id":'manuel','password':'supersec79',},
{"user_id":'tobias','password':'supersec02'},
{"user_id":'laura','password':'supersec35'},
{"user_id":'florencia','password':'supersec68'},
{"user_id":'santiago','password':'supersec91'}

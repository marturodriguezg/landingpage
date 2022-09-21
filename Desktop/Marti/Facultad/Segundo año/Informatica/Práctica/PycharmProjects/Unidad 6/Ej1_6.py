class Esfera:
    def __init__(self, nombre, radio):
        self.nombre = nombre
        self.radio = radio

    def devolver_nombre_esfera (self): #para definir un metodo es como una fx y se pone entre () self
        print("Nombre de la esfera es: ", self.nombre)

    def devolver_radio (self):
        print("La radio de la esfera es: ", self.radio)

class Cubo:
    def __init__(self, nombre, lado):
        self.nombre = nombre
        self.lado = lado

    def devolver_nombre_cubo(self):
        print("El nombre del Cubo es: ", self.nombre)

    def devolver_radio(self):
        print("El lado de la esfera es: ", self.lado)


class Prisma_rectangular:
    def __init__(self, nombre, base, altura, profundidad):
        self.nombre = nombre
        self.base = base
        self.altura = altura
        self.profundad = profundidad

    def devolver_nombre_prisma(self):
        print("El nombre del Prisma Rectangular es: ", self.nombre)

    def devolver_atributos(self):
        print("Los atributos del Prisma Rectangular son: ", self.base, ", ", self.profundad, ", ", self.altura)

esfera1 = Esfera("pepe", 3)                 #Yo creo mi esfera en una var con mi nombre y radio que son los atrib
print(esfera1.devolver_nombre_esfera())     #le pido que me devuelva con la fx el nombre de la esfera



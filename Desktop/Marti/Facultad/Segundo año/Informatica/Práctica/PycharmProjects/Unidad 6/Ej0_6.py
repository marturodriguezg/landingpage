
class Ballena:
    def __init__ (self, nombre, edad, sexo, peso, mamifero):        #Constructor
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.mamifero = mamifero

    def nadar(self):        #automaticamente me tira el self        #se dice metodo cuando la fx pertenece a un objeto
        return f"{self.nombre} está nadando... "

    def saltar(self):
        return f"{self.nombre} va a saltar la escollera..."

    def alimentarse(self):
        return f"{self.nombre} está alimentandose..."

    def descansar(self):
        return  f"{self.nombre} zzz...."

    def estado(self):
        return f"\n\tNombre: {self.nombre}" \
            f"\n\tEdad: {self.edad}" \
            f"\n\tSexo: {self.sexo}" \
            f"\n\tPeso: {self.peso}" \
            f"\n\tMamifero: {'SI' if self.mamifero else 'NO'}





willy = Ballena("Willy", 9, "M", 2000, True)

print(f"Mi ballena es: {willy.nombre}")
print(willy.nadar())
print(willy.saltar())
print(willy.alimentarse())
print(willy.descansar())

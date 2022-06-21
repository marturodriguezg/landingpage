animals_lista = ["jirafa", "elefante", "mono"]

animals_tupla = ( "jirafa" , "elefante" , "mono")

animals_conjunto = { "jirafa" , "jirafa" , "elefante" , "mono"}

print(animals_lista)

print(animals_tupla)

print(animals_conjunto)

print("Diccionario de Animales:")

animals_diccionario = { "animal1": "jirafa" , "animal_2" : "elefante" , "animal_3" : "mono" }
for key, value in animals_diccionario.items():
        print(key + ":" , value)




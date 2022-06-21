usuario={"Nombre" : "Mark",
         "Apellido" : "Ronnan",     #Recordá después de cada CLAVE y VALOR va una coma
         "DNI" : "89278823",
         "Rol" : "Asistente",
         "Sucursal" : "005"
}

for key, value in usuario.items():  #Fx que mete el enter es diccionario.items()
    print(key + ":", value)         #por cada key, value
                                    # imprimime la key (dentro del key sumale los ":" ) y impr el valor
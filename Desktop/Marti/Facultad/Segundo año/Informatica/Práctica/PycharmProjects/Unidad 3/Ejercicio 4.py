encuestados = {'anonimo1': '6', 'anonimo2': '9', 'anonimo3': '5', 'anonimo4':
'x', 'anonimo5': 'x', 'anonimo6': '8', 'anonimo7': '3',
'anonimo8': '10', 'anonimo9': '4', 'anonimo10': '5', 'anonimo11':
'x', 'anonimo12': '2', 'anonimo13': '7', 'anonimo14': '5',
'anonimo15': '2', 'anonimo16': '8', 'anonimo17': '10'}

no_contestaron = 0
contestaron = { }

for key, values in encuestados.items():     #Siempre que ponga key, values --> llamar la lista.items()
    if values == "x":
        no_contestaron += 1                 #Si no contestaron, suma en cant a la lista de no contestaron
    else:
        contestaron[key] = values           #Si contestaron, agrega la clave y valor a la lista de contestaron

print("Cantidad de empleados que no contestaron:" , no_contestaron)
print("Lista de las personas que contestaron la encuesta: \n" , contestaron)  #\n es como un break, meter dentro del string

suma_valores = 0
for values in contestaron.values():                         #Si quiero agarrar las dos cosas (k:v) es .items()... si quiero agarrar solo values es .values()
    suma_valores += int(values)                             #Como cada value esta en string, lo convertí en string
print("Numero total de encuestados: " , len(contestaron))   #el len me cuenta cada key y value juntos
print("Suma total de aceptación:", suma_valores)

valor_maximo=10
print("Porcentaje de aceptación:", (suma_valores*100)/(valor_maximo*len(contestaron)))






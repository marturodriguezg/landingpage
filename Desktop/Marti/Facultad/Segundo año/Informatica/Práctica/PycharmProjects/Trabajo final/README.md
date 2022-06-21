Trabajo final - Fundamentos de Informatica:

    El objetivo de este proyecto es idear una API pediátrica donde los padres puedan ingresar 
los datos de sus niños. Hoy en día, cada consulta requiere un resumen inicial de nuestros 
datos básicos y antecedentes. Con nuestra API, sería cuestión de buscar al paciente en la base
de datos para obtener todo su historial. Además podría disponerse de ella para hacer análisis 
del rubro. Podríamos averiguar qué porcentaje de gente tiene determinada enfermedad, obra social,
etc.
    Hay mucha información que se podría ingresar por paciente. Para simplificarlo, trabajaremos 
con los siguientes datos: nombre, apellido, fecha de nacimiento, obra social, código postal, altura,
alergias y su respectivo id. La información recolectada se guardará en la aplicación. En adición, 
instanciamos a los pacientes cómo objetos (POO) para representarlos. Definimos a los pacientes 
cómo clases, asignando los datos mencionados anteriormente cómo atributos. Por otro lado, creamos 
la clase “Obra Social” cómo herencia de la superclase “Pacientes”, la cual cuenta con los siguientes
atributos: nombre, plan y número de la tarjeta. A partir del atributo “Plan” podremos diferenciar a 
los pacientes según las diferentes categorías del plan (mencionar).
    Optamos por desarrollar nuestra API en base a los diferentes pacientes y consumir información 
de la siguiente API de terceros:
“https://cdn.buenosaires.gob.ar/datosabiertos/datasets/salud/hospitales/hospitales.geojson” .
La misma cuenta con datos correspondientes a hospitales del Gran Buenos Aires. De igual modo, no 
utilizaremos todos los campos que nos proporciona la API de terceros, sino que únicamente 
aprovecharemos los siguientes datos: nombre, calle, altura y código postal. Utilizaremos el código 
postal, dato coincidente en ambas APIs, para poder asignarle el hospital más cercano al paciente. 
    A través de la herramienta “Postman” y de 6 diferentes endpoints consultaremos y consumiremos 
información de ambas API, a través de los métodos HTTP (GET, POST, PUT y DELETE). 

    Postman collection con cada uno de los endpoints: 
https://www.getpostman.com/collections/2839577c6c10f50a2441
	Para desarrollar el trabajo, utilizamos la herramienta de Git para poder trabajar de forma 
conjunta.
https://github.com/labourdettecamila/informaticatp

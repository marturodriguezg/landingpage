vehicles = {
    "moto": 10,
    "auto": 20,
    "camioneta" : 25,
    "camion" : 60,
    "camion con acoplado": 90,
    "Emmet Brown" : 200,
}

def print_ticket(category):
    try:
        vehicle_price = vehicles[category]
        print("Imprimiendo...")
        print(f"Vehiculo {category.upper()}: Su tarifa es $ {vehicle_price}")    #la f le dice que dentro del string pueden haber variables
    except KeyError:
        print(f"No se pudo encontrar la categoría {category}")

def user_menu():
    while True:
        print("1- Moto")
        print("2- Auto")
        print("3- Camioneta")
        print("4- Camión")
        print("5- Camión con acoplado")
        print("6- Emmet Brown")

        option = input(">> ")

        if option == "1":
            print_ticket("moto")
        if option == "2":
            print_ticket("auto")
        if option == "3":
            print_ticket("camioneta")
        if option == "4":
            print_ticket("camión")
        if option == "5":
            print_ticket("camión con acoplado")
        if option == "6":
            print_ticket("Emmet Brown")
        else:
            print("Opción inválida")

user_menu()

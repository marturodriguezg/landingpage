accounts=[                                                           #abro una lista con los clientes
        {"user_id":'pablo','password':'supersec123',                 #abro un diccionario del cliente
         'saving_bank':{'account_num':'CA-468-111','amount':100},    #abro otro dic y guardo la caja de ahorro y el monto de la misma
         'current_bank':{'account_num':'CC-358-111','amount':200},   #abro otro dic y guardo la cuenta corriente
         'last_trxs':[45.0,26.5,43.8]                                #abro una lista con los nros de las transacciones del clientes
         },
          {"user_id":'raquel','password':'supersec456',
         'saving_bank':{'account_num':'CA-288-111','amount':500},
         'current_bank':{'account_num':'CC-488-111','amount':400},
         'last_trxs':[50.0,76.5,68.8]
         },
          {"user_id":'irma','password':'supersec789',
         'saving_bank':{'account_num':'CA-888-118','amount':600},
         'current_bank':{'account_num':'CC-888-116','amount':800},
         'last_trxs':[70.0,60.5,51.8]
         },
          {"user_id":'pablo','password':'supersec012',
         'saving_bank':{'account_num':'CA-888-191','amount':700},
         'current_bank':{'account_num':'CC-888-211','amount':600},
         'last_trxs':[20.0,12.5,43.8]
         },
          {"user_id":'pedro','password':'supersec345',
         'saving_bank':{'account_num':'CA-887-111','amount':500},
         'current_bank':{'account_num':'CC-886-111','amount':700},
         'last_trxs':[73.0,28.5,17.8]
         },
          {"user_id":'juan','password':'supersec678',
         'saving_bank':{'account_num':'CA-887-111','amount':800},
         'current_bank':{'account_num':'CC-885-111','amount':200},
         'last_trxs':[19.0,94.5,36.8]
         },
          {"user_id":'alfredo','password':'supersec901',
         'saving_bank':{'account_num':'CA-858-111','amount':900},
         'current_bank':{'account_num':'CC-878-111','amount':900},
         'last_trxs':[48.0,46.5,70.8]
         }
         ]

def login(user, password):
    wrong_account = ""
    account_finded = {}

    for account in accounts:
        if account['user_id'] == user and account['password'] == password:
            print('Sesión iniciada')
            print("Posición de la cuenta:", (accounts.index(account) + 1))
            global posicion
            posicion = accounts.index(account)
            global account_check
            account_check = True
            account_finded = account
            break

        else:
            print("Permiso denegado - Usuario invalido")

    return account_finded
posicion = 0
account_check = False

while True:
    print(" \t*********************************\n    *  Bienvenido al Banco Digital  *  \n \t********************************* \n")

    user = input('Introduzca su nombre de usuario: ')

    password = input('Introduzca su contraseña: ')

    login(user, password)
    if account_check == True:
        print("-----------------------------------\n1) Acreditar en CA\n2) Acreditar en CC\n3) Consultar saldo en CA\n4) Consultar saldo en CC\n5) Consultar TRX\n6) Salir\n-----------------------------------")

        option = input("Elige una opción: ")
        if option == "1":
            new_value = input("Ingrese monto a acreditar a su cuenta de ahorro: ")
            accounts[posicion]["saving_bank"]["amount"] += int(new_value)
            print("¡Listo! el saldo actual es de:", accounts[posicion]["saving_bank"]["amount"])

        elif option == "2":
            new_value = input("Ingrese monto a acreditar a su cuenta corriente: ")
            accounts[posicion]["current_bank"]["amount"] += int(new_value)
            print("¡Listo! el saldo actual es de:", accounts[posicion]["current_bank"]["amount"])

        elif option == "3":
            print("El saldo actual de tu cuenta de ahorro es de:", accounts[posicion]["saving_bank"]["amount"])

        elif option == "4":
            print("El saldo actual de tu cuenta de ahorro es de:", accounts[posicion]["current_bank"]["amount"])

        elif option == "5":
            print("Tus transacciones son las siguientes: ", accounts[posicion]["last_trxs"])

        elif option == "6":
            print("Sesión cerrada")

        else:
            print("Introduzca un valor válido")
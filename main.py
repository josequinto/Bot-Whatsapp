from colorama import Fore, Back, Style, init

import config

from app import app

print(Style.RESET_ALL)
print(Back.GREEN + "\n\t\t-BOT DE SPAM PARA WHATSAPP-")
print(Style.RESET_ALL)

tipo_de_mensaje = input('''
¿Qué deseas enviar?
    1. Primer contacto
    2. Seguimiento
    
Respuesta: ''')

print("Esta es la lista a contactar:\n")

print(config.CLIENTES)

ejecucion = input("\nEsta lista es correcta? (Y/n)\n>> ")

if ejecucion == 'Y':
    
    print(Fore.GREEN  + "\nIniciando ejecución...\n\n")
    print(Style.RESET_ALL)

    #Aqui debe ir Ejecucion()
    app(tipo_de_mensaje)

else:
    print(Fore.RED + "\nCanceled\n\n")
    print(Style.RESET_ALL)

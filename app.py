import webbrowser
import pyautogui as pg

import config
from Mensaje_De_Contacto import Mensaje_De_Contacto
from Mensaje_De_Seguimiento import Mensaje_De_Seguimiento

def app(tipo_de_mensaje):

    for index, cliente in config.CLIENTES.iterrows():

        nombre = cliente.get('Nombre')
        numero = cliente.get('Numero')

        webbrowser.open(f'https://web.whatsapp.com/send?phone=+{numero}')

        pg.sleep(30) #Tiempo de espera mientras abre Whatsapp

        match tipo_de_mensaje:
            case "1":
                Mensaje_De_Contacto()
            case "2":
                Mensaje_De_Seguimiento()

        pg.sleep(5)
        
        pg.hotkey('ctrl', 'w')
import pandas as pd


# Agrega '/export?format=csv' al final de la url de la hoja de Sheets
RUTA_DE_CONTACTOS = 'https://docs.google.com/spreadsheets/d/1KBwQogXCNuEoeyZfGMNzQdaEf8HYX3OSEc5TSkd0aHo/export?format=csv'


CLIENTES = pd.read_csv(RUTA_DE_CONTACTOS)



MENSAJE_SEGUIMIENTO = """
Hola  🙏 espero te encuentres muy bien  🥳 🙏

Mira  👀 ultimo apartamento disponible para entrega inmediata  🏬 🚀

Solo $125 millones, cuotas desde solo $380 mil pesos mensuales!

Lo quieres aprovechar?  escribeme y te ayudo a lograrlo 💪🙏
"""

#Mensajes del primer contacto

MENSAJE_1 = """
Hola 👋🏼, buenos días! Espero te encuentres muy bien 🙏🏼🥳

Gracias por tu interés en nuestro proyecto AUREAL Apartamentos

Soy Diego Osorio asesor de la constructora Skema y con mucho gusto te ayudaré con la compra de tu apartamento 🙏🏼🤩
"""

MENSAJE_2 = """
El proyecto incluye: 

🔅 Conjunto cerrado
🔅 Piscina para niños y adultos 
🔅 Cancha múltiple 
🔅 Kiosko de reuniones
🔅 Salón para Teletrabajo
🔅 Sendero recreativo
🔅 Estaciones para ejercicios
🔅 Zonas verdes 
🔅 Zona para mascotas
🔅 Parque infantil
🔅 Estacionamientos
🔅 Vigilancia privada 24 horas
"""

MENSAJE_3 = """
Mira, este apartamento 👆🏼 lo tenemos disponible con cuota inicial desde solo $400 mil pesos mensual y podrás aplicar hasta por 65 millones de subsidio de vivienda! 

¡Yo te ayudo para que el banco te apruebe tu crédito y tu subsidio de vivienda! 🤩🏬
"""

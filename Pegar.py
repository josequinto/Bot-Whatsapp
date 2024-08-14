from PIL import Image
import pyautogui as pg
import win32clipboard
import pyperclip
import io


def Imagen(img):
    image = Image.open(f'./imagenes/{img}.jpeg')

    # Convierte la imagen en formato BMP a un buffer
    output = io.BytesIO()
    image.convert('RGB').save(output, 'BMP')
    data = output.getvalue()[14:]  # Omite el encabezado BMP
    output.close()

    # Copia la imagen al portapapeles
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

    pg.sleep(2)
    pg.hotkey('ctrl', 'v')
    pg.sleep(2)
    pg.press('enter')

def Mensaje(msg):
    pg.sleep(2)
    pyperclip.copy(msg)
    pg.hotkey('ctrl', 'v')
    pg.sleep(2)
    pg.press('enter')
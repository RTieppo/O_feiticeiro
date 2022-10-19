from PySimpleGUI import PySimpleGUI as sg
import pyglet
from pyglet.libs.win32 import constants

constants.COINIT_MULTITHREADED = 0x2

pyglet.font.add_file(r'.\font\PixelOperator8-Bold.ttf')
pyglet.font.add_file(r'.\font\PixelOperatorSC-Bold.ttf')

font1 = ('Pixel Operator 8', 30)
font2 = ('Pixel Operator SC', 15)
font3 = ('Pixel Operator SC', 25)
font4 = ('Pixel Operator 8', 40)
font5 = ('Pixel Operator SC', 20)
font6 = ('Pixel Operator SC', 40)

def tela_343():
    sg.theme('DarkAmber')
    
    layout=[
        [sg.Text('343\n', justification='c',font=font1, size=(550,0))],

        [sg.Text(open('ark_txt\Telas\Tela_343.txt', 'r',encoding='utf-8').read(), font=font5)],

        [sg.Text('')], #ajuste de espaço

        [sg.Text(open('ark_txt\Telas\Tela_343_1.txt', 'r',encoding='utf-8').read(), font=font5, text_color='red')],

        [sg.Text('')], #ajuste de espaço

        [sg.Button('Subir', font=font2),sg.Button('Menu', font=font2)]
    ]
    return sg.Window('',size=(550,850),border_depth=(-15),layout=layout, finalize=True, element_justification='c',
    icon='Icon\Sabio.ico', location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))
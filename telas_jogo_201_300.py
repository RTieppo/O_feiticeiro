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

def tela_278_156():
    sg.theme('DarkAmber')

    layout=[
        [sg.Text('278 - 156', justification='c',font=font1, size=(550,0))],

        [sg.Text('\n   A passagem logo termina em uma porta de'
        '\nmadeira trancada. Você cola o ouvido na'
        '\nporta. Mas não ouve nada. Você vai tentar'
        '\nderrubá-la? ou vai dar meia volta?'
        '\n',font=font5)],

        [sg.Image('img\porta1.png')],
        
        [sg.Text('', key='Info0', font=font2)],

        [sg.Text('', key='info2', font=font2, text_color='green'),
        sg.Text('', key='Info1', font=font2, text_color='red')],

        [sg.Button('Derrubar', font=font2),sg.Button('Menu', font=font2),
        sg.Button('Retornar', font=font2)],
    ]
    return sg.Window('',size=(550,850),border_depth=(-15),layout=layout, finalize=True, element_justification='c',
    icon='Icon\Sabio.ico', location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))
    
def tela_248():
    sg.theme('DarkAmber')

    layout=[
        [sg.Text('248\n', justification='c',font=font1, size=(550,0))],

        [sg.Text(open(r'.\ark_txt\Telas\Tela_248.txt', 'r',encoding='utf-8').read().strip(), font=font5)],

        [sg.Text('ORC NV1', font=font5, justification='c', text_color='green')],

        [sg.Text('HABILIDADE - 6', font=font5, justification='c')],

        [sg.Text(open(r'.\ark_txt\user\Nome.txt', 'r', encoding='utf-8').read(), font=font5),
        sg.Text('', key='-dano_jogador-', font=font5, text_color='red'),
        sg.Text('VS', font=font5),
        sg.Text('', key='-dano_mostro-', font=font5, text_color='red'),
        sg.Text('Orc', font=font5)],

        [sg.Text('', key='causa', font=font2, text_color='green')],
        
        [sg.Text('', key='Sofre', font=font2, text_color='red')],

        [sg.Text('', key='Empate', font=font2, text_color='yellow')],

        [sg.Button('Atacar', font=('Pixel Operator SC',15)),sg.Button('Menu', font=font2, size=(6,0))],
        [sg.Text('',key='-botao_sorte-')],
    ]
    return sg.Window('',size=(550,850),border_depth=(-15),layout=layout, finalize=True, element_justification='c',
    icon='Icon\Sabio.ico', location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))
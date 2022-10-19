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

def tela_000():
    sg.theme('DarkAmber')

    layout=[
        [sg.Text('Índices',font=font6, justification='c', size=(550,0))],

        [sg.Text('  Muito bem aventureiro vamos definir os seus índices'
        '\npara começar essa jornada é só clicar nos botões abaixo'
        '\nque as suas habilidades vão ser geradas aleatoriamente.'
        '\n', font=font2)],

        [sg.Button('HABILIDADE',font=font2)],

        [sg.Text('6  +',font=font2), sg.Text('', key='H',font=font2),
        sg.Text('', key='S_H',font=font2, text_color ='green')],

        [sg.Button('ENERGIA',font=font2,)],

        [sg.Text('12  +',font=font2), sg.Text('', key='E',font=font2),
        sg.Text('', key='S_E',font=font2, text_color ='green')],

        [sg.Button('SORTE',font=font2)],

        [sg.Text('6  +',font=font2), sg.Text('', key='S',font=font2),
        sg.Text('', key='S_S',font=font2, text_color ='green')],

        [sg.Text('', key='aviso_indices', font=font2, text_color='red')],

        [sg.Text('Poção',font=font6, justification='c', size=(550,0))],

        [sg.Text('  Escolha uma poção para levar com você, escolha'
        '\ncom sabedoria pois você terá dois frascos da poção'
        '\nescolhida.'
        '\n',font=font2)],

        [sg.Button('Força',key='P2',font=font2), sg.Button('Habilidade', key='P1',font=font2),
        sg.Button('Fortuna', key='P3',font=font2)],

        [sg.Text('', key='C_P', font=font2, text_color='green'),
        sg.Text('',key='aviso_pocao', font=font2, text_color='red')],

        [sg.Image('img\Tesouro.png')],

        [sg.Text('', key='aviso_validador', font=font5, text_color='red')],

        [sg.Button('Estou pronto',font=font2, size=(20,0))],

        [sg.Button('Voltar',font=font2), sg.Button('Resetar',font=font2)]
        
        ]
    return sg.Window('',size=(550,850),border_depth=(-15),layout=layout, finalize=True, element_justification='c',
    icon='Icon\Sabio.ico', location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))

def tela_001():
    sg.theme('DarkAmber')
    
    layout=[
        [sg.Text('001', size=(550,0), justification='c', font=font1)],

        [sg.Text(open('ark_txt\Telas\Tela_001.txt', 'r', encoding='utf-8').read(),font=font2)],

        [sg.Button('Oeste', font=font2),sg.Button('Menu', font=font2),

        sg.Button('Leste', font=font2)],

    ]
    return sg.Window('',size=(550,850),border_depth=(-15),layout=layout, finalize=True, element_justification='c',
    icon='Icon\Sabio.ico', location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))

#foi só criada / falta implementar
def tela_002():
    sg.theme('DarkAmber')
    
    layout=[
        [sg.Text('002', size=(550,0), justification='c', font=font1)],
        [sg.Text('',font=font2)],
        [sg.Button('Oeste', font=font2),sg.Button('Menu', font=font2),
        sg.Button('Leste', font=font2)],
    ]
    return sg.Window('',size=(550,850),border_depth=(-15),layout=layout, finalize=True, element_justification='c',
    icon='Icon\Sabio.ico', location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))

def tela_71():
    sg.theme('DarkAmber')

    layout=[
        [sg.Text('71\n', justification='c',font=font1, size=(550,0))],

        [sg.Text(open('ark_txt\Telas\Tela_71.txt', 'r',encoding='utf-8').read(), font=font5)],

        [sg.Text('', key='S1', font=font2, text_color='green')],

        [sg.Text('', key='S2', font=font2, text_color='red')],

        [sg.Text('', key='S3', font=font2, text_color='red')],

        [sg.Button('Testar', font=font2),sg.Button('Menu', font=font2)],

    ]
    return sg.Window('',size=(550,850),border_depth=(-15),layout=layout, finalize=True, element_justification='c',
    icon='Icon\Sabio.ico', location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))

def tela_92_71():
    sg.theme('DarkAmber')

    layout=[
        [sg.Text('92 - 71\n', justification='c',font=font1, size=(550,0))],

        [sg.Text(open('ark_txt\Telas\Tela_92_71.txt', 'r',encoding='utf-8').read(), font=font5)],

        [sg.Text('', key='S1', font=font2, text_color='green')],

        [sg.Text('', key='S2', font=font2, text_color='red', justification='c')],

        [sg.Text('', key='S3', font=font2, text_color='red')],

        [sg.Button('Testar', font=font2),sg.Button('Menu', font=font2)]
    ]
    return sg.Window('',size=(550,850),border_depth=(-15),layout=layout, finalize=True, element_justification='c',
    icon='Icon\Sabio.ico', location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))
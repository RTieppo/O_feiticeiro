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

def tela_menu(energia, habilidade, sorte, provisoes, energia_v, habilidade_v, sorte_v, poção_base, numero_poção):
    sg.theme('DarkAmber')

    layout=[
        [sg.Text('Menu', size=(550,0), justification='c', font=font1)],

        [sg.Text('=-='*30, font=font2)],

        [sg.Text('Indices', size=(550,0), justification='c', font=font3)],

        [sg.Text(f'HABILIDADE: {habilidade} / {habilidade_v}',font=font2)],

        [sg.Text(f'ENERGIA: {energia} / {energia_v}',font=font2)],

        [sg.Text(f'SORTE: {sorte} / {sorte_v}',font=font2)],

        [sg.Text(f'{poção_base} {numero_poção}',font=font2)],

        [sg.Text(f'Provisôes:{provisoes}',font=font2)],

        [sg.Text('=-='*30, font=font2)],

        [sg.Text('Mochila', size=(550,0), justification='c', font=font3)],

        [sg.Text('=-='*30, font=font2)],

        [sg.Text('',key='-aviso_saida-', text_color='red', font=font2)],

        [sg.Button('Mapa',font=font2), sg.Button('Voltar',font=font2), sg.Button('Sair', font=font2)],
    ]
    return sg.Window('',size=(550,850),border_depth=(-15),layout=layout, finalize=True, element_justification='c',
    icon='Icon\Sabio.ico', location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))

def tela_mapa():
    sg.theme('DarkAmber')

    layout=[
        [sg.Text('Mapa', size=(550,0), justification='c', font=font1)],

        [sg.Text('=-='*30, font=font2)],

        [sg.Text(open(r'C:\Users\Public\O feiticeiro\Mapa.txt', 'r', encoding='utf-8').read(), font=font2)],

        [sg.Text('=-='*30, font=('Pixel Operator SC',15))],

        [sg.Text(' ', key= 'info', font=font2)],

        [sg.Button('Menu', font=('Pixel Operator sc',15)), sg.Button('Salvar',font=font2), sg.Button('Sair', font=font2)],

    ]
    return sg.Window('',size=(550,850),border_depth=(-15),layout=layout, finalize=True, element_justification='c',
    icon='Icon\Sabio.ico', location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))

def tela_morte():
    sg.theme('Black')

    layout=[
        [sg.VPush(), sg.Text('Você\nMorreu', font=font4, justification='c', text_color='red')],
        [sg.Text('', key='-aviso_save-', text_color='red', font=font5)],
        [sg.Button('Salvar\nMapa',key = '-Salva-', font=font2, size=(6,2)), sg.Button('Tela\nInicial', key= '-Inicio-', font=font2, size=(7,2)), sg.Button('Sair', font=font2, size=(6,2), )],
    ]
    return sg.Window('',size=(550,850),border_depth=(-15),layout=layout, finalize=True, element_justification='c',
    icon='Icon\Sabio.ico', location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))

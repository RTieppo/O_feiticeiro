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
font6 = ('Pixel Operator 8', 20)

def tela_nome():
    sg.theme('DarkAmber')
    

    layout = [
        [sg.Text('\nEscolha o nome\ndo seu Guerreiro\n', justification='c', font=font6)],

        [sg.Image(r'img\Guerreiro.png')],

        [sg.Text('')], #ajusta espaço

        [sg.Input(size=(50,20), key='usernome')],

        [sg.Text('',key='aviso1', font=font2, text_color='green'), sg.Text('', key='aviso2', font=font2, text_color='red')],

        [sg.Button('Validar', font=font2, size=(7,0)), sg.Button('Voltar', font=font2, size=(7,0))],

        [sg.Text('', key='valido')]

    ]
    return sg.Window('', size=(550,850), border_depth=(-15), layout=layout, finalize=True, element_justification='c',
    icon='Icon\Sabio.ico', location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))

def tela_dicas():
    sg.theme('DarkAmber')

    layout=[
        [sg.Text('DICAS PARA O JOGO',font=font3, justification='c')],

        [sg.Text(open('ark_txt\Telas\Tela_dicas.txt', 'r', encoding='utf-8').read(), font=font2)],

        [sg.Text('Que a sorte dos deuses o'
        '\nacompanhe nessa aventura!',font=font5, justification='c')],

        [sg.Text('')], #ajuste de espaço

        [sg.Button('Boatos',font=font2),sg.Button('Voltar',font=font2)]
    ]
    return sg.Window('',size=(550,850),border_depth=(-15),layout=layout, finalize=True, element_justification='c',
    icon='Icon\Sabio.ico', location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))

def tela_boatos1():
    sg.theme('DarkAmber')

    layout=[
        [sg.Text('BOATOS', size=(550,0), justification='c', font=font1)],

        [sg.Text(open('ark_txt\Telas\Tela_boatos1.txt', 'r', encoding='utf-8').read(), font=font2)],

        [sg.Text('')], #ajuste de espaço

        [sg.Button('Próximo', font=font2), sg.Button('Voltar', font=font2)]
    ]
    return sg.Window('',size=(550,850),border_depth=(-15),layout=layout, finalize=True, element_justification='c',
    icon='Icon\Sabio.ico', location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))

def tela_boatos2():
    sg.theme('DarkAmber')

    layout=[
       [sg.Text('BOATOS', size=(550,0), justification='c', font=font1)],

       [sg.Text(open('ark_txt\Telas\Tela_boatos2.txt', 'r', encoding='utf-8').read(), font=font2)],

       [sg.Image('img\Espada.png')],

       [sg.Text('')], #ajuste de espaço
       
       [sg.Button('Começar', font=font2), sg.Button('Anterior', font=font2)]
    ]
    return sg.Window('',size=(550,850),border_depth=(-15),layout=layout, finalize=True, element_justification='c',
    icon='Icon\Sabio.ico', location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))
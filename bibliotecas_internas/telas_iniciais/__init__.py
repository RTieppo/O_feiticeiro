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

#eComeça sempre no centro se voltar para elas também vai para o centro

def tela_abertura():
    sg.theme('DarkAmber')

    layout=[
        [sg.Text('\n\n\n\n\n\n', font=font4)], #ajuste de alinhamento
        [sg.Text('RTieppo', key='-imprime-', font=font1, justification='c')],
        [sg.Text('', key='-nome_2-', font=font3, justification='c')]
    ]
    return sg.Window('',size=(550,850),border_depth=(-15),layout=layout, finalize=True,element_justification='c', no_titlebar=  True)

def tela_intro():
    sg.theme('DarkAmber')

    layout=[
        [sg.Text('O Feiticeiro', font=font1)],

        [sg.Text('DA MONTANHA DE FOGO', size=(550,0), font=font3, justification='c')],

        [sg.Text(open('ark_txt\Telas\Tela_intro.txt', 'r', encoding='utf-8').read(), font=font2)],

        [sg.Image('img\Dragão.png')],

        [sg.Image('')],

        [sg.Button('Jogar', size=(8,0), font=font2), sg.Button('Regras', size=(8,0) ,font=font2),

        sg.Button('Biblioteca', size=(10,0) ,font=font2),

        sg.Button('Créditos', size=(8,0) ,font=font2), sg.Button('Sugestões', size=(10,0) ,font=font2)],

        [sg.Button('Sair', size=(15,0) ,font=font2)]
        ]
    
    return sg.Window('',size=(550,850),border_depth=(-15),layout=layout, finalize=True, element_justification='c', icon='Icon\Sabio.ico')

def tela_regras():
    sg.theme('DarkAmber')

    layout=[
        [sg.Text('REGRAS', font=font1, size=(550,0), justification='c')],

        [sg.Text('Então você quer entende como funciona o jogo?'
        '\nMuito bem o que você quer entender:', font=font2, justification = 'c' )],

        [sg.Button('Indices', font=font2, size=(10,0)), sg.Button('Batalha', font=font2, size=(10,0)),

        sg.Button('Fuga', font=font2, size=(10,0)), sg.Button('Sorte', font=font2, size=(10,0))],

        [sg.Button('Inventário', font=font2, size=(10,0)), sg.Button('Poções', font=font2, size=(10,0)),

        sg.Button('Provisões', font=font2, size=(10,0))],

        [sg.Image('img\Livro.png')],

        [sg.Text(' ', key = 'info', font=font2)],

        [sg.VPush(), sg.Button('Inicio', font=font2, size=(10,0))]
        
    ]
    return sg.Window('',size=(550,850),border_depth=(-15),layout=layout, finalize=True, element_justification='c',
    icon='Icon\Sabio.ico')

def tela_sugestao():
    sg.theme('DarkAmber')

    layout=[
        [sg.Text('SUGESTÃO', size=(550,0), justification='c',font=font4)],

        [sg.Text('  Olá jogador, aqui você pode deixar a sua avaliação ou'
        '\nsugestão para melhorarmos ainda mais,sua experiência'
        '\ncom o jogo.'
        '\n'
        '\nBasta escrever abaixo a sua sugestão ou avaliação'
        '\ne clicar em enviar.', font=font2)],

        [sg.Input(size=(80,20),key='usertexto')],

        [sg.Button('Enviar', font=font2), sg.Button('Voltar',size=(10,0), font=font2)],

        [sg.Text('', key='mensagem', font=font2, justification='c')],

        [sg.Image(r'img\Sugestão.png')]
        ]

    return sg.Window('',size=(550,850),border_depth=(-15), layout=layout, finalize=True, element_justification='c', icon='Icon\Sabio.ico')
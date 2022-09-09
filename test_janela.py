
#Bibliotecas Extras
import pyglet
from pyglet.libs.win32 import constants
import random
import smtplib
from email.message import EmailMessage
from PySimpleGUI import PySimpleGUI as sg
import time
import os

#funções complementares
import telas_iniciais
import telas_de_introdução
import telas_jogo_0_100
import telas_jogo_101_200
import telas_jogo_201_300
import telas_jogo_301_400
import dados
import gerador_de_arquivos_txt
import telas_recorentes
import gerador_de_mostro
import aplicador_de_dano
import alterador_de_indices
import efeitos_sonoros

#gravação de fonte fora do sistema

constants.COINIT_MULTITHREADED = 0x2

pyglet.font.add_file(r'.\font\PixelOperator8-Bold.ttf')
pyglet.font.add_file(r'.\font\PixelOperatorSC-Bold.ttf')

font1 = ('Pixel Operator 8', 30)
font2 = ('Pixel Operator SC', 15)
font3 = ('Pixel Operator SC', 25)
font4 = ('Pixel Operator 8', 40)
font5 = ('Pixel Operator SC', 20)
font6 = ('Pixel Operator SC', 40)

#aplicada criar 92_71

def tela_abertura():
    sg.theme('DarkAmber')

    layout=[
        [sg.Text('\n\n\n\n\n\n', font=font6)], #ajuste de alinhamento
        [sg.Text('RTieppo', key='-imprime-', font=font1, justification='c')],
        [sg.Text('', key='-nome_2-', font=font3, justification='c')]
    ]
    return sg.Window('',size=(550,850),border_depth=(-15),layout=layout, finalize=True,element_justification='c', no_titlebar=  True)


janela_abertura = tela_abertura()

abertura = 0

while True:
    #ações para o teste da tela
    Window,eventos,valores = sg.read_all_windows(timeout=1000)

    #ação da tela no loop

    if janela_abertura and eventos == sg.TIMEOUT_EVENT:
        while abertura < 5:

            if abertura <2:
                janela_abertura['-imprime-'].update('Aprsenta')
                janela_abertura.refresh()
                time.sleep(1)
                abertura += 1

            elif abertura <= 3:
                janela_abertura['-imprime-'].update('O Feiticeiro')
                janela_abertura.refresh()
                time.sleep(1)
                abertura += 1
            
            elif abertura <= 4:
                janela_abertura['-nome_2-'].update('DA MONTANHA DE FOGO')
                janela_abertura.refresh()
                time.sleep(1)
                abertura += 1
            
            elif abertura == 5:
                break
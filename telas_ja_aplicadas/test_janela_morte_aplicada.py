#Bibliotecas Extras
from turtle import position
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

def tela_morte():
    sg.theme('Black')

    layout=[
        [sg.VPush(), sg.Text('Você\nMorreu', font=font4, justification='c', text_color='red')],
        [sg.Text('', key='-aviso_save-', text_color='red', font=font5)],
        [sg.Button('Salvar\nMapa',key = '-Salva-', font=font2, size=(6,2)), sg.Button('Tela\nInicial', key= '-Inicio-', font=font2, size=(7,2)), sg.Button('Sair', font=font2, size=(6,2), )],
    ]
    return sg.Window('',size=(550,850),border_depth=(-15),layout=layout, finalize=True, element_justification='c',
    icon='Icon\Sabio.ico', location=tuple(sg.user_settings_get_entry('-last position-', (None, None))))


janela_morte = tela_morte()


while True:
    #ações para o teste da tela
    Window,eventos,valores = sg.read_all_windows()

    #ação da tela no loop

    if Window == janela_morte and eventos == sg.WIN_CLOSED or Window == janela_morte and eventos =='Sair':
        break

    elif Window == janela_morte and eventos =='-Inicio-':
        pass
    

    elif Window == janela_morte and eventos == '-Salva-':
        while True:
            #indentifica user

            sistema = os.environ
            user = sistema['USERNAME']
            
            #Unifica user com caminho e gera lista
            caminho1 = os.path.join(r'C:\Users',user,r'Documents')
            validador = os.listdir(caminho1)

            #caminho para criar a pasta 
            caminho2 = os.path.join(caminho1,r'Save User')

            #unifica caminho final e grava txt
            caminho3 = os.path.join(caminho2,r'Mapa.txt')

            if 'Save User' in validador:
                save = open(r'.\ark_txt\map\Mapa.txt', 'r', encoding='utf-8').read()
                criar_arquivo = open(caminho3, 'w', encoding='utf-8')
                criar_arquivo.write(save)
                criar_arquivo.close()
                Window['-aviso_save-'].update('Salvo em Documentos')
                break

            else:
                os.makedirs(caminho2)
    
    
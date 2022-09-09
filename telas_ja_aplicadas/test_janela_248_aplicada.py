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


janela_248, janela_menu  = tela_248(), None

volta = None

#Limita criação do notão sorte
limita_botao_sorte = 0

#variaveis de combate e ativação do botão sorte
ativação_botão_sorte = 0
resultado_batalha = ' '


while True:
    #ações para o teste da tela
    Window,eventos,valores = sg.read_all_windows()

    if Window == janela_menu and eventos == sg.WIN_CLOSED:
        break

    elif Window == janela_menu and eventos == 'Voltar':
        sg.user_settings_set_entry('-last position-', janela_menu.current_location())
        volta = volta.un_hide()
        janela_menu.close()

    elif Window == janela_menu and eventos == 'Mapa':
        sg.user_settings_set_entry('-last position-', janela_menu.current_location())
        janela_mapa = telas_recorentes.tela_mapa()
        janela_menu.close()


    #ação da tela no loop

    if Window == janela_248 and eventos == sg.WIN_CLOSED:
        break
    
    elif Window == janela_248 and eventos == 'Menu':
        sg.user_settings_set_entry('-last position-', janela_248.current_location())
        janela_menu = telas_recorentes.tela_menu()
        janela_248.hide()
        volta = janela_248
    
    elif Window == janela_248 and eventos == 'Atacar':
        #limpa informações da tela
        Window['causa'] .update('')
        Window['Empate'] .update('')
        Window['Sofre'] .update('')
        Window['-dano_mostro-'] .update('')
        Window['-dano_jogador-'] .update('')

        #abre vida jogador para validação
        valida_energia_jogador = int(open(r'.\ark_txt\ind\ENER_V.txt','r', encoding='utf-8').read())

         #abre vida da criatura
        abre_vida_criatura = int(open(r'.\ark_txt\Batalha\orca.txt', 'r', encoding='utf-8').read())
        
        #valida vida jogador
        if valida_energia_jogador > 0:

            #valida vida do mostro
            if abre_vida_criatura > 0:

                #Abre aquivo para a validação da sorte e criação do botão
                valida_sorte = int(open(r'.\ark_txt\ind\Sort_V.txt', 'r',encoding='utf-8').read())
                
                if valida_sorte > limita_botao_sorte:
                    #adicona botão sorte e trava a criação de novos botoes 
                    janela_248.extend_layout(janela_248['-botao_sorte-'],
                    [[sg.Button('Sorte',font=font2)]])
                    limita_botao_sorte += 30
                
                #reseta ativação do botão sorte
                ativação_botão_sorte = 0
                
                #Gera a força do jogador e do mostro
                força_user01 = int(random.randint(1,6))
                força_user02 = int(random.randint(1,6))

                força_mostro01 = int(random.randint(1,6))
                força_mostro02 = int(random.randint(1,6))

                #abre habilidade variavel 
                Habilidade_variavel = int(open(r'.\ark_txt\ind\HAB_V.txt','r', encoding='utf-8').read())

                #soma força final
                soma_força_user = força_user01 + força_user02 + Habilidade_variavel
                soma_força_mostro = força_mostro01 + força_mostro02 + 6

                if soma_força_user > soma_força_mostro:

                    Window['causa'] .update('Dano Causado')
                    #Mostra as informações da batalha para o jogador 
                    Window['-dano_mostro-'] .update(soma_força_mostro)
                    Window['-dano_jogador-'] .update(soma_força_user)

                    #grava resultado de combate para aplicar na sorte
                    resultado_batalha = 'Dano_causado'
                    
                    #Atualiza vida da criatura e aplica dano normal
                    aplicador_de_dano.dano_aumentado_normal()
                    
                elif soma_força_user < soma_força_mostro:

                    Window['Sofre'] .update('Dano Sofrido')
                    #Mostra as informações da batalha para o jogador 
                    Window['-dano_mostro-'] .update(soma_força_mostro)
                    Window['-dano_jogador-'] .update(soma_força_user)

                    #grava resultado de combate para aplicar na sorte
                    resultado_batalha = 'Dano_sofrido'

                    #atualiza vida do jogador
                    aplicador_de_dano.dano_normal_recebido()
                    

                else:
                    Window['Empate'] .update('Esquiva')
                    #aplica informações na tela
                    Window['-dano_mostro-'] .update(soma_força_mostro)
                    Window['-dano_jogador-'] .update(soma_força_user)

            else:
                        #informa jogador a morte de mostro
                        Window['causa'] .update('Criatura foi morta')
                        #adicionar os seguintes reset
                        #resultado batalha
                        #limitador de botão sorte
                        #ativação do botão sorte
                        #criar ação depois da morte da criatura

        else:
                    #informa jogador a morte de mostro
                    Window['Sofre'] .update('Você foi morto')

                    #criar ação depois da morte do jogador
    
    #ajustar uso da sorte e apresentação das informações para o jogador
    elif Window == janela_248 and eventos == 'Sorte':
        #limpa informação da tela
        Window['causa'] .update('')
        Window['Sofre'] .update('')
        Window['Empate'] .update('')
        Window['-dano_mostro-'] .update('')
        Window['-dano_jogador-'] .update('')

        #faz nova leitura dos arquivos para aplicar a sorte
        vida_jogador = int(open(r'.\ark_txt\ind\ENER_V.txt', 'r', encoding='utf-8').read())
        vida_criatura = int(open(r'.\ark_txt\Batalha\orca.txt', 'r', encoding='utf-8').read())
        alterador_de_sorte_e_validador = int(open(r'.\ark_txt\ind\Sort_V.txt','r', encoding='utf-8').read())
       
        #validação se o botão sorte já foi usado
        if ativação_botão_sorte <= 0:

            #validação se jogador ainda tem sorte
            if alterador_de_sorte_e_validador > 0:

                #gerador de comparação de sorte
                teste_sorte1 = int(random.randint(1,6))
                teste_sorte2 = int(random.randint(1,6))

                # ajusta sorte assim que usada
                alterador_de_indices.menos_sorte()
    
                if resultado_batalha == 'Dano_causado':

                    if alterador_de_sorte_e_validador > teste_sorte1 + teste_sorte2:
                        #sorte ajudou jogador 
                        Window['causa'] .update('Dano ampliado')
                        ativação_botão_sorte += 1
                        #aplica dano aumentado
                        aplicador_de_dano.dano_aumentado_normal()
                        
                    
                    else:
                        #sorte não ajudou na batalha
                        Window['Empate'] .update('Dano reduzido')
                        ativação_botão_sorte += 1
                        #Reduz dano normal
                        aplicador_de_dano.dano_reduzido()
                        

                elif resultado_batalha == 'Dano_sofrido':
                    #jogador teve sorte e dano foi reduzido
                    if alterador_de_sorte_e_validador  > teste_sorte1 + teste_sorte2:
                        Window['causa'] .update('Sangramento contido')
                        ativação_botão_sorte += 1
                        aplicador_de_dano.conteve_sangramento()
                        
                    #jogador não teve sorte dano foi aumentado
                    else:
                        Window['Sofre'] .update('Sangramento aumentado')
                        ativação_botão_sorte += 1
                        aplicador_de_dano.sangramento_aumentado()
                        

                else:
                    Window['Empate'] .update('sorte não aplicavel')

            else:
                Window['Sofre'] .update('Sorte Esgotada')
                
        else:
            Window['Empate'] .update('sorte já usada')
            
            #criar informação jogador na tela
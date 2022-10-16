#Bibliotecas Extras
from pickle import FALSE
import pyglet
from pyglet.libs.win32 import constants
import random
import smtplib
from email.message import EmailMessage
from PySimpleGUI import PySimpleGUI as sg
import time

#Bibliotecas internas
from biblioteca_de_telas import telas_iniciais
from biblioteca_de_telas import telas_de_introdução
from biblioteca_de_telas import telas_jogo_0_100
from biblioteca_de_telas import telas_jogo_101_200
from biblioteca_de_telas import telas_jogo_201_300
from biblioteca_de_telas import telas_jogo_301_400
from biblioteca_de_telas import telas_recorentes
from biblioteca_de_geradores import gerador_mapa
from biblioteca_de_geradores import gerador_txt_user
from biblioteca_de_geradores import gerador_de_dados
from biblioteca_manipuladores import txt

from biblioteca_combate import combate_gerais
from biblioteca_combate import sorte_combate

import dados

import aplicador_de_dano
import alterador_de_indices


#puxafonte fora do sistema
constants.COINIT_MULTITHREADED = 0x2

pyglet.font.add_file(r'.\font\PixelOperator8-Bold.ttf')
pyglet.font.add_file(r'.\font\PixelOperatorSC-Bold.ttf')

font1 = ('Pixel Operator 8', 30)
font2 = ('Pixel Operator SC', 15)
font3 = ('Pixel Operator SC', 25)
font4 = ('Pixel Operator 8', 40)
font5 = ('Pixel Operator SC', 20)
font6 = ('Pixel Operator 8', 20)

#Atribuição de janelas
#janelas iniciais

#janelas recorentes
janela_menu = janela_mapa = janela_morte = None

#grava janela antes de acessar o menu
volta = None

#limitador de criação de botão
limita_botão_nome = limita_botao_sorte = 0

#ativação de botão
ativação_botão_sorte = False

#indices base do jogador
energia = habilidade = sorte = provisoes = 10

#indices variaveis do jogador
energia_v = habilidade_v = sorte_v = 5

#poção jogador
poção_base = ' '
numero_poção = 5

#indeces mostrons
mostro_1_V  = 5
mostro_1_H = 5

#nome global
nome_jogador = 'eu'

#confirmado de saida para tela inicial
confirma_saida = 0


janela_248 = telas_jogo_201_300.tela_248(nome_jogador, mostro_1_H)

#O loop foi criado de acordo com o surgimento das telas
#Assim não vão respeitar uma ordem numerica, mapa principal sendo criado
 
while True:

    Windows,eventos,valores = sg.read_all_windows()

    if Windows == janela_menu and eventos == sg.WIN_CLOSED:
        break

    elif Windows == janela_menu and eventos == 'Voltar':
        sg.user_settings_set_entry('-last position-', janela_menu.current_location())
        volta = volta.un_hide()
        janela_menu.close()

    elif Windows == janela_menu and eventos == 'Mapa':
        sg.user_settings_set_entry('-last position-', janela_menu.current_location())
        janela_mapa = telas_recorentes.tela_mapa()
        janela_menu.close()
    
    elif Windows == janela_menu and eventos == 'Sair':
        #confirma se jogador realmente vai querer sair
        if confirma_saida == 0:
            Windows['-aviso_saida-'] .update('Tem certeza que deseja sair?')
            confirma_saida += 1
        #encerra as janelas e zera o contador de saida
        else:
            janela_intro = telas_iniciais.tela_intro()
            confirma_saida = 0
            energia = habilidade = sorte = provisoes = 0
            energia_v = habilidade_v = sorte_v = 0
            numero_poção = 0
            poção_base = ' '
            janela_menu.close()
            volta.close()
#janela Mapa

    if Windows == janela_248 and eventos == sg.WIN_CLOSED:
        break
    
    elif Windows == janela_248 and eventos == 'Menu':
        sg.user_settings_set_entry('-last position-', janela_248.current_location())
        janela_menu = telas_recorentes.tela_menu(energia, habilidade, sorte, provisoes, energia_v, habilidade_v, sorte_v, poção_base, numero_poção)
        janela_248.hide()
        volta = janela_248
    
    elif Windows == janela_248 and eventos == 'Atacar':
        #limpa informações da tela
        Windows['causa'] .update('')
        Windows['Empate'] .update('')
        Windows['Sofre'] .update('')
        Windows['-dano_mostro-'] .update('')
        Windows['-dano_jogador-'] .update('')
        ativação_botão_sorte = False

        atk = combate_gerais.combateX1(energia_v,mostro_1_V,habilidade_v,mostro_1_H)

        if  limita_botao_sorte == 0:
            #adicona botão sorte e trava a criação de novos botoes 
            janela_248.extend_layout(janela_248['-botao_sorte-'],
            [[sg.Button('Sorte',font=font2)]])
            limita_botao_sorte += 1
            #reseta ativação do botão sorte
            ativação_botão_sorte = False
        
        if atk[0] == 'Dano causado':
            Windows['causa'] .update(atk[0])
            #Mostra as informações da batalha para o jogador 
            Windows['-dano_mostro-'] .update(atk[1])
            Windows['-dano_jogador-'] .update(atk[2])
            
            #Atualiza vida da criatura e aplica dano normal
            mostro_1_V -= 2
        
        elif atk[0] == 'Dano Sofrido':
            Windows['Sofre'] .update(atk[0])
            #Mostra as informações da batalha para o jogador 
            Windows['-dano_mostro-'] .update(atk[1])
            Windows['-dano_jogador-'] .update(atk[2])

            #atualiza vida do jogador
            energia_v -= 2
        
        elif atk[0]== 'Esquiva':
            Windows['Empate'] .update(atk[0])
            #aplica informações na tela
            Windows['-dano_mostro-'] .update(atk[1])
            Windows['-dano_jogador-'] .update(atk[2])

        elif atk == 'Criatura foi morta':
            #informa jogador a morte de mostro reseta variaveis de combate
            #troca de tela automaticamente com tempo de leitura para o jogador
            Windows['causa'] .update(atk)
            sg.user_settings_set_entry('-last position-', janela_248.current_location())
            gerador_mapa.grava_mapa('248 »')
            #limita_botao_sorte = 0
            #ativação_botão_sorte = 0
            #liberar limitadores na alfa de test
            #criar ação depois da morte da criatura - em criação

        elif atk == 'Você foi morto':
            #jogador morreu informa e grava no mapa
            Windows['Sofre'] .update(atk)
            gerador_mapa.morte_jogador()
            janela_morte = telas_recorentes.tela_morte()
            janela_248.close()

    #ajusta uso da sorte e apresentação das informações para o jogador
    elif Windows == janela_248 and eventos == 'Sorte':
        #limpa informação da tela
        Windows['causa'] .update('')
        Windows['Sofre'] .update('')
        Windows['Empate'] .update('')
        Windows['-dano_mostro-'] .update('')
        Windows['-dano_jogador-'] .update('')

        usou_sorte = sorte_combate.uso_de_sorte(ativação_botão_sorte,sorte_v,atk)

        if usou_sorte == 'Dano ampliado':
            Windows['causa'] .update(usou_sorte)
            mostro_1_V -= 2
            ativação_botão_sorte = True
        
        elif usou_sorte == 'Dano reduzido':
            Windows['Empate'] .update(usou_sorte)
            mostro_1_V -= 1
            ativação_botão_sorte = True
        
        elif usou_sorte == 'Sangramento contido':
            Windows['causa'] .update(usou_sorte)
            ativação_botão_sorte = True
            energia_v += 1
        
        elif usou_sorte == 'Sangramento aumentado':
            Windows['Sofre'] .update(usou_sorte)
            ativação_botão_sorte = True
            energia_v -= 1
        
        elif usou_sorte == 'sorte não aplicavel':
            Windows['Empate'] .update(usou_sorte)
        
        elif usou_sorte == 'Sorte Esgotada':
            Windows['Sofre'] .update(usou_sorte)
        
        else:
            Windows['Empate'] .update('sorte já usada')


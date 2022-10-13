#Bibliotecas Extras
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
import dados

import aplicador_de_dano
import alterador_de_indices
import efeitos_sonoros

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

janela_abertura = telas_iniciais.tela_abertura()
janela_intro = janela_regras = janela_sugestao =janela_dicas = janela_boatos1 = janela_boatos2 = janela_000 = None

#janelas recorentes
janela_menu = janela_mapa = janela_morte = None

#primeira leva de janela
janela_nome = janela_001 = janela_278_156 = janela_343 = janela_71 = janela_92_71 = janela_248 = None

#grava janela antes de acessar o menu
volta = None

#limitador de criação de botão
limita_botão_nome = limita_botao_sorte = 0

#ativação de botão
ativação_botão_sorte = 0

#variaveis de combate
resultado_batalha = ' '

#indices base do jogador
energia = habilidade = sorte = provisoes = 0

#indices variaveis do jogador
energia_v = habilidade_v = sorte_v = 0

#poção jogador
poção_base = ' '
numero_poção = 0

#indeces mostrons
mostro_1_V = mostro_2_V = mostro_3_V = mostro_4_V = 0
mostro_1_H = mostro_2_H = mostro_3_H = mostro_4_H = 0

#nome global
nome_jogador = ' '

#confirmado de saida para tela inicial
confirma_saida = 0

#contador abertura inicial
abertura = 0

#O loop foi criado de acordo com o surgimento das telas
#Assim não vão respeitar uma ordem numerica, mapa principal sendo criado
 
while True:

    Windows,eventos,valores = sg.read_all_windows(timeout= 1000)
    

    if janela_abertura and eventos == sg.TIMEOUT_EVENT:

        if abertura < 1:
            efeitos_sonoros.abertura()

        while abertura <= 7:

            if abertura <3:
                janela_abertura['-imprime-'].update('Apresenta')
                janela_abertura.refresh()
                time.sleep(1)
                abertura += 1

            elif abertura <= 5:
                janela_abertura['-imprime-'].update('O Feiticeiro')
                janela_abertura.refresh()
                time.sleep(1)
                abertura += 1
            
            elif abertura <= 6:
                janela_abertura['-nome_2-'].update('DA MONTANHA DE FOGO')
                janela_abertura.refresh()
                time.sleep(1)
                abertura += 1
            
            else:
                janela_intro = telas_iniciais.tela_intro()
                janela_abertura.close()
                abertura += 1
                break

#Janelaintro

    if Windows == janela_intro and eventos == sg.WIN_CLOSED or Windows == janela_intro and eventos == 'Sair':
        break
    
    elif Windows == janela_intro and eventos == 'Jogar':
        sg.user_settings_set_entry('-last position-', janela_intro.current_location())
        efeitos_sonoros.botão()
        time.sleep(0.2)
        janela_nome = telas_de_introdução.tela_nome()
        janela_intro.close()
           
    elif Windows == janela_intro and eventos == 'Regras':
        efeitos_sonoros.botão()
        time.sleep(0.2)
        janela_regras = telas_iniciais.tela_regras()
        janela_intro.close()

    elif Windows == janela_intro and eventos == 'Biblioteca de mostros':
        pass
        #criar ação

    elif Windows == janela_intro and eventos == 'Créditos':
        efeitos_sonoros.botão()
        time.sleep(0.2)
        arquivo = open(r'.\ark_txt\popup_t\creditos.txt', 'r', encoding='utf-8').read()
        sg.popup_no_titlebar(f'{arquivo}')

    elif Windows == janela_intro and eventos == 'Sugestões':
        efeitos_sonoros.botão()
        time.sleep(0.2)
        janela_sugestao = telas_iniciais.tela_sugestao()
        janela_intro.close()
    
#Janelaregras

    if Windows == janela_regras and eventos == sg.WIN_CLOSED:
        break
    
    elif Windows == janela_regras and eventos == 'Inicio':
        janela_intro = telas_iniciais.tela_intro()
        janela_regras.close()
    
    elif Windows == janela_regras and eventos =='Indices':
        arquivo = open(r'.\ark_txt\popup_t\indices.txt' , 'r', encoding='utf-8'). read()
        Windows['info'] .update(arquivo)
    
    elif Windows == janela_regras and eventos == 'Batalha':
        arquivo = open(r'.\ark_txt\popup_t\Batalha.txt', 'r', encoding='utf-8').read()
        Windows['info'] .update(arquivo) 
    
    elif Windows == janela_regras and eventos == 'Fuga':
        arquivo = open(r'.\ark_txt\popup_t\Fuga.txt', 'r', encoding='utf-8').read()
        Windows['info'] .update(arquivo)
    
    elif Windows == janela_regras and eventos == 'Sorte':
        arquivo = open(r'.\ark_txt\popup_t\sorte.txt', 'r', encoding='utf-8').read()
        Windows['info'] .update(arquivo)
        
    elif Windows == janela_regras and eventos == 'Inventário':
        arquivo = open(r'.\ark_txt\popup_t\inventario.txt', 'r', encoding='utf-8').read()
        Windows['info'] .update(arquivo)
          
    elif Windows == janela_regras and eventos == 'Poções':
        arquivo = open(r'.\ark_txt\popup_t\poçoes.txt', 'r', encoding='utf-8').read()
        Windows['info'] .update(arquivo)
        
    elif Windows == janela_regras and eventos == 'Provisões':
        arquivo = open(r'.\ark_txt\popup_t\provisoes.txt', 'r', encoding='utf-8').read()
        Windows['info'] .update(arquivo)
        
#janela Sugestão

    if Windows == janela_sugestao and eventos == sg.WIN_CLOSED:
        break

    elif Windows == janela_sugestao and eventos == 'Voltar':
        janela_intro = telas_iniciais.tela_intro()
        janela_sugestao.close()
    
    elif Windows == janela_sugestao and eventos == 'Enviar':
        EMAIL_ADDRESS = dados.Email
        EMAIL_PASSWORD = dados.Senha
        texto_user = valores['usertexto']
    
        msg = EmailMessage()
        msg['subject'] = 'Sugestões'
        msg['From'] = dados.Email
        msg['To'] = dados.Email
        msg.set_content(texto_user)

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
                smtp.send_message(msg)
                Windows['mensagem'] .update('Sugestão Enviada! \n Obrigado!')
        
        except TimeoutError as erro1:
            Windows['mensagem'].update('Verifiqeu sua conecção')
            
        except Exception as erro2:
            sg.popup_error(erro2, no_titlebar= True)

#Janela Nome

    if  Windows == janela_nome and eventos == sg.WIN_CLOSED:
        break

    elif Windows == janela_nome and eventos == 'Voltar':
        limita_botão_nome = 0
        nome_jogador = ' '
        janela_intro = telas_iniciais.tela_intro()
        janela_nome.close()
    
    elif Windows == janela_nome and eventos == 'Validar':
        
        Windows['aviso1'].update('')
        Windows['aviso2'].update('')
        nome_gerado = str(valores['usernome']).strip()

        if len(nome_gerado) > 12:
            Windows['aviso2'].update('Máximo 12 caracteres')
        
        elif len(nome_gerado) < 3:
            Windows['aviso2'].update('Minimo 3 caracteres')
        
        else:
            Windows['aviso1'].update('Nome Valido!')
            nome_jogador = nome_gerado

            if limita_botão_nome == 0:
                #cria botão na janela
                janela_nome.extend_layout(janela_nome['valido'],
                [[sg.Button('Começar', font=font2)]])
                #limita a criação
                limita_botão_nome += 30
    
    elif Windows == janela_nome and eventos == 'Começar':
        sg.user_settings_set_entry('-last position-', janela_nome.current_location())
        limita_botão_nome = 0
        janela_dicas = telas_de_introdução.tela_dicas()
        janela_nome.close()

#Janela dica inicial

    if Windows == janela_dicas and eventos == sg.WIN_CLOSED:
        break

    elif Windows == janela_dicas and eventos == 'Boatos':
        sg.user_settings_set_entry('-last position-', janela_dicas.current_location())
        janela_boatos1 = telas_de_introdução.tela_boatos1()
        janela_dicas.close()

    elif Windows == janela_dicas and eventos == 'Voltar':
        sg.user_settings_set_entry('-last position-', janela_dicas.current_location())
        limita_botão_nome = 0
        janela_nome = telas_de_introdução.tela_nome()
        janela_dicas.close()

#janela de boatos1

    if Windows == janela_boatos1 and eventos == sg.WIN_CLOSED:
        break

    elif Windows == janela_boatos1 and eventos == 'Sair':
        janela_boatos1.close()
        break

    elif Windows == janela_boatos1 and eventos == 'Próximo':
        sg.user_settings_set_entry('-last position-', janela_boatos1.current_location())
        janela_boatos2 = telas_de_introdução.tela_boatos2()
        janela_boatos1.close()

    elif Windows == janela_boatos1 and eventos == 'Voltar':
        sg.user_settings_set_entry('-last position-', janela_boatos1.current_location())
        janela_dicas = telas_de_introdução.tela_dicas()
        janela_boatos1.close()


#janela de boatos2

    if Windows == janela_boatos2 and eventos == sg.WIN_CLOSED:
        break

    elif Windows == janela_boatos2 and eventos == 'Começar':
        
        sg.user_settings_set_entry('-last position-', janela_boatos2.current_location())
        janela_000 = telas_jogo_0_100.tela_000()
        janela_boatos2.close()

    elif Windows == janela_boatos2 and eventos == 'Anterior':
        sg.user_settings_set_entry('-last position-', janela_boatos2.current_location())
        janela_boatos1 = telas_de_introdução.tela_boatos1()
        janela_boatos2.close()

#janela 000 - gerador e validador de indices

    if Windows == janela_000 and eventos == sg.WIN_CLOSED:
        break
    #gera e valida os indices

    elif Windows == janela_000 and eventos == 'HABILIDADE':

        #verifica se já foi gerado
        if habilidade <= 0:
            numero_aleatorio = int(random.randint(1,6))
            soma_h = int(numero_aleatorio + 6)

            Windows['H'] .update(f'{numero_aleatorio}')
            Windows['S_H'] .update(f'= {soma_h}')

            habilidade = habilidade_v = soma_h
        
        else:
            Windows['aviso_indices'].update('Habilidade Já foi Gerada')
    

    elif Windows == janela_000 and eventos == 'ENERGIA':

        if energia <= 0:
            numero_aleatorio1 = int(random.randint(1,6))
            numero_aleatorio2 = int(random.randint(1,6))
            soma_e = int((numero_aleatorio1 + numero_aleatorio2) + 12)

            Windows['E'] .update(f'{numero_aleatorio1 + numero_aleatorio2}')
            Windows['S_E'] .update(f'= {soma_e}')

            energia = energia_v = soma_e
        
        else:
            Windows['aviso_indices'].update('Energia Já foi Gerada')
        

    elif Windows == janela_000 and eventos == 'SORTE':

        if sorte <= 0:
            numero_aleatorio = int(random.randint(1,6))
            soma_s = int(numero_aleatorio + 6)

            Windows['S'] .update(f'{numero_aleatorio}')
            Windows['S_S'] .update(f'= {soma_s}')

            sorte = sorte_v = soma_s
        
        else:
            Windows['aviso_indices'].update('Sorte Já foi Gerada')

    #gera e valida as poçoes

    elif Windows == janela_000 and eventos == 'P1':
        
        if numero_poção <=0:
            numero_poção = 2
            poção_base = 'Poção Habilidade:'
            Windows['C_P'].update('Habilidade selecionada')

        else:
            Windows['C_P'].update('')
            Windows['aviso_pocao'].update('Poção já foi Gerada')
            
    elif Windows == janela_000 and eventos == 'P2':

        if numero_poção <=0:
            numero_poção = 2
            poção_base = 'Poção Força:'
            Windows['C_P'].update('Força selecionada')
        
        else:
            Windows['C_P'].update('')
            Windows['aviso_pocao'].update('Poção já foi Gerada')
    
    elif Windows == janela_000 and eventos == 'P3':

        if numero_poção <=0:
            numero_poção = 2
            poção_base = 'Poção Fortuna:'
            Windows['C_P'].update('Fortuna selecionada')
        
        else:
            Windows['C_P'].update('')
            Windows['aviso_pocao'].update('Poção já foi Gerada')
    
    #verifica se todos os itens foram gerados

    elif Windows == janela_000 and eventos == 'Estou pronto':

        if energia > 0 and habilidade > 0 and sorte > 0 and numero_poção > 0:
            provisoes = 10
            txt.valida_txt()
            sg.user_settings_set_entry('-last position-', janela_000.current_location())
            janela_001 = telas_jogo_0_100.tela_001()
            janela_000.close()
        
        else:
            Windows['C_P'].update('')
            Windows['aviso_pocao'].update('')
            Windows['aviso_validador'].update('Confira os indices e poções')

    elif Windows == janela_000 and eventos == 'Voltar':
        energia = habilidade = sorte = provisoes = 0
        energia_v = habilidade_v = sorte_v = 0
        numero_poção = 0
        poção_base = ' '
        sg.user_settings_set_entry('-last position-', janela_000.current_location())
        janela_boatos2 = telas_de_introdução.tela_boatos2()
        janela_000.close()

    #reseta todas as info

    elif Windows == janela_000 and eventos == 'Resetar':
        energia = habilidade = sorte = provisoes = 0
        energia_v = habilidade_v = sorte_v = 0
        numero_poção = 0
        poção_base = ' '
        janela_000.close()
        janela_000 = telas_jogo_0_100.tela_000()

#janelas recorentes inicio

#janela menu

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

    if Windows == janela_mapa and eventos == sg.WIN_CLOSED:
        break

    elif Windows == janela_mapa and eventos == 'Menu':
        sg.user_settings_set_entry('-last position-', janela_mapa.current_location())
        janela_menu = telas_recorentes.tela_menu(energia, habilidade, sorte, provisoes, energia_v, habilidade_v, sorte_v, poção_base, numero_poção)
        janela_mapa.close()
    
    elif Windows == janela_mapa and eventos == 'Sair':
        sg.user_settings_set_entry('-last position-', janela_mapa.current_location())
        volta = volta.un_hide()
        janela_mapa.close()
        janela_menu.close()
    
    elif Windows == janela_mapa and eventos == 'Salvar':
        gerador_txt_user.save_mapa()
        Windows['info'].update('Salvo em Documentos')

#janela Morte
    if Windows == janela_morte and eventos == sg.WIN_CLOSED or Windows == janela_morte and eventos =='Sair':
            break

    elif Windows == janela_morte and eventos =='-Inicio-':
        janela_intro = telas_iniciais.tela_intro()
        janela_morte.close()
    
    elif Windows == janela_morte and eventos == '-Salva-':
        gerador_txt_user.save_mapa()
        Windows['-aviso_save-'].update('Salvo em Documentos')

#janela 001

    if Windows == janela_001 and eventos == sg.WIN_CLOSED:
        break

    elif Windows == janela_001 and eventos == 'Oeste':
        local = sg.user_settings_set_entry('-last position-', janela_001.current_location())
        
        #Grava mapa
        gerador_mapa.grava_mapa('001 » ')
        janela_71 = telas_jogo_0_100.tela_71()
        janela_001.close()
        

    elif Windows == janela_001 and eventos == 'Leste':
        local = sg.user_settings_set_entry('-last position-', janela_001.current_location())
        
        #Grava mapa
        gerador_mapa.grava_mapa('001 » ')

        janela_278_156 = telas_jogo_201_300.tela_278_156()
        janela_001.close()

    elif Windows == janela_001 and eventos == 'Menu':
        sg.user_settings_set_entry('-last position-', janela_001.current_location())
        janela_menu = telas_recorentes.tela_menu(energia, habilidade, sorte, provisoes, energia_v, habilidade_v, sorte_v, poção_base, numero_poção)
        janela_001.hide()
        volta = janela_001

#janela 278_156

    if Windows == janela_278_156 and eventos == sg.WIN_CLOSED:
        break
    
    elif Windows == janela_278_156 and eventos == 'Derrubar':
        sg.user_settings_set_entry('-last position-', janela_278_156.current_location())
        Windows['Info0'] .update('Você bate contra aporta com o ombro.')

        #validação de indice de habilidade

        resultado_278_156 = gerador_de_dados.dado_duplo()

        if resultado_278_156 <= habilidade:
            #jogador consegui derrubar a porta
            Windows['info2'] .update('A Porta ABRIU!')
            janela_278_156.refresh()

            #Diminui Habilidade jogador
            habilidade_v -= 1

            #grava local no mapa
            gerador_mapa.grava_mapa('278-156 » ')

            #vai para nova tela automatico
            time.sleep(3)
            janela_278_156.close()
            janela_343 = telas_jogo_301_400.tela_343()
            
        elif resultado_278_156 > habilidade:
            Windows['Info1'] .update('Você esfrega o ombro machucado \n  Resolvendo não tentar de novo.')
            janela_278_156.refresh()
            #jogador não consegui derrubar a porta muda de tela automatico

            #grava local no mapa
            gerador_mapa.grava_mapa('278-156 » ')

            time.sleep(3)
            #vai para nova tela automatico
            janela_92_71 = telas_jogo_0_100.tela_92_71()
            janela_278_156.close()
                    
    elif Windows == janela_278_156 and eventos == 'Retornar':
        sg.user_settings_set_entry('-last position-', janela_278_156.current_location())
        
        #grava local no mapa
        gerador_mapa.grava_mapa('278-156 » ')
        
        janela_92_71 = telas_jogo_0_100.tela_92_71()
        janela_278_156.close()
            
    elif Windows == janela_278_156 and eventos == 'Menu':
        sg.user_settings_set_entry('-last position-', janela_278_156.current_location())
        janela_menu = telas_recorentes.tela_menu(energia, habilidade, sorte, provisoes, energia_v, habilidade_v, sorte_v, poção_base, numero_poção)
        janela_278_156.hide()
        volta = janela_278_156
 
#janela 343

    if Windows == janela_343 and eventos == sg.WIN_CLOSED:
        break

    elif Windows == janela_343 and eventos == 'Menu':
        sg.user_settings_set_entry('-last position-', janela_343.current_location())
        janela_menu = telas_recorentes.tela_menu(energia, habilidade, sorte, provisoes, energia_v, habilidade_v, sorte_v, poção_base, numero_poção)
        janela_343.hide()
        volta = janela_343
    
    elif Windows == janela_343 and eventos == 'Subir':
        sg.user_settings_set_entry('-last position-', janela_343.current_location())
        
        #grava local no mapa
        gerador_mapa.grava_mapa('343 » ')

        janela_92_71 = telas_jogo_0_100.tela_92_71()
        janela_343.close()
        
#janela 71

    if Windows == janela_71 and eventos == sg.WIN_CLOSED:
        break

    elif Windows == janela_71 and eventos == 'Menu':
        sg.user_settings_set_entry('-last position-', janela_71.current_location())
        janela_menu = telas_recorentes.tela_menu(energia, habilidade, sorte, provisoes, energia_v, habilidade_v, sorte_v, poção_base, numero_poção)
        janela_71.hide()
        volta = janela_71
    
    elif Windows == janela_71 and eventos == 'Testar':
        sg.user_settings_set_entry('-last position-', janela_71.current_location())
        
        #validando a sorte
        if sorte_v > 0:
            resultado_71 = gerador_de_dados.dado_duplo()

            if resultado_71 <= sorte_v:
                Windows['S1'].update('A Criatura não acordou!')
                Windows['S2'].update('Você perdeu 1 ponto de sorte')
                janela_71.refresh()
                #sorte ajudou o jogador - diminui sorte variavel
                sorte_v -= 1
                #grava local no mapa
                gerador_mapa.grava_mapa('71 » ')
                time.sleep(3)
                #criar ação - em produção
               
            elif resultado_71> sorte_v:
                #informa o jogador e atualiza a tela
                Windows['S2'] .update('você pisa em terreno mole e faz um barulho!'
                '\nOs olhos do ser se abrem instantaneamente')
                Windows['S3'].update('Menos 1 ponto de Sorte\n        Hora de Lutar!')
                janela_71.refresh()
                
                #sorte não ajudou o jogador - diminui sorte variavel
                sorte_v -= 1
                mostro_1_V = 5
                mostro_1_H = 6
                #grava local no mapa
                gerador_mapa.grava_mapa('71 » ')
                
                #pausa a tela para leitura da informação apresentada
                #depois troca a tela

                time.sleep(3)
                janela_248 = telas_jogo_201_300.tela_248(nome_jogador, mostro_1_H)
                janela_71.close()

        else:
            #jogador sem sorte vai direto para o combate
            #informa o jogador e atualiza a tela
            Windows['S2'] .update('você pisa em terreno mole e faz um barulho!'
            '\nOs olhos do ser se abrem instantaneamente')
            Windows['S3'].update('Hora de Lutar!'.center())
            janela_71.refresh()
            #grava local no mapa
            mostro_1_V = 5
            mostro_1_H = 6
            gerador_mapa.grava_mapa('71 » ')
            #pausa a tela para leitura da informação apresentada
            #depois troca a tela
            time.sleep(3)
            janela_248 = telas_jogo_201_300.tela_248(nome_jogador, mostro_1_H)
            janela_71.close()

# janela 92_71

    if Windows == janela_92_71 and eventos == sg.WIN_CLOSED:
        break

    elif Windows == janela_92_71 and eventos == 'Menu':
        sg.user_settings_set_entry('-last position-', janela_92_71.current_location())
        janela_menu = telas_recorentes.tela_menu(energia, habilidade, sorte, provisoes, energia_v, habilidade_v, sorte_v, poção_base, numero_poção)
        janela_92_71.hide()
        volta = janela_92_71
    
    elif Windows == janela_92_71 and eventos == 'Testar':
        sg.user_settings_set_entry('-last position-', janela_92_71.current_location())

        #validando a sorte

        if sorte_v > 0:
            resultado_92_71 = gerador_de_dados.dado_duplo()

            if resultado_92_71 <= sorte_v:
                #informa o jogador e atualiza a tela
                Windows['S1'].update('A Criatura não acordou!')
                Windows['S2'].update('Você perdeu 1 ponto de sorte')
                janela_92_71.refresh()

                #sorte ajudou o jogador - diminui sorte variavel
                sorte_v -= 1
                #grava local no mapa
                gerador_mapa.grava_mapa('92-71 »')
                
                #pausa a tela para leitura da informação apresentada
                #depois troca a tela
                time.sleep(3)
                #criar ação - tela em criação
            
            elif resultado_92_71 > sorte_v:
                #informa o jogador e atualiza a tela
                Windows['S2'] .update('você pisa em terreno mole e faz um barulho!'
                '\nOs olhos do ser se abrem instantaneamente')
                Windows['S3'].update('Menos 1 ponto de Sorte\n        Hora de Lutar!')
                janela_92_71.refresh()

                #sorte não ajudou o jogador - diminui sorte variavel
                sorte_v -= 1
                mostro_1_V = 5
                mostro_1_H = 6
                #gera mostro para a luta

                #grava local no mapa
                gerador_mapa.grava_mapa('92-71 »')

                #pausa a tela para leitura da informação apresentada
                #depois troca a tela
                time.sleep(3)
                janela_248 = telas_jogo_201_300.tela_248(nome_jogador, mostro_1_H)
                janela_92_71.close()

        else:
            #jogador sem sorte vai direto para o combate
            #informa o jogador e atualiza a tela
            Windows['S2'] .update('você pisa em terreno mole e faz um barulho!'
            '\nOs olhos do ser se abrem instantaneamente')
            Windows['S3'].update('Hora de Lutar!')
            janela_92_71.refresh()

            #gera mostro para a luta
            mostro_1_V = 5
            mostro_1_H = 6
            #grava local no mapa
            gerador_mapa.grava_mapa('92-71 »')

            #pausa a tela para leitura da informação apresentada
            #depois troca a tela
            time.sleep(3)
            janela_248 = telas_jogo_201_300.tela_248(nome_jogador, mostro_1_H)
            janela_92_71.close()
    
#janela 248 combate

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

                    Windows['causa'] .update('Dano Causado')
                    #Mostra as informações da batalha para o jogador 
                    Windows['-dano_mostro-'] .update(soma_força_mostro)
                    Windows['-dano_jogador-'] .update(soma_força_user)

                    #grava resultado de combate para aplicar na sorte
                    resultado_batalha = 'Dano_causado'
                    
                    #Atualiza vida da criatura e aplica dano normal
                    aplicador_de_dano.dano_aumentado_normal()
                    
                elif soma_força_user < soma_força_mostro:

                    Windows['Sofre'] .update('Dano Sofrido')
                    #Mostra as informações da batalha para o jogador 
                    Windows['-dano_mostro-'] .update(soma_força_mostro)
                    Windows['-dano_jogador-'] .update(soma_força_user)

                    #grava resultado de combate para aplicar na sorte
                    resultado_batalha = 'Dano_sofrido'

                    #atualiza vida do jogador
                    aplicador_de_dano.dano_normal_recebido()
                    

                else:
                    Windows['Empate'] .update('Esquiva')
                    #aplica informações na tela
                    Windows['-dano_mostro-'] .update(soma_força_mostro)
                    Windows['-dano_jogador-'] .update(soma_força_user)

            else:
                        #informa jogador a morte de mostro reseta variaveis de combate
                        #troca de tela automaticamente com tempo de leitura para o jogador
                        Windows['causa'] .update('Criatura foi morta')
                        sg.user_settings_set_entry('-last position-', janela_248.current_location())
                        gerador_mapa.grava_mapa('248 »')
                        #limita_botao_sorte = 0
                        #resultado_batalha = ' '
                        #ativação_botão_sorte = 0

                        #liberar limitadores na alfa de test
                        #criar ação depois da morte da criatura - em criação

        else:
                    #jogador morreu informa e grava no mapa
                    Windows['Sofre'] .update('Você foi morto')
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
                        Windows['causa'] .update('Dano ampliado')
                        ativação_botão_sorte += 1
                        #aplica dano aumentado
                        aplicador_de_dano.dano_aumentado_normal()
                        
                    else:
                        #sorte não ajudou na batalha
                        Windows['Empate'] .update('Dano reduzido')
                        ativação_botão_sorte += 1
                        #Reduz dano normal
                        aplicador_de_dano.dano_reduzido()
                        
                elif resultado_batalha == 'Dano_sofrido':
                    #jogador teve sorte e dano foi reduzido
                    if alterador_de_sorte_e_validador  > teste_sorte1 + teste_sorte2:
                        Windows['causa'] .update('Sangramento contido')
                        ativação_botão_sorte += 1
                        aplicador_de_dano.conteve_sangramento()
                        
                    #jogador não teve sorte dano foi aumentado
                    else:
                        Windows['Sofre'] .update('Sangramento aumentado')
                        ativação_botão_sorte += 1
                        aplicador_de_dano.sangramento_aumentado()

                #jogador e mostro tem força igual, sorte não é aplicavel      
                else:
                    Windows['Empate'] .update('sorte não aplicavel')
            
            #jogador esgotou a sorte
            else:
                Windows['Sofre'] .update('Sorte Esgotada')
        
        #sorte já foi usada naquela rodada
        else:
            Windows['Empate'] .update('sorte já usada')

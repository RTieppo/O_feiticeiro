
#Dano sofrido - usando a sorte - jogador

def conteve_sangramento():
    vida_jogador = int(open(r'.\ark_txt\ind\ENER_V.txt', 'r', encoding='utf-8').read())
    conteve_sangramento = open(r'.\ark_txt\ind\ENER_V.txt', 'w', encoding='utf-8')
    conteve_sangramento.write(f'{vida_jogador + 1}')
    conteve_sangramento.close()

def sangramento_aumentado():
    vida_jogador = int(open(r'.\ark_txt\ind\ENER_V.txt', 'r', encoding='utf-8').read())
    aumento_do_sangramento = open(r'.\ark_txt\ind\ENER_V.txt', 'w', encoding='utf-8')
    aumento_do_sangramento.write(f'{vida_jogador - 1}')
    aumento_do_sangramento.close()

#Dano sofrido - normal - jogador

def dano_normal_recebido():
    vida_jogador = int(open(r'.\ark_txt\ind\ENER_V.txt', 'r', encoding='utf-8').read())
    grava_dano_ao_jogador = open(r'.\ark_txt\ind\ENER_V.txt', 'w', encoding='utf-8')
    grava_dano_ao_jogador.write(f'{vida_jogador - 2}')
    grava_dano_ao_jogador.close()

#Dano normal e dano amplido com o uso de sorte

def dano_aumentado_normal():
    vida_criatura = int(open(r'.\ark_txt\Batalha\orca.txt', 'r', encoding='utf-8').read())
    Dano_ampliado = open(r'.\ark_txt\Batalha\orca.txt', 'w', encoding='utf-8')
    diminui_vida_criatura = vida_criatura - 2
    Dano_ampliado.write(f'{diminui_vida_criatura}')
    Dano_ampliado.close()

#Dano reduzido com o uso de sorte

def dano_reduzido():
    vida_criatura = int(open(r'.\ark_txt\Batalha\orca.txt', 'r', encoding='utf-8').read())
    Dano_reduzido = open(r'.\ark_txt\Batalha\orca.txt', 'w', encoding='utf-8')
    aumenta_vida_criatura = vida_criatura + 1
    Dano_reduzido.write(f'{aumenta_vida_criatura}')
    Dano_reduzido.close()

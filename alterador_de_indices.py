
#Diminui indices de sorte - Habilidade - energia

def menos_sorte():
    sorte_jogador = int(open(r'.\ark_txt\ind\Sort_V.txt','r', encoding='utf-8').read())
    alterador_sorte = open(r'.\ark_txt\ind\Sort_V.txt','w', encoding='utf-8')
    alterador_sorte.write(f'{sorte_jogador - 1}')
    alterador_sorte.close()

def menos_habilidade():
    
    arquivo_habilidade_variavel= int(open(r'.\ark_txt\ind\HAB_V.txt', 'r', encoding='utf-8').read())
    alterador_habilidade = open(r'.\ark_txt\ind\HAB_V.txt', 'w', encoding='utf-8')
    alterador_habilidade.write(f'{arquivo_habilidade_variavel - 1}')
    alterador_habilidade.close()
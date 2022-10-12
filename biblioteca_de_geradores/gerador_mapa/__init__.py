#grava morte jogador

def morte_jogador():
    grava_mapa = open(r'C:\Users\Public\O feiticeiro\Mapa.txt', 'a', encoding='UTF-8')
    grava_mapa.write('Faleceu!')
    grava_mapa.close()

#Salva mapa confore jogador avança cria arquivo caso não exista

def grava_mapa(local):
    import os
    while True:
        verifica_arquivos = os.listdir(r'C:\Users\Public')
        if 'O feiticeiro' in verifica_arquivos:
            grava_mapa = open(r'C:\Users\Public\O feiticeiro\Mapa.txt', 'a', encoding='UTF-8')
            grava_mapa.write(local)
            grava_mapa.close()
            break
        else:
            os.makedirs(r'C:\Users\Public\O feiticeiro')
            cria_txt = open(r'C:\Users\Public\O feiticeiro\Mapa.txt','w',encoding='UTF-8')
            cria_txt.write('')
            cria_txt.close()

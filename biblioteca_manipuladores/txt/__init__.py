def valida_txt():
    import os
    while True:
        verifica_arquivos = os.listdir(r'C:\Users\Public')
        if 'O feiticeiro' in verifica_arquivos:
            cria_txt = open(r'C:\Users\Public\O feiticeiro\Mapa.txt','w',encoding='UTF-8')
            cria_txt.write('')
            cria_txt.close()
            break
        else:
            os.makedirs(r'C:\Users\Public\O feiticeiro')
            cria_txt = open(r'C:\Users\Public\O feiticeiro\Mapa.txt','w',encoding='UTF-8')
            cria_txt.write('')
            cria_txt.close()

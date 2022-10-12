
def save_mapa():
    import os
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
            save = open(r'C:\Users\Public\O feiticeiro\Mapa.txt', 'r', encoding='utf-8').read()
            criar_arquivo = open(caminho3, 'w', encoding='utf-8')
            criar_arquivo.write(save)
            criar_arquivo.close()
            break

        else:
            os.makedirs(caminho2)
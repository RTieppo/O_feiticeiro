from biblioteca_de_geradores import gerador_de_dados

def combateX1(energia_v,mostro_1_V,habilidade_v,mostro_1_H):

    if energia_v > 0:

        #valida vida do mostro
        if mostro_1_V > 0:
            
            #Gera a força do jogador e do mostro
            força_user = gerador_de_dados.dado_duplo() + habilidade_v

            força_mostro = gerador_de_dados.dado_duplo() + mostro_1_H

            if força_user > força_mostro:
                return ('Dano causado', força_mostro, força_user)

                
            elif força_user < força_mostro:
                return ('Dano Sofrido', força_mostro, força_user)

            
            else:
                return ('Esquiva', força_mostro, força_user)

        else:
            return ('Criatura foi morta')

    else:
        return ('Você foi morto')

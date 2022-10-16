from biblioteca_de_geradores import gerador_de_dados

def uso_de_sorte(ativação_botão_sorte,sorte_v,atk):

    if ativação_botão_sorte == False:

        #validação se jogador ainda tem sorte
        if sorte_v > 0:

            #gerador de comparação de sorte
            teste_sorte = gerador_de_dados.dado_duplo() 

            if atk[0] == 'Dano causado':
                if sorte_v > teste_sorte:
                    return 'Dano ampliado'
                else:
                    return 'Dano reduzido'
                    
            elif atk[0] == 'Dano Sofrido':
                #jogador teve sorte e dano foi reduzido
                if sorte_v  > teste_sorte:
                    return 'Sangramento contido'
                    
                #jogador não teve sorte dano foi aumentado
                else:
                    return 'Sangramento aumentado'

            #jogador e mostro tem força igual, sorte não é aplicavel      
            else:
                return 'sorte não aplicavel'

        #jogador esgotou a sorte
        else:
            return 'Sorte Esgotada'
    
    #sorte já foi usada naquela rodada
    else:
        return 'sorte já usada'
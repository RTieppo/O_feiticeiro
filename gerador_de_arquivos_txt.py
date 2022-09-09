
def grava_pocao_habilidade():
    arquivo0 = open('ark_txt\ind\Pocao.txt', 'w', encoding='utf-8')
    arquivo0.write('Poção Habilidade: 2')
    arquivo0.close()

    arquivo1 = open('ark_txt\ind\Po_v.txt', 'w', encoding='utf-8')
    arquivo1.write('2')
    arquivo1.close()

def grava_pocao_forca():
    arquivo0 = open('ark_txt\ind\Pocao.txt', 'w', encoding='utf-8')
    arquivo0.write('Poção Força: 2')
    arquivo0.close()

    arquivo1 = open('ark_txt\ind\Po_v.txt', 'w', encoding='utf-8')
    arquivo1.write('2')
    arquivo1.close()

def grava_pocao_fortuna():
    arquivo0 = open('ark_txt\ind\Pocao.txt', 'w', encoding='utf-8')
    arquivo0.write('Poção Fortuna: 2')
    arquivo0.close()

    arquivo1 = open('ark_txt\ind\Po_v.txt', 'w', encoding='utf-8')
    arquivo1.write('2')
    arquivo1.close()

def grava_Provisoes():
    arquivo0 = open('ark_txt\ind\Provisoes.txt', 'w', encoding='utf-8')
    arquivo0.write('10')
    arquivo0.close()

    arquivo1 = open('ark_txt\ind\Pro_v.txt', 'w', encoding='utf-8')
    arquivo1.write('10')
    arquivo1.close()

def reseta_i_H():
    arquivo0 = open('ark_txt\ind\HABILIDADE.txt', 'w', encoding='utf-8')
    arquivo0.write('0')
    arquivo0.close()

    arquivo1 = open('ark_txt\ind\HAB_V.txt', 'w', encoding='utf-8')
    arquivo1.write('0')
    arquivo1.close()

def reseta_i_E():
    arquivo0 = open('ark_txt\ind\ENERGIA.txt', 'w', encoding='utf-8')
    arquivo0.write('0')
    arquivo0.close()

    arquivo1 = open('ark_txt\ind\ENER_V.txt', 'w', encoding='utf-8')
    arquivo1.write('0')
    arquivo1.close()

def reseta_i_S():
    arquivo0 = open('ark_txt\ind\SORTE.txt', 'w', encoding='utf-8')
    arquivo0.write('0')
    arquivo0.close()

    arquivo1 = open('ark_txt\ind\Sort_V.txt', 'w', encoding='utf-8')
    arquivo1.write('0')
    arquivo1.close()

def reseta_p():
    arquivo0 = open('ark_txt\ind\Pocao.txt', 'w', encoding='utf-8')
    arquivo0.write('')
    arquivo0.close()

    arquivo1 = open('ark_txt\ind\Po_v.txt', 'w', encoding='utf-8')
    arquivo1.write('0')
    arquivo1.close()

def reseta_mapa():
    arquivo0 = open('ark_txt\map\Mapa.txt', 'w', encoding='utf-8')
    arquivo0.write('')
    arquivo0.close()

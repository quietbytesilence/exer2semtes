# EXECÍCIOS DE ENTRADA E SAÍDA
# </Gustavo Maciel>
# 07/03/2024
from alldata.utils import number, num_entre
import math
def media_aritmética_notas():
    a, b = [], 0
    for c in range(3):
        print(f'Digite a {c+1}º nota.')
        a.append(number(1)); b = b + a[c]
    print(f'A média aritmética é: {b/len(a)}')

def celsius_faren():
    print('''
[1] - Celsius -> Fahrenheit
[2] - Fahrenheit -> Celsius
        ''')
    esco = num_entre(1, 2); nome = 'Celsius' if esco == 2 else 'Fahrenheit'
    print(f'Digite o valor: ')
    if esco == 1:
        val = (number(1) * 9/5) + 32
    else:
        val = (number(2) - 32) * 5/9
    print(f'O valor em {nome} é {val:.2f}')

def troca_valor():
    v1 = number(1,'Digite o valor de X')
    v2 = number(1,'Digite o valor de Y')
    print(f'x = {v1} | y = {v2}')
    a = v1; v1 = v2; v2 = a
    print(f'--> x = {v1} | y = {v2}')

def area_circ():
    print(f'Calcular Área do Círculo')
    r = number(2,'Digite o Valor do Raio')
    print(f'Área do Círculo = {(math.pi*r)**2:.2f} π u²')


def area_dive():
    print(f'Calcular Área do Quadrado, Trapézio e Triângulo')
    print('Quadrado/Retângulo')
    qa = number(2,'Digite a Altura: ')
    ql = number(2,'Digite a Largura: ')
    print('='*20)
    print('Trapézio')
    B = number(2,'Digite a Base Maior: ')
    b = number(2,'Digite a Base Menor: ')
    ta = number(2,'Digite a Altura: ')
    print('='*20)
    print('Triângulo')
    trb = number(2,'Digite a Base: ')
    tra = number(2,'Digite a Altura: ')
    print('='*20)
    areas  = {
        'Triângulo': (trb*tra)/2,
        'Trapézio': ((B+b)*ta)/2,
        'Quadrado': qa*ql
    }
    print(f'Área do Quadrado/Retângulo: {areas["Quadrado"]} u²')
    print(f'Área do Trapézio: {areas["Trapézio"]} u²')
    print(f'Área do Triângulo: {areas["Triângulo"]} u²')
    print(f"A maior área é do {list(areas.keys())[list(areas.values()).index(max([areas['Triângulo'], areas['Trapézio'], areas['Quadrado']]))]}, com {max(list(areas.values()))} u²")

#   print(f"a Maior Área é {areas[['Trapézio','Triângulo','Quadrado'][areas['Trapézio'], areas['Triângulo'], areas['Quadrado']].index(max([areas['Trapézio'], areas['Triângulo'], areas['Quadrado']]))]}")

def area_sala():
    print('Calcular a Área da Sala')
    alt = number(2,'Digite a Altura da Sala: ')
    com = number(2,'Digite o Comprimento da Sala: ')
    print(f'A Área Total da Sala É: {alt*com:.2f}')

def piscina():
    print('Utilidades da Piscina')
    prof = number(2,'Digite a Profundidade da Piscina (m): ')
    larg = number(2,'Digite a Largura da Piscina: (m)')
    comp = number(2,'Digite o Comprimento da Piscina: (m)')
    print(f'O Total de água que a piscina comporta é \n---> {(prof*larg*comp) * 1000:.2f}Litros')
    taxa = number(2,'Qual a vazão da tornira em Metros Cúbicos?')
    print(f'O tempo para encher a piscina é de {((larg*comp*prof)/taxa)} Minutos')

def resto():
    print('Conta do Restaurante')
    conta = number(1,'Qual foi o valor da conta?')
    gorje = number(2,'Quanto você deseja dar de gojeta?\nDigite 0 se não quiser. O valor é em porcentagem')
    print(f'Gorjeta: R$: {conta*gorje/100:.2f}\nO valor total é R$: {conta + (conta*(gorje/100)):.2f}')



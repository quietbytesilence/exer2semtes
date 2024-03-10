#Programa de Utilidades
# </Gustavo Maciel>
# 07/03/2024
import math, os

def number(opt, msg='====='):
    print(msg)
    num = None; a = 'Inteiro' if opt == 2 else 'Decimal ou Inteiro'
    while True:
        valor = input('>>>> ').strip()
        try:
            if opt == 1:
                num = float(valor)
            elif opt == 2:
                num = int(valor)
            else:
                print('Erro Crítico: parâmetros incorretos!')
                return 0;
            break
        except ValueError:
            print(f'Valor Inválido! Por favor insira um número. {a}')
    return num;

def clear_term(pause=True):
    if pause:
        a = str(input('Press <ENTER> to Continue.'))
    os.system('cls' if os.name == 'nt' else 'clear')

def num_entre(n1, n2, msg='=====',tp=2):
    while True:
        num = number(tp, msg)
        if n1 <= num <= n2:
            return int(num);
            break
        print(f'Por favor, escolha valores entre {n1} e {n2}')

def pega_maior_igual(lim=0, tp=2):
    while True:
        n1 = number(tp, f'Digite um número maior ou igual a {str(lim)}')
        if n1 >= lim:
            break
    return n1

def pega_interval_list(fim, msg1, msg2, ini=0):
    itens = []
    for item in range(ini, fim):
        print(msg1, item+1, msg2)
        a = number(1)
        itens.append(a)
    return itens

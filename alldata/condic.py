# EXECÍCIOS DE CONDICIONAIS
# </Gustavo Maciel>
# 08/03/2024
from alldata.utils import number, clear_term, num_entre, pega_interval_list
from datetime import datetime
def maior_num():
    print(f"O maior número é: {max([number(1,'Digite o primeiro número: '),number(1,'Digite o segundo número: ')])}")

def conta_vogais():
    p = input('Digite uma palavra: ')
    print(f"O numero de vogais é: {p.count('a')+p.count('e')+p.count('i')+p.count('o')+p.count('u')}")
    
def apro_repro():
    notas = pega_interval_list(3,'Digite a ', 'º nota: ')
    if (sum(notas)/3) >= 6:
        print(f'MÉDIA: {sum(notas)/3:.2f}')
        print('Parabéns. Aluno APROVADO!')
    else:
        print(f'MÉDIA: {sum(notas)/3:.2f}')
        print('Que pena. Aluno REPROVADO!')

def impar_par():
    num = number(2, 'Digite um Número: ')
    a = 'Par' if num % 2 == 0 else 'Impar'
    print(f'O número {num} é {a}')

def mes_extenso():
    mes = ('','Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
    i = num_entre(1, 12, 'Digite o Número do Mês')
    print(f'O mês correspondente é: {mes[i]}')

def sim_nao():
    word = input('Digite a palavra: ').lower().strip()
    if word == 'sim':
        print('SIM!')
    else:
        print('Não!')

def imc():
    peso = num_entre(0, 500, 'Digite o seu peso: ',tp=1)
    altura = num_entre(10, 300, 'Digite sua altura em cm: ',tp=1)
    imc = (peso/((altura/100)**2))
    if imc < 20:
        print(f'Você está ABAIXO do peso')
    elif 20 <= imc <= 25:
        print(f'Você está no peso IDEAL')
    else:
        print(f'Você está ACIMA do peso')
    print(f'IMC: {imc:.2f}')

def signo():
    #Tratar posteriomente para signo Peixes (Problemas com ano Bissexto) - FEITO
    while True:
        dia = num_entre(1, 31, 'Digite o Dia do seu Nascimento: ')
        mes = num_entre(1, 12, 'Digite o Mês do seu Nascimento: ')
        ano = num_entre(-9999, 9999, 'Digite o Ano de seu Nascimento: ')
        try:
            nascimento = datetime(ano, mes, dia)
            break
        except Exception:
            print(f'Data Inválida. Tente novamente')
    print(f'Considerando {dia}/{mes}/{ano}')
    # Dicionário com os ranges de datas para cada signo
    ranges_de_signos = {
        'Áries': (datetime(ano, 3, 21), datetime(ano, 4, 19)),
        'Touro': (datetime(ano, 4, 20), datetime(ano, 5, 20)),
        'Gêmeos': (datetime(ano, 5, 21), datetime(ano, 6, 20)),
        'Câncer': (datetime(ano, 6, 21), datetime(ano, 7, 22)),
        'Leão': (datetime(ano, 7, 23), datetime(ano, 8, 22)),
        'Virgem': (datetime(ano, 8, 23), datetime(ano, 9, 22)),
        'Libra': (datetime(ano, 9, 23), datetime(ano, 10, 22)),
        'Escorpião': (datetime(ano, 10, 23), datetime(ano, 11, 21)),
        'Sagitário': (datetime(ano, 11, 22), datetime(ano, 12, 21)),
        'Capricórnio': (datetime(ano-1, 12, 22), datetime(ano, 1, 19)),
        'Aquário': (datetime(ano, 1, 20), datetime(ano, 2, 18)),
        'Peixes': (datetime(ano, 2, 19), datetime(ano, 3, 20))
    }
    def verificar_signo(data_usuario):
        for signo, (inicio, fim) in ranges_de_signos.items():
            if inicio <= data_usuario <= fim:
                return signo
        return "Signo não encontrado"
    data_do_usuario = nascimento
    signo = verificar_signo(data_do_usuario)
    print("O signo é:", signo)


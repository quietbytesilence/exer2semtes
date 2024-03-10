def signo():
    #Tratar posteriomente para signo Peixes (Problemas com ano Bissexto) - FEITO
    while True:
        dia = num_entre(1, 31, 'Digite o Dia do seu Nascimento: ')
        mes = num_entre(1, 12, 'Digite o Mês do seu Nascimento: ')
        ano = num_entre(-9999, 9999, 'Digite o Ano de seu Nascimento: ')
        dias_mes = {
            '1': 31,  # Janeiro
            '2': 29,  # Fevereiro
            '3': 31,  # Março
            '4': 30,  # Abril
            '5': 31,  # Maio
            '6': 30,  # Junho
            '7': 31,  # Julho
            '8': 31,  # Agosto
            '9': 30,  # Setembro
            '10': 31,  # Outubro
            '11': 30,  # Novembro
            '12': 31,  # Dezembro
        }
        if dia <= dias_mes[str(mes)]:
            print(f'Ok!')
            print(f'Considerando {dia}/{mes}/{ano}')
            break
        else:
            print(f'Data Inválida!')

    signos = ["Áries", "Touro", "Gêmeos", "Câncer", "Leão", "Virgem",
             "Libra", "Escorpião", "Sagitário", "Capricórnio", "Aquário", "Peixes"]
    intervalos = [
        ((21, 3), (19, 4)),  # Áries
        ((20, 4), (20, 5)),  # Touro
        ((21, 5), (20, 6)),  # Gêmeos
        ((21, 6), (22, 7)),  # Câncer
        ((23, 7), (22, 8)),  # Leão
        ((23, 8), (22, 9)),  # Virgem
        ((23, 9), (22, 10)),  # Libra
        ((23, 10), (21, 11)),  # Escorpião
        ((22, 11), (21, 12)),  # Sagitário
        ((22, 12), (19, 1)),  # Capricórnio
        ((20, 1), (18, 2)),  # Aquário
        ((19, 2), (20, 3)),  # Peixes (considera ano bissexto)
    ]

    # Ajustar data para Peixes em anos bissextos
    if mes == 2 and dia == 29 and ((ano % 4 == 0) or (ano % 400 == 0)):
        data_nascimento = datetime(ano, mes, dia)
    else:
        data_nascimento = datetime(ano, mes, dia, 23, 59, 59)

    # Verificar signo
    for signo, intervalo in zip(signos, intervalos):
        if data_nascimento >= intervalo[0] and data_nascimento <= intervalo[1]:
            print(f"Seu signo é {signo}")
            break


def num_entre(n1, n2, msg='=====',tp=2):
    while True:
        num = number(tp, msg)
        if n1 <= num <= n2:
            return int(num);
            break
        print(f'Por favor, escolha valores entre {n1} e {n2}')

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
       dias_mes = {
            '1': 31,  # Janeiro
            '2': 29,  # Fevereiro
            '3': 31,  # Março
            '4': 30,  # Abril
            '5': 31,  # Maio
            '6': 30,  # Junho
            '7': 31,  # Julho
            '8': 31,  # Agosto
            '9': 30,  # Setembro
            '10': 31,  # Outubro
            '11': 30,  # Novembro
            '12': 31,  # Dezembro
        }
        if dia <= dias_mes[str(mes)]:
            print(f'Ok!')
            print(f'Considerando {dia}/{mes}/{ano}')
            break
        else:
            print(f'Data Inválida!')


    signos = ["Áries", "Touro", "Gêmeos", "Câncer", "Leão", "Virgem",
             "Libra", "Escorpião", "Sagitário", "Capricórnio", "Aquário", "Peixes"]
    intervalos = [
        ((21, 3), (19, 4)),  # Áries
        ((20, 4), (20, 5)),  # Touro
        ((21, 5), (20, 6)),  # Gêmeos
        ((21, 6), (22, 7)),  # Câncer
        ((23, 7), (22, 8)),  # Leão
        ((23, 8), (22, 9)),  # Virgem
        ((23, 9), (22, 10)),  # Libra
        ((23, 10), (21, 11)),  # Escorpião
        ((22, 11), (21, 12)),  # Sagitário
        ((22, 12), (19, 1)),  # Capricórnio
        ((20, 1), (18, 2)),  # Aquário
        ((19, 2), (20, 3)),  # Peixes (considera ano bissexto)
    ]

"""
Escreva um programa que peça ao usuário para inserir seu mês e dia de
nascimento. Em seguida, seu programa deve relatar o signo do zodı́aco do
usuário como parte de uma mensagem de saı́da apropriada.

"""


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
        "Áries": (datetime(ano, 3, 21), datetime(ano, 4, 19)),
        "Touro": (datetime(ano, 4, 20), datetime(ano, 5, 20)),
        "Gêmeos": (datetime(ano, 5, 21), datetime(ano, 6, 20)),
        "Câncer": (datetime(ano, 6, 21), datetime(ano, 7, 22)),
        "Leão": (datetime(ano, 7, 23), datetime(ano, 8, 22)),
        "Virgem": (datetime(ano, 8, 23), datetime(ano, 9, 22)),
        "Libra": (datetime(ano, 9, 23), datetime(ano, 10, 22)),
        "Escorpião": (datetime(ano, 10, 23), datetime(ano, 11, 21)),
        "Sagitário": (datetime(ano, 11, 22), datetime(ano, 12, 21)),
        "Capricórnio": (datetime(ano-1, 12, 22), datetime(ano, 1, 19)),
        "Aquário": (datetime(ano, 1, 20), datetime(ano, 2, 18)),
        "Peixes": (datetime(ano, 2, 19), datetime(ano, 3, 20))
    }

    def verificar_signo(data_usuario):
        for signo, (inicio, fim) in ranges_de_signos.items():
            if inicio <= data_usuario <= fim:
                return signo
        return "Signo não encontrado"  # Retorna caso a data não esteja em nenhum dos ranges

    # Exemplo de uso
    data_do_usuario = nascimento  # Substitua essa linha pela entrada real do usuário
    signo = verificar_signo(data_do_usuario)
    print("O signo é:", signo)



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
def num_entre(n1, n2, msg='=====',tp=2):
    while True:
        num = number(tp, msg)
        if n1 <= num <= n2:
            return int(num);
            break
        print(f'Por favor, escolha valores entre {n1} e {n2}')
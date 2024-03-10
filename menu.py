# Menu Principal
# </Gustavo Maciel>
# 07/03/2024
from alldata.utils import number, clear_term, num_entre
import alldata.entra_saida as entra
import alldata.condic as condi
import alldata.repeti as repi
print(f'''
LISTA DE EXERCÍCIOS
Prof. Dr. João Santana
</Cien. Gustavo Maciel>
{22*"="}''');
while True:
    print('''
[0] - Fechar Programa
[1] - Exercícios de Entrada e Saída
[2] - Exercícios de Condicionais
[3] - Exercícios de Laçoes de Repetição
[4] - Exercícios de Funções - Modularizações
[5] - Exercícios de Listas
[6] - Exercícios de Dicionários
[7] - Exercícios de Arquivos
[8] - Exercícios de Diversos
        ''')
    esco = num_entre(0, 8, 'Digite a opção desejada:')
    match esco:
        case 1:
            print('''
    [- EXERCÍCIOS DE ENTRADA E SAÍDA -]
    [0] - Voltar
    [1] - Média Aritmética das Notas
    [2] - Celsius x Fahrenheit
    [3] - Troca de Valores de Variáveis
    [4] - Área do Círculo
    [5] - Maior Área
    [6] - Área da Sala
    [7] - Piscina - Diversos
    [8] - Restaurante
                ''')
            esco = num_entre(0, 8, 'Digite a opção desejada: ')
            match esco:
                case 1: entra.media_aritmética_notas()
                case 2: entra.celsius_faren(); clear_term()
                case 3: entra.troca_valor(); clear_term()
                case 4: entra.area_circ(); clear_term()
                case 5: entra.area_dive(); clear_term()
                case 6: entra.area_sala(); clear_term()
                case 7: entra.piscina(); clear_term()
                case 8: entra.resto(); clear_term()
                case _: clear_term(False)
        case 2:
            print('''
[- EXECÍCIOS DE ESTRUTURAS CONDICIONAIS -]
[0] -  Voltar
[1] - Maior Número
[2] - Impar/Par
[3] - Contar Vogais
[4] - Aprovado/Reprovado
[5] - Mês por Extenso
[6] - Sim/Não
[7] - IMC
[8] - Signo
                ''')
            esco = num_entre(0, 8, 'Digite a opção desejada: ')
            match esco:
                case 1: condi.maior_num(); clear_term()
                case 2: condi.impar_par(); clear_term()
                case 3: condi.conta_vogais(); clear_term()
                case 4: condi.apro_repro(); clear_term()
                case 5: condi.mes_extenso(); clear_term()
                case 6: condi.sim_nao(); clear_term()
                case 7: condi.imc(); clear_term()
                case 8: condi.signo(); clear_term()
                case _: clear_term(False)
        case 3:
            print('''
[- EXECÍCIOS DE ESTRUTURAS DE REPETIÇÃO-]
[00] - Voltar
[01] - Fatorial
[02] - Tabuada
[03] - 
[04] - 
[05] - 
[06] - 
[07] - 
[08] - 
[09] - 
[10] - 
[11] - 
[12] - 
[13] - 
[14] - 
[15] - 
[16] - 
[17] - 
[18] - 
[19] - 
[20] - 
[21] - 
                ''')
            esco = num_entre(0,21)
            match esco:
                case 1: repi.fatorial()
                case 3: repi.tabu()
                case 3: pass
                case 4: pass
                case 5: pass
                case 6: pass
                case 7: pass
                case 8: pass
                case 9: pass
                case 10: pass
                case 11: pass
                case 12: pass
                case 13: pass
                case 14: pass
                case 15: pass
                case 16: pass
                case 17: pass
                case 18: pass
                case 19: pass
                case 20: pass
                case 21: pass
                case _: clear_term(False)
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            pass
        case _:
            clear_term(False)
            exit()




from alldata.utils import number, clear_term, num_entre, pega_maior_igual

def fatorial():
    number = pega_maior_igual(1)
    def fact(n1):
                if n1 == 1:
                    return 1;
                n1 = n1 * fact(n1-1)
                return n1;
    print(f'O fatorial de {number} é {fact(number)}')

def tabu():
    n = num_entre(1, 10, 'Digite um número: ')
    for c in range(11):
        beaty = ' ' if len(str(n*c)) < 2 else ''
        tabulation = ' ' if len(str(c)) <2 else ''
        print(f'{n} x {tabulation}{c} = {beaty}{n*c}')
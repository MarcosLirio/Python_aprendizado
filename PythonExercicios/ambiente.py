#Explicação:
help(print)
print(input.__doc__)

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Marcos Lírio
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')

contador(2, 10, 2)

help(contador)
def somar(a=0, b=0, c=0):
     """
     ->Faz a soma de três valores e mostra o resultado na tela.
     :param a: o primeiro valor
     :param b: o segundo valor
     :param c: o terceiro valor
     Função criada por Marcos Lírio aprendendo com o CursoemVideo
     """
     s = a + b + c
     return s

r1 = somar(3, 2)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2}, {r3}')
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#Programa Principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
#print(f'No programa principal, x vale {x}')

#Exercício de Prática:
def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

'''n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')'''

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par')

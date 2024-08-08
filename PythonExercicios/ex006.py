'''Crie um algoritmo que leia um número e mostre o seu dobro, triplo e
raiz quadrada'''

n = int(input('Digite um número: '))
print('O dobro de {} vale {}, \no triplo de {} vale {:.2f} \na raiz quadrada de {} vale {}'.format(n, (n*2), n, (n*3), n, (n **(1/2))))
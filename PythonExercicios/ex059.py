'''Crie um programa que leia dois
valores e mostre um menu como o
ao lado da tela:                            [ 1 ] Somar
Seu programa deverá realizar a              [ 2 ] multiplicar
operação solicitada em cada caso.           [ 3 ] maior
                                            [ 4 ] novos números
                                            [ 5 ] sair do programa'''

from time import sleep
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao <= 4:
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        sleep(0.5)
        soma = v1 + v2
        print('A soma entre {} + {} é {}'.format(v1, v2, soma))
        sleep(3)
        print('-=' * 30)
    elif opcao == 2:
        sleep(0.5)
        multiplicacao = v1 * v2
        print('O resultado de {} x {} é {}'.format(v1, v2, multiplicacao))
        sleep(3)
        print('-=' * 30)
    elif opcao == 3:
        sleep(0.5)
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('Entre {} e {} o maior valor é {}'.format(v1, v2, maior))
        sleep(3)
        print('-=' * 30)
    elif opcao == 4:
        sleep(1)
        print('Informe os números novamente: ')
        v1 = int(input('Digite o primeiro valor: '))
        v2 = int(input('Digite o segundo valor: '))
        print('-=' * 30)
    elif opcao == 5:
        print('Finalizando...')
        sleep(3)
        print('Fim do programa! Volte sempre!')
    else:
        while opcao not in (1,2,3,4,5):
            print('Opção inválida. Tente novamente')
            print('-=' * 30)
            print('[ 1 ] Somar')
            print('[ 2 ] Multiplicar')
            print('[ 3 ] Maior')
            print('[ 4 ] Novos números')
            print('[ 5 ] Sair do programa')
            opcao = int(input('Qual é a sua opção? '))
        print('Finalizando...')
        sleep(3)
        print('Fim do programa! Volte sempre!')
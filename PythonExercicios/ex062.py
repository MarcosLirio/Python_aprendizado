''''Melhore o desafio 061, perguntando
para o usuário se ele quer mostrar
mais alguns termos. O programa
encerra quando ele disser que quer
parar mostrando 0 termos'''

print('Gerador de PA')
print('-=-' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
continua = 10
while continua != 0:
    total = total + continua
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + razao
        cont += 1
    print('Pausa')
    continua = int(input('Quantos termos a mais deseja mostrar? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
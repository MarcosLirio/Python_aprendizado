'''Desenvolva um programa que leia o
primeiro termo de uma PA.
No final, mostre os 10 primeiros
termos dessa progressão'''

print('{:=^70}'.format(' 10 termos de uma PA '))
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, decimo + razao, razao):
    print(c,'->', end=' ')
print('ACABOU')
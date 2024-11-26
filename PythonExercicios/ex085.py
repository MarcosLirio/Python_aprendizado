''''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
 que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem
 crescente.
'''
#Minha Solução
numeros = list()
pares = list()
impares = list()
for n in range(0, 7):
    numeros.append(int(input(f'Digite o {n + 1}º número: ')))
    if numeros[n] % 2 == 0:
        pares.append(numeros[n])
    else:
        impares.append(numeros[n])
numeros.clear()
numeros.append(pares[:])
numeros.append(impares[:])
print(numeros)
print(f'Os números pares digitados foram: {pares}')
print(f'Os números ímpares digitados foram: {impares}')

#Solução do Professor:
'''
numeros = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º número: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('-=' * 30)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores Pares digitados foram {numeros[0]}')
print(f'Os valores Ímpares digitados foram {numeros[1]}')
'''
lanche = ('hambúrguer', 'suco', 'pizza', 'pudim', 'Batata Frita')
#Tuplas são imutáveis
#tuplas[1] = 'Refrigerante'
print(lanche[1]) #printa o lanche na posição da variável composta
print(len(lanche)) #printa o tamanho da variável composta lanche
#for comida in lanche:
#    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba!')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

#Lanche em ordem alfabética
print(sorted(lanche))
#concatenação de tuplas
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5))
#verificando o índice de um número em uma variável composta
print(c.index(8))
#verificando o índice quando têm mais de um número na variável composta
print(c.index(5,1))

pessoa = ('Gustavo', 39, 'M', 99.8)
print(pessoa)
del (pessoa) #deletando variável composta
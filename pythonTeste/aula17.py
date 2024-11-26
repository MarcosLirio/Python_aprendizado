num = [2, 5, 9, 1] #criação de uma lista
num[2] = 3 #alterando uma lista
num.append(7) #adicionando um valor ao último elemento da lista
num.sort() #Organizando a lista por ordem crescente/alfabética
num.sort(reverse=True) #Revertendo os valores da lista
num.insert(2, 0) #inserindo valores na lista informando a posição e o valor
num.pop() #Apagando o último elemento da lista
num.pop(2) #Apagando uma posição da lista com o comando pop
num.remove(2) #Removendo uma posição da lista com o comando remove
#tentando remover um número que não têm na lista
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista têm {len(num)} elementos') #printando o tamanho da lista

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}')
print('Cheguei ao final da lista')

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final do programa')

#Ligação de uma lista com a outra
a = [2, 3, 4, 7]
b = a
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#Cópia de uma lista pra outra
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
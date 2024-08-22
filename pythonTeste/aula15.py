
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma entre os números é {}'.format(s))
#Aprendendo a utilizar a formatação com F strings
print(f'A soma entre os números é {s}')

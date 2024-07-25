a = int(input('Digite o primeiro valor: '));
b = int(input('Digite o segundo valor: '));
c = int(input('digite o terceiro valor: '));
#Verificando quem é o menor:
menor = a
if b < a and b < c:
    menor = b;
if c < a and c < b:
    menor = c;
#Verificando quem é o maior:
maior = a
if b > a and b > c:
    maior = b;
if c > a and c > b:
    maior = c;
print('O menor valor foi: {}'.format(menor));
print('O maior valor é: {}'.format(maior));
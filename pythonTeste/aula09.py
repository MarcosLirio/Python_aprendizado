frase = '   Curso em Video Python   ';
#Fatiamento de String
print(frase[3]);
print(frase[3:13]);
print(frase[:13]);
print(frase[1:15:2]);
print(frase[1::2]);
print(frase[::2]);
print(frase.count('o'));
print(frase.upper().count('o'));
print(len(frase));
print(len(frase.strip()));

#Transformação de String
print(frase.replace('Python', 'Android'));               #Trocando palavras
print(frase);                                                        #Não salvou a alteração anterior
frase = frase.replace('Python', 'Android');              #Agora sim salvou a alteração na String

print('curso' in frase);
print(frase.find('video'));

print(frase.split());
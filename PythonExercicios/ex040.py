'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
-Média abaixo de 5.0: REPROVADO
-Média entre 5.0 e 6.9: RECUPERAÇÃO
-Média 7.0 ou superior: APROVADO'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Primeira nota: {:.1f} \nSegunda nota: {:.2f} \nMédia: {:.1f}\nREPROVADO! Terá que estudar tudo denovo'.format(nota1, nota2, media))
elif media > 5 and media <= 6.9:
    print('Primeira nota: {:.1f} \nSegunda nota: {:.2f} \nMédia: {:.1f} \nRECUPERAÇÃO! Terá que se esforçar um pouco mais para ser aprovado'.format(nota1, nota2, media))
else:
    print('Primeira nota: {:.1f} \nSegunda nota: {:.2f} \nMédia: {}\nPARABÉNS! Voçê foi aprovado'.format(nota1, nota2, media))
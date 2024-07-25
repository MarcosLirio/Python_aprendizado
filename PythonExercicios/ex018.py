from math import radians,sin,cos, tan;
ângulo = float(input('Digite o ângulo que voçê deseja: '));
seno = sin(radians(ângulo));
print('O ângulo {} têm o SENO de {:.2f}'.format(ângulo, seno));
cosseno = cos(radians(ângulo));
print('O ângulo de {} têm o COSSENO {:.2F}'.format(ângulo, cosseno));
tangente = tan(radians(ângulo));
print('O ângulo de {} têm a TANGENTE {:.2f}'.format(ângulo, tangente));
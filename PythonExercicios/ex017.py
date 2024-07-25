from math import hypot;
co = float(input('comprimento do cateto oposto: '));
ca = float(input('comprimento do cateto adjascente: '));
hi = hypot(co, ca);
print('A hipotenusa vai medir {:.2f}'.format(hi));
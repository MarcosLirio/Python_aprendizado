'''Cirei uma tupla preenchida com os 20     A) Os 5 primeiros.
primeiros colocados da tabela do            B) Os 4 últimos colocados
Campeonato Brasileirão de Futebol,          C) Times em ordem alfabética
na ordem de colocação. Depois               D) Em que posição está o
mostre:                                        time do São Paulo FC'''

times = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Flamengo', 'Cruzeiro',
         'São Paulo', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Internacional',
         'Bragantino', 'Athletico-PR', 'Criciúma', 'Juventude', 'Grêmio',
         'Fluminense', 'Corinthians', 'EC Vitória', 'Cuiabá', 'Atlético-GO')
print('-=' * 50)
print(f'Lista de times do Campeonato Brasileiro: \n{times}')
print('-=' * 50)
print(f'Os 5 primeiros colocados são \n{times[0:5]}')
print('-=' * 50)
print(f'Os 4 últimos que estão na lantera da zona de rebaixamento são: \n{times[-4:]}')
print('-=' * 50)
print(f'Lista dos times em ordem alfabética: \n{sorted(times)}')
print('-=' * 50)
print(f'O São Paulo está na {times.index('São Paulo') + 1}ª posição')
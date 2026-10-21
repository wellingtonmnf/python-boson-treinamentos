import random

for cont_ext in range(1,6):
    print(f'\nRodada: {cont_ext}')
    for cont_int in range(5,0,-1):
        print(f'Valor: {cont_int}')

print('Fim dos laços de repetição')

for a in range(1,6):
    print(f'Conjunto: {a}')
    for b in range(5):
        num = random.randint(1,100)
        print(f'Valor: {num}')

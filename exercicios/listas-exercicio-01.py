bebidas = list()

for i in range(5):
    bebida = input('Digite uma bebida: ')
    bebidas.append(bebida)

bebidas.sort()
print(f'Bebidas escolhidas: \n')
for bebida in bebidas:
    print(bebida)

print('Saúde!')

import random

valor = random.randint(1, 20)
print(valor)

print('Gerar cinco números aleatórios entre 1 e 50: \n')
for c in range(5):
    n = random.randint(1, 50)
    print(f'Número gerado: {n}')

valor = random.random()  # Números aleatórios de ponto flutuante
print(f'Número gerado: {round(valor * 10, 2)}')  # areedondando o valor apra o número de casas decimais especificadas

numero = random.uniform(1, 100)
print(f'Número: {round(numero, 4)}')

lista = [2, 4, 6, 9, 10, 13, 14, 16, 18, 20, 21, 27, 33]
# Escolhe um valor aleatório de um conjunto ou lista
n1 = random.choice(lista)
print(f'Número escolhido: {n1}')

# Escolhe vários valores aleatórios de um conjunto ou lista
n2 = random.sample(lista, 3)
print(f'Números escolhidos: {n2}')

print(f'Exibir a lista original: {lista}')
# Embaralha uma lista e não retorna nada. Ele muda o objeto original
random.shuffle(lista)
print(f'Lista embaralhada: {lista}')

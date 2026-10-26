# Funções Lambda (anônimas)
from typing import Protocol

# Sintaxe
# lambda argumentos: expressão

quadrado = lambda x: x ** 2

for i in range(1, 11):
    print(quadrado(i))

par = lambda x: x % 2 == 0
print(par(9))

f_c = lambda f: (f - 32) * 5 / 9
print(f_c(212))

# Função map()
# Sintaxe

# map(função, iterável)
# A função map retorna objetos do tipo map. Necessário fazer casting

num = [1, 2, 3, 4, 5, 6, 7, 8]
dobro = list(map(lambda x: x * 2, num))
print(dobro)

palavras = 'Python é uma linguagem de programação'.split()
maiusculas = list(map(str.upper, palavras))
print(maiusculas)


# Função filter()
# Sintaxe:

# filter(função, sequência)

def numeros_pares(n):
    return n % 2 == 0


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

num_par = list(filter(numeros_pares, numeros))
print(num_par)

num_impar = list(filter(lambda x: x % 2 != 0, numeros))
print(num_impar)

# Função reduce()
# Sintaxe
# reduce(função, sequência, valor_inicial)

from functools import reduce


def mult(x, y):
    return x * y


numeros2 = [1, 2, 3, 4, 5, 6]

total = reduce(mult, numeros2)
print(total)

# Soma cumulativa dos quadrados de valores, usando expressão lambda
# ((1² + 2²)² + 3²)² + 4²

numeros3 = [1, 2, 3, 4]

total2 = reduce(lambda x, y: x ** 2 + y ** 2, numeros3)
print(total2)

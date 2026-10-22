# import math # import genérico
# from math import sqrt, sin # import de funções específicas
# from math import * # import universal (pouco recomendado, por questões de
# possíveis conflitos de nomenclatura com outras funções de outros módulos)

import math as m # usar alaises ajuda a conciliar possíveis conflitos e
# organiza melhor o código

print(m.sqrt(9))

import mod_func as mf
import numpy as np

if __name__ == '__main__':
    mf.mensagem()

    num = int(input('Digite um número inteiro: '))

    print(f'\nCalcular fatorial do número: ')
    fat = mf.fatorial(num)
    print(f' {num}! = {fat}')

    print(f'\nCalcular sequência de Fibonacci com {num} termos:', end=' ')
    fib = mf.fibonacci(num)
    print(f'{fib}')

L = np.array([1,2,3,4,5,6,7,8,9])
print(L)

from math import sqrt


# Criação de um tipo de exceção própria usando a classe Exception
class NumeroNegativoError(Exception):
    def __init__(self):
        pass


if __name__ == '__main__':

    while True:
        try:
            num = int(input('Digite um número POSITIVO: '))
            if num < 0:
                raise NumeroNegativoError
        # Cada exceção deve ser tratara em uma linha separada
        except NumeroNegativoError:
            print(f'Foi fornecido um número NEGATIVO!')
        except ValueError:
            print('Ocorreu um erro ao ler o valor. Tente novamente.')
        else:
            break

    print(f'A raiz quadrada de {num} é igual a {sqrt(num)}')
    print(f'\nFim do cálculo')

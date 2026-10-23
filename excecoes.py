# Exceção é um objeto que representa um erro ao executar o programa
# Blocos try... except

def divisao(k, j):
    return round(k / j, 2)


if __name__ == '__main__':

    while True:
        try:
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite outro número: '))
            break
        except ValueError:
            print('Ocorreu um erro ao ler o valor. Tente novamente.')

    # Tenta executar um bloco de código onde se acredita que possa haver exceção
    try:
        r = divisao(n1, n2)
    # Cada exceção deve ser tratada em uma linha diferente
    except ZeroDivisionError:
        print(f'Não é possível dividir por zero!')
    except:
        print(f'Ocorreu um erro desconhecido')
    # Executa caso não haja exceção
    else:
        print(f'Resultado: {r}')
    # Executa independente de haver exceção ou não
    finally:
        print(f'\nFim do cálculo')

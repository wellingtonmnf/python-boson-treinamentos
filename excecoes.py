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

    try:
        r = divisao(n1, n2)
    except ZeroDivisionError:
        print(f'Não é possível dividir por zero!')
    except:
        print(f'Ocorreu um erro desconhecido')
    else:
        print(f'Resultado: {r}')
    finally:
        print(f'\nFim do cálculo')

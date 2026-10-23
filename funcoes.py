# Funções
# Modularização, Reuso de Código, Legibilidade

# # Sintaxe
# def <nome_funcao>([argumentos]):
#     <instrucoes>

def mensagem():
    print('Bóson Treinamentos em Tecnologia')
    print('Curso Completo de Python')


mensagem()


# Função com argumentos

def soma(a, b):
    print(a + b)


soma(12, 7)


def multiplicar(x, y):
    return x * y


a = 5
b = 8
c = multiplicar(5, 8)
print(f'O produto de {a} vezes {b} é {c}')


def dividir(k, j):
    if j != 0:
        return k / j
    else:
        return 'Impossível dividir por zero!'


def quadrado(valor):
    quadrados = []
    for x in valor:
        quadrados.append(x ** 2)
    return quadrados


if __name__ == '__main__':
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    valores = [2,5,7,9,12]

    resultado = dividir(a, b)
    print(f'{a} dividido por {b} é igual a {resultado}')

    resultados = quadrado(valores)
    for g in resultados:
        print(g)

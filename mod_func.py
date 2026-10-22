# Módulo com funções variadas

# Função que exibe mensagem de boas-vindas:
def mensagem():
    print('Bóson Treinamentos em Tecnologia!\n')


# Função para cálculo do fatorial de um número:
def fatorial(numero):
    fat = numero
    if numero == 0:
        print(f'O fatorial de {numero} é {fat}')
    elif numero > 0:
        for cont in range(1, numero):
            fat *= cont
    else:
        fat = None
        print('Digite um valor maior ou igual a zero!')
    return fat


# Função para cálculo da sequência de Fibonacci de um número:
def fibonacci(numero):
    if numero <= 0:
        print('Digite um valor maior ou igual a zero!')
        return []
    if numero == 1:
        return [0]
    sequencia = [0, 1]
    while len(sequencia) < numero:
        # A lista adiciona o número resultante da adição entre o último e o penúltimo número da lista, a cada iteração
        sequencia.append(sequencia[-1] + sequencia[-2]) # Pega a última e a penúltima posição da lista, sempre
    return sequencia

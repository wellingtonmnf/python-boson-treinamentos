# Escopo global e local

var_global = 'Curso Completo de Python'


def escreve_texto():
    var_global = 'Bancos de Dados com SQL'  # Sombreamento: criou-se uma nova variável local que predomina em seu escopo
    var_local = 'Wellington'
    print(f'Variável Global: {var_global}')
    print(f'Variável Local: {var_local}')


def escrever():
    global var_global  # Especifica que será feito o uso de uma variável global
    var_global = 'Bancos de Dados com SQL'  # A atribuição/alteração do valor PRECISA SER DEPOIS da especificaçaõ do escopo
    var_local = 'Wellington'
    print(f'Variável Global: {var_global}')
    print(f'Variável Local: {var_local}')


if __name__ == '__main__':
    print(f'Executar a função escreve_texto()')
    escreve_texto()

    print('Tentar acessar as variáveis diretamente')
    print(f'Variável Global: {var_global}')
    # print(f'Variável Local: {var_local}') # Variáveis locais são inacessíveis fora de seu escopo (função, no caso)

    print('Executar a função escrever()')
    escrever()

    print('Tentar acessar as variáveis diretamente')
    print(f'Variável Global: {var_global}')

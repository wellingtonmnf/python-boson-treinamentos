# Sintaxe:

# print(objetos, argumentos)

mensagem = 'Função print()'
print(mensagem) # Imprimindo variável
print('Aula de Python') # Imprimindo string diretamente

nome = 'Wellington Morais'
canal = 'Bóson Treinamentos'
print('Bóson Treinamentos - ', nome)
print(canal,' - ',nome)

nome2 =  input('Digite seu nome: ')
msg = 'Olá, ' + nome2 + '! Bem vindo(a) ao curso de Python!'
print(msg)
print('Outro texto') # A função print quebra a linha automaticamene

print('Imprime a mensagem e muda de linha')
print('Imprime a mensagem e permanece na linha. ', end='') # Emenda a linha do comando posterior
print('Continuo na mesma linha!')

nome3 = 'Maria'
idade = 30
msg_formatada = 'O nome é {0} e a idade é {1} anos'.format(nome3, idade) # É possível posicionar os argumentos da função
print(msg_formatada)

nome4 = 'Milena'
peso = 58.50
msg2 = f'Olá, meu nome é {nome4} e eu peso {peso} kg.'
print(msg2)

a = 10
b = 5
resultado = f'A soma de {a} com {b} é igual a {a+b}' # É possível usar expressos em uma fstring
print(resultado)

valor = 125.579637
print(f'O valor é {valor}')
print(f'O valor é {valor:.2f}') # É possível formatar o valor dentro de uma fstring
print(f'O valor é \'{valor:.2f}\'') # É possível formatar o valor com caracteres de espaço

nome5 = 'João'
idade2 = 32
print(f'Nome: {nome5}\tIdade: {idade2}') # Caractere de escape par tabulação

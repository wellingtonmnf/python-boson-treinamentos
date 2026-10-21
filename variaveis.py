nome_usuario = 'Wellington'
print(nome_usuario)

media = 0

n1 = n2 = n3 = n4 = 0.0

nome, idade = 'Wellington', 36

estado = True

# Função type()

print(type(media))
print(type(n2))
print(type(nome))
print(type(estado))
print(type(1+2j)) # número complexo (usado p.e. em engenharia elétrica)

# Função isinstance() para saber o tipo (classe) de uma variável

a = 10
b = 'Sol'

print(isinstance(a, int))
print(isinstance(b, str))
print(isinstance(a, float))
print(isinstance(a, (int, float))) # pode inserir mais de um tipo para checagem

a = 40 # reatribuição de valor
c = 3
r = a * c
print(r)

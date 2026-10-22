# Set

planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(planeta_anao)
print(len(planeta_anao))
print('Ceres' in planeta_anao)
print('Lua' in planeta_anao)
print('Lua' not in planeta_anao)

for astro in planeta_anao:
    print(astro.upper(), end=' ')

astros = ['Lua', 'Vênus', 'Sirius', 'Marte', 'Lua']
print('\n', astros, end=' ')

astro_set = set(astros)
print('\n', astro_set, end=' ')

astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Io'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Cometa de Halley'}
print('\n', astros1 == astros2)
print('\n', astros1 != astros2)
print('\n', astros1 | astros2) # Usando '|' podemos fazer a união entre conjuntos
print(astros1.union(astros2)) # Podemos fazer a mesma coisa usando .union()
print('\n', astros1 & astros2) # Usando '&' podemos fazer a intersecção entre conjuntos
print(astros1.intersection(astros2)) # Podemos fazer a mesma coisa usando .intersection()
print('\n', astros1 ^ astros2) # Usando '^' podemos checar a difereça simétrica entre conjuntos
print(astros1.symmetric_difference(astros2)) # Podemos fazer a mesma coisa usando .intersection()

astros1.add('Urano')
astros1.add('Sol')
astros1.remove('Io')
# astros1.remove('Plutão') # Tentar remover algo que não existe no conjunto dará erro
astros1.discard('Lua') # Usar .discard( ão resulta em erro caso o elemento não exista no conjunto)
astros1.pop() # remove um elemento arbitrário do conjunto
print(astros1)
astros1.clear()
print(astros1)

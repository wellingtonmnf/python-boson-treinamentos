curso = 'Curso de Python'
aluno = 'Wellington'
letra = aluno[2]
print(letra)
print(len(aluno))
print(curso + ' com ' + aluno)

frase = 'Vamos aprender Python hoje.'
palavras = frase.split()
print(palavras)
print(palavras[1])

for letra in frase:
    print(letra)

print(frase[0:5])
print(frase[6:15])
print(frase[7:19])
print(frase[-3:])

# email = input('Digite seu endereço de e-mail: ')
# arroba = email.find('@')
# print(arroba)
#
# usuario = email[:arroba]
# dominio = email[arroba+1:]
# print(usuario)
# print(dominio)

produtos = 'carbonato de sódio e óxido de zinco'
print('sódio' in produtos)
print('magnésio' in produtos)
print('magnésio' not in produtos)

item = 'hipoclorito'
pos = item.find('clor')
print(pos)  # Retorna a posição inicial da substring
pos = item.find('flu')
print(pos)  # Caso não exista, ele responde -1

objeto_celeste = 'galáxia esPiral M31'
print(objeto_celeste)
print(objeto_celeste.upper())  # Tudo maiúsculo
print(objeto_celeste.lower())  # Tudo minúsculo
print(objeto_celeste.capitalize())  # Primeira letra da string em maiúsculo
print(objeto_celeste.title())  # Primeira letra de cada palavra fica em maiúsculo

suplemento = 'cloreto de magnésio'
novo_suplemento = suplemento.replace('magnésio', 'zinco')
print(suplemento)
print(novo_suplemento)

frase2 = '         Ômega 3 é bom para a saúde       '
print(frase2)
print(frase2.lstrip())
print(frase2.rstrip())
print(frase2.strip())

fruta = 'Abacate'
print(fruta)
print(fruta.rjust(20))
print(fruta.center(20))
print(fruta.ljust(20, '-'))
print(fruta.center(20, '-'))

p = 'Bóson Treinamentos'
print(p.startswith('Bó'))
print(p.startswith('b'))
print(p.endswith('s'))
print(p.endswith('o'))

# Docstrings
texto = """"
Docstring é uma espécie de documentação 
que podemos inserir dentro de um módulo, 
função ou classe no Python, entre outros locais.
    Respeita deslocamento de texto e é multilinhas
"""

print(texto)

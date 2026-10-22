# Lista: representa uma sequência de valores armazenados na memória

# Sintaxe: nome_lista = [valores]

notas = [5, 7, 8, 6, 9]
print(notas)

n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6, 3, 0, 12, 11]
valores = n1 + n2
print(valores)
print(type(valores))

print(valores[0])  # Acessa a primeira posição
print(valores[-1])  # Acessa a última posição
print(valores[-2])  # Acessa a penúltima posição

valores[0] = 9  # Atribuir valor a uma posição específica
print(valores[0])

# Slice (fatiamento) de listas
print(valores[0:2])
print(valores[0:])
print(valores[:4])
print(valores[3:3])
print(valores[3:4])
print(valores[-2:])
print(valores[:-3])
print(valores[-4:10])

print(len(valores))  # Mostra a quantidade de itens da lista
print(sorted(valores))  # Ordena a lista, sem modificar o objeto original
print(sorted(valores, reverse=True))  # Ordena a lista de forma reversa, sem modificar o objeto original

print(sum(valores))  # Soma os valores da lista
print(min(valores))  # Pega o valor mínimo da lista
print(max(valores))  # Pega o valor máximo da lista

valores.append(13)  # Acrescenta um novo valor ao final da lista
print(valores)
valores.pop()  # Remove o último valor ao final da lista
print(valores)
valores.pop(3)  # Remove o valor indicado na posição da lista
print(valores)
valores.insert(3, 21)  # Insere um valor na posição especificada na lista
print(valores)
valores.remove(6)  # Remove a primeira ocorrência do valor na lista
print(valores)
print(12 in valores)  # Checa a existência de determinado valor na lista
print(17 in valores)

planetas = ['Mercúrio', 'Vênus', 'Marte', 'Saturno', 'Urano', 'Netuno']
for planeta in planetas:
    print(planeta)

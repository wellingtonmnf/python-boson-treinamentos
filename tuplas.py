# Tuplas são imutáveis

tupla = (2, 4, 6, 7, 9)
# tupla[1] = 5 # Uma tupla não suporta uma nova atribuição a seus itens
print(tupla)

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
t1 = (5, 2, 6, 8, 4, 5, 6, 4, 4, 0, 12, 22, 3, 4, 5)

print(halogenios)
print(len(halogenios))
print(halogenios[3])
print(halogenios[-1])
print(elementos)
print(t1.count(5))
print(t1.count(3))
print(halogenios[0:2])
print(halogenios[:3])
print(halogenios[-2:])
print('Cl' in halogenios)
print('Fe' in halogenios)
print(sum(t1))
print(min(t1))
print(max(t1))

# Operações não disponíveis em tuplas: .sort(), .appedn(), .reverse(), .pop()...

for elemento in elementos:
    print(f'Elemento químico: {elemento}')

grupo17 = list(halogenios)
grupo17[0] = 'H'
print(grupo17)

grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)
print(alcalinos)
print(type(alcalinos))

print(sorted(alcalinos)) # O metodo sorted() ordena sem alterar o objeto original

# Para 'ordenar' uma tupla, criar uma nova tubla atribuindo o valor de sorted(tupla_original)
alcalinos_ordenados = sorted(alcalinos)
print(alcalinos_ordenados)

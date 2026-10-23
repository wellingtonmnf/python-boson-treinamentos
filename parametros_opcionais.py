def contar(num=11, caractere='+'):  # Usa a definição caso não seja passado nenhum parâmetro
    for i in range(1, num):
        print(caractere)


# Parâmetros obrigatórios devem vir SEMPRE antes do não obrigatórios
def escrever(caractere, num=5):
    for i in range(1, num):
        print(caractere)


x, y, z = 5, 6, 3


def soma_mult(a, b, c=0):
    if c == 0:
        return a * b
    else:
        return a + b + c


if __name__ == '__main__':
    contar()
    contar(5, '-')
    contar(caractere='&')  # Para usar parâmetro específico que não segue a ordem declarada
    contar(num=7)  # Pode especificar o parâmetro, ams não é obrigatório
    contar(7)  # Passando apenas um parâmetro, na ordem
    escrever('~')
    escrever('#', 3)
    escrever(num=3, caractere='#')  # É possível nomear e assim, também, alterar a ordem de declaração

    res = soma_mult(x,y)
    print(res)
    res = soma_mult(x,y,z)
    print(res)

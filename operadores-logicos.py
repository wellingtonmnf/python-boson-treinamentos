# Operador AND
idade = 15
altura = 1.75

resultado = (idade >= 18) and (altura >= 1.70)
msg = 'Pode participar do evento? ' + str(resultado)

print(msg)

# Operador OR
# Programa de disparo de alarme
porta = 'f' #fechada
janela = 'a' #aberta

alarme = (porta == 'a') or (janela == 'a')
msg2 = 'Alarme disparado? ' + str(alarme)
print(msg2)

# Operador NOT
tem_dinheiro = False
tem_dinheiro = not tem_dinheiro
msg3 = 'Tem dinheiro? ' + str(tem_dinheiro)
print(msg3)

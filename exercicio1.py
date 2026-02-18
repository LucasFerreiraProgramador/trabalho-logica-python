#O exercício foi resolvido com um loop while True
while True:
    #Dados de entrada: nome e peso
    nome = input('Qual o nome do lutador? ')
    peso = float(input('Qual é o peso do lutador? '))

    #Utilizei if para verificação do peso
    if peso <= 0: #Se o if for menor ou igual a zero da erro
        print('[ERRO] Peso invalido. Digite um peso maior que 0')
        continue
    if peso < 65:
        print('O lutador {} pesa {} Kg e se enquadra na categoria Pena'.format(nome, peso))
        # Caso o if for verdadeiro, é executado um mini "teste" para
        # saber se o usuário quer continuar ou não, se digitar 'Y'
        # o loop volta para o início, se digitar 'N' ou outra fetra o teste finaliza
        teste = input('Quer continuar? (Y/N) ')
        if (teste == 'Y'):
            continue
        else:
            break
    #Todos os outros if são iguais, só muda os parâmetros de comparação e o print
    if peso >= 65 and peso < 72:
        print('O lutador {} pesa {} Kg e se enquadra na categoria Leve'.format(nome, peso))
        teste = input('Quer continuar? (Y/N) ')
        if (teste == 'Y'):
            continue
        else:
            break
    if peso >= 72 and peso < 79:
        print('O lutador {} pesa {} Kg e se enquadra na categoria Ligeiro'.format(nome, peso))
        teste = input('Quer continuar? (Y/N) ')
        if (teste == 'Y'):
            continue
        else:
            break
    if peso >= 79 and peso < 86:
        print('O lutador {} pesa {} Kg e se enquadra na categoria Meio-médio'.format(nome, peso))
        teste = input('Quer continuar? (Y/N) ')
        if (teste == 'Y'):
            continue
        else:
            break
    if peso >= 86 and peso < 93:
        print('O lutador {} pesa {} Kg e se enquadra na categoria Médio'.format(nome, peso))
        teste = input('Quer continuar? (Y/N) ')
        if (teste == 'Y'):
            continue
        else:
            break
    if peso >= 93 and peso < 100:
        print('O lutador {} pesa {} Kg e se enquadra na categoria Meio-pesado'.format(nome, peso))
        teste = input('Quer continuar? (Y/N) ')
        if (teste == 'Y'):
            continue
        else:
            break
    if peso >= 100:
        print('O lutador {} pesa {} Kg e se enquadra na categoria Pesado'.format(nome, peso))
        teste = input('Quer continuar? (Y/N) ')
        if (teste == 'Y'):
            continue
        else:
            break
# Se no teste o usuário digite 'N' ou outro caractere,
# o programa é finalizado encerrando o loop
print('Fim do programa.')

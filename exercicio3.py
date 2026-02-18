# Número de quantos alunos vão ser cadastrados
numeroAlunos = int(input('Quantos alunos quer cadastrar? '))

notasAlunos = {}
todosAlunos = []
# Usei um for que se repete na quantidade de vezes no número de alunos
for i in range(numeroAlunos):
    notasAlunos['aluno'] = input('Qual o nome do aluno? ')  # Pegando o nome do aluno
    n1 = float(input('Qual a 1° nota? '))                   # Pegando as notas
    n2 = float(input('Qual a 2° nota? '))
    n3 = float(input('Qual a 3° nota? '))
    n4 = float(input('Qual a 4° nota? '))
    notasAlunos['notas'] = n1, n2, n3, n4                  # Atribuindo todas as notas
    media = (n1 + n2 + n3 + n4) / 4                        # Calculando a média

    # if para aprovado se a média for maior ou igual a 7
    # if para reprovado se a média for menor a 7
    if media >= 7:
        notasAlunos['status'] = 'Aprovado'
    if media < 7:
        notasAlunos['status'] = 'Reprovado'
    # Fazendo uma cópia dos dados e adicionando ao dicionário todosAlunos
    todosAlunos.append(notasAlunos.copy())

# Print na tela do resultado
print('_' * 30)
print('Notas dos alunos:')
print('_' * 30)
# Dois for uma para a lista e o outro para o dicionário
for e in todosAlunos:
    for i,j in e.items():
        print('{} = {}'.format(i, j))
    print('_' * 30)


# Primeiro pequei quantos números o usuária vai cadastrar
numeroTelefone = int(input('Quantos números quer cadastrar? '))

# Depois criei um dicionário e uma lista
listaTelefonica = {}
todosContatos = []

# Fiz o formulário com um for que se repete conforme o usuário colocou
for i in range(numeroTelefone):
    listaTelefonica['nome'] = input('Digite o nome: ')      # Adiciona o nome
    if listaTelefonica['nome'] == '':                       # Se for iqual a '' o programa para
        print('!!! [ERRO] Nome não foi preenchido !!! ')
        break
    listaTelefonica['idade'] = int(input('Digite a idade: '))        # Adiciona idade
    listaTelefonica['telefone'] = int(input('Digite o número: '))    # Adiciona telefone

    todosContatos.append(listaTelefonica.copy())     # Copia todos os dados e joga dentro de todosContatos

#Criei uma fonção que retorna o nome
def ordemAufabtica(e):
  return e['nome']

#Ordenei em ordem alfabetica com o sort()
todosContatos.sort(key=ordemAufabtica)
print('_' * 30)
print('Contatos em ordem alfabetca:')
print('_' * 30)

# Exibi na tela os contatos em ordem alfabética com
# Dois for uma para a lista e o outro para o dicionário
for e in todosContatos:
    for i,j in e.items():
        print('{} = {}'.format(i, j))
    print('_' * 30)

# Criei duas listas para separar o todosContatos
# Uma para contatos maiores de idade e para menores de idade
contatosDeMaior = []
contatosDeMenor = []
# Fiz a filtragem com um for
for i in range(numeroTelefone):
    if todosContatos[i]['idade'] >= 18:
        contatosDeMaior.append(todosContatos[i])
        # Se for maior de idade é adicionado a lista contatosDeMaior
    if todosContatos[i]['idade'] < 18:
        contatosDeMenor.append(todosContatos[i])
        # Se for menores de idade é adicionado a lista contatosDeMenor

# Exibi na tela os resultados filtrados

print('#' * 30)

# Resultados maiores de idade
print('_' * 30)
print('Maiores de idade:')
print('_' * 30)
for e in contatosDeMaior:
    for i,j in e.items():
        print('{} = {}'.format(i, j))
    print('_' * 30)

# Resultados menores de idade
print('_' * 30)
print('Menores de idade: ')
print('_' * 30)
for e in contatosDeMenor:
    for i,j in e.items():
        print('{} = {}'.format(i, j))
    print('_' * 30)

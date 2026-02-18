# Criei uma função para receber o parâmetro e validá-lo ao mesmo tempo
def testeCodigoValido():
    while True:
        codigoProdutos = int(input('Digite o código do produto entre 10000 e 30000:'))
        # Se o código for menor que 10000 e maior que 30000 ele retorna: código invalido
        # e faz o usuário digitar novamente
        if(codigoProdutos < 10000):
            print('[CODIGO INVALIDO] Tente de novo! ')
            continue
        if(codigoProdutos > 30000):
            print('[CODIGO INVALIDO] Tente de novo!')
            continue
        else:
        # Se for dentro do intervalo o número é retornado
            return codigoProdutos

# Depois de validar o número, eu converti em uma string
# E atribui a string em uma lista
numeroValido = str(testeCodigoValido())
listaDeCodigo = [numeroValido]

# Com o número em formato  de lista comecei a fazer os cálculos e armazenar em funções
def soma1():
    # Seleciono o número específico dentro da lista, faço o cálculo e retorno o resultado
    n1 = int(listaDeCodigo[0][0])
    resultado = n1 * 2
    return resultado
def soma2():
    n1 = int(listaDeCodigo[0][1])
    resultado = n1 * 3
    return resultado
def soma3():
    n1 = int(listaDeCodigo[0][2])
    resultado = n1 * 4
    return resultado
def soma4():
    n1 = int(listaDeCodigo[0][3])
    resultado = n1 * 5
    return resultado
def soma5():
    n1 = int(listaDeCodigo[0][4])
    resultado = n1 * 6
    return resultado

# Função para pegar o resultado da divisão de todos os números
def resultado():
    somaTodos = soma1() + soma2() + soma3() + soma4() + soma5()
    resultadoDivisao = somaTodos % 7
    return resultadoDivisao

# E retornei o resultado em uma string
resultadoString = str(resultado())

# Imprimindo na tela
print('{}-{}'.format(numeroValido, resultadoString))

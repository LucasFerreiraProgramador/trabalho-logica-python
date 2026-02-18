frase = input("Digite a frase: ")
fraseArray = list(frase)

chave = int(input("Digite os dois ultimos numeros do seu RU: "))
chaveBit = format(chave, "08b")


tamanho = len(fraseArray)

listaAscii = []
for x in range(tamanho):
    listaAscii.append(ord(fraseArray[x])) #string para ascii

binario = []
for x in range(tamanho):
    binario.append(format(listaAscii[x], "08b")) #scii para binario

cifra = []
teste = []
#Criptografando a frase com a chave
for x in range(tamanho):
    teste.clear()
    for i in range(8):
        if (binario[x][i] == chaveBit[i]):
            teste.append('0')
        else:
            teste.append('1')
    cifra.append(teste)

descripto = []
teste2 = []
#Descriotografado a frase com a chave
for x in range(tamanho):
    teste2.clear()
    for i in range(8):
        if (cifra[x][i] == chaveBit[i]):
            teste2.append('0')
        else:
            teste2.append('1')
    descripto.append(teste2)

#converteAscii = []
#for x in range(tamanho):
#    converteAscii.append(chr(listaAscii[x]))  #de ascii para string


print("Frase inicial:")
print(fraseArray)
print("---------")
print("chaveBit")
print(chaveBit)
print("---------")
print("De ascii para binario")
print(binario)
print("---------")
print("Cifra")
print(cifra)
for x in range(tamanho):
    print(cifra[x])
print("---------")
print("Descriptografado")
print(descripto)
for x in range(tamanho):
    print(descripto[x])


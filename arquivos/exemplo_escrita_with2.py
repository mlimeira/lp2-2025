lista = []
with open('exemplo.txt', 'r+') as arquivo:
    while True:
        linha = arquivo.readline()
        if linha == '':
            break
        nova_linha = linha[:-1]+'Vou tirar 10 em LP2\n' #Colocando conteúdo em novas linhas
        lista.append(nova_linha)
with open('exemplo.txt', 'w') as novo_arquivo: #Reescrevendo em um novo contexto
    for i in lista:
        novo_arquivo.write(i)

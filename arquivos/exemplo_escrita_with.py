with open('exemplo.txt', 'r+') as arquivo:
    lista = []
    while True:
        linha = arquivo.readline()
        if linha == '':
            break
        nova_linha = linha[:-1]+'Vou tirar 10 em LP2\n' #Colocando conteúdo em novas linhas
        lista.append(nova_linha)

    for i in lista:
        arquivo.write(i)

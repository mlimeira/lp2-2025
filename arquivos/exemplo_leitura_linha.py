arquivo = open('exemplo.txt', 'r')
while True:
    conteudo = arquivo.readline()
    if conteudo == '':
        break
    print(conteudo, end='')
arquivo.close()
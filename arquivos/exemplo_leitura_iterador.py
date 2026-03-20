arquivo = open('exemplo.txt', 'r')
for linha in arquivo:
    print(linha, end='')
arquivo.close()
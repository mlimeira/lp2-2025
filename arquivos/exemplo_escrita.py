arquivo = open('exemplo.txt', 'w', encoding='utf-8')
for i in range(1, 11):
    arquivo.write(f'Teste {i};\n')
arquivo.close()
print('Arquivo criado com sucesso')
def geradora():
    for i in range(1,11):
        yield i

iterador = geradora()
#iterando 2 vezes
print(f'Fora do laço: {next(iterador)}')
#print(next(iterador))
#reiniciou o iterador
#c
#Iterando em toda a estrutura
while True:
    try:
        print(f'Dentro do laço: {next(iterador)}')
    except:
        print('Final do iterador')
        break

iterador = geradora()
lista = list(iterador)
print(lista)
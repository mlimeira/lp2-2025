#Função geradora
def imprimir():
    i = 0
    print('linha 1')
    i += 1
    yield i
    print('linha 2')
    i += 1
    yield i
    #return True

gerador = imprimir()
print(type(gerador))
retorno = next(gerador)
print(retorno)
retorno = next(gerador)
print(retorno)

#StopIteration
#retorno = next(gerador)
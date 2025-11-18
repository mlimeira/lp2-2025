obj_it = iter('123')
print(type(obj_it))
print(next(obj_it))
print(next(obj_it))
print(next(obj_it))
print(next(obj_it))
print(next(obj_it))
for s in obj_it:
    print(s)

doces = ['doce de mamão', 'pudim', 'brigadeiro']
doces_it = enumerate(doces)
print(next(doces_it))
for indice, valor in doces_it:
    print(indice, valor)
#As iterações consumiram o conteúdo do iterador
#Repovoar os objeto iteradores
obj_it = iter('123')
doces_it = enumerate(doces)
mapeamento = zip(obj_it, doces_it)
#print(next(mapeamento))
for x, y in mapeamento:
    print(x,y)
    #print(f'{x}:{y[1]}')

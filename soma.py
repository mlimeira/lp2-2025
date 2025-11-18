#Soma com valores default
def soma(x=0,y=0, z=0):
    return x+y

#Soma com quantidade arbitrária de parâmetros
def soma_arbitraria(*args):
    resultado = 0
    for x in args:
        resultado += x
    return resultado

print(soma(10,20))
print(soma_arbitraria(10,30,40,50,60,70,80,90))

soma_anonima = lambda x,y : x+y
print(soma_anonima(6,7))
soma_anonima_arbitraria = lambda *args : sum(args)
print(soma_anonima_arbitraria(6,7,10,20,40,50))
funcao_ternario = lambda x,y : x/y if y!=0 else x
print(funcao_ternario(10,0))
lista = ['Pedro', 'Ana', 'João']
funcao_exemplo_comprehension = lambda nomes : [nome.upper() for nome in nomes]
print(funcao_exemplo_comprehension(lista))
print(lista)
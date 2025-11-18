#Exemplo de LP1
entrada = list(map(int, input().split()))
print(entrada)
#Exemplo com lambda
lista = [1,2,3]
teste = [5,6,7,8]
quadrados = list(map(lambda x : x**2, lista))
print(quadrados)
soma = list(map(lambda x,y : x+y, lista, teste))
print(soma)


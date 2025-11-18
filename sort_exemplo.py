lista = [('ovos', 3), ('miragina', 10), ('cafe', 5)]
#lista.sort()
lista.sort(key = lambda tupla : tupla[1])
print(lista)

matriz = [[1,2,3],[4,5,6,7],[8,9]]
matriz.sort(key = lambda lista : len(lista))
print(matriz)

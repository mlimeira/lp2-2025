import random

valor = ['a','b','c']
def imprime():
    global valor
    #valor = random.randint(1,50)
    random.shuffle(valor)
    print('dentro da função',valor)
print('')
imprime()
print('')
print('fora da função',valor)
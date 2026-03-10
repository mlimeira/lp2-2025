class Sobrecarga:
    def __init__(self, *args): ##Possibilitar formas diferentes de criar os objetos
        self._tam = len(args)
        self._lista = args
        self.__str__()

    def __str__(self):
        if self._tam == 0:
            return 'Obj sem argumento'
        elif self._tam == 1:
            return f'Obj com um parâmetro + {self._lista[0]}'
        elif self._tam == 2:
            return f'Obj com dois parâmetros + {self._lista[0]} + {self._lista[1]}'
        
            
##    def __init__(self):
##        print('dois')
##    def __init__(self):
##        print('três')

teste = Sobrecarga('Arg')
teste2 = Sobrecarga('Arg1', 'Arg2')
print(teste)
print(teste2)

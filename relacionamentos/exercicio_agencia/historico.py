class Historico:
    def __init__(self):
        self._transacoes = []

    def ver_extrato(self):
        print('Inicio do Extrato')
        print('=================')
        for i in self._transacoes:
            print(i)
        print('=================')
        print('Fim Extrato')        

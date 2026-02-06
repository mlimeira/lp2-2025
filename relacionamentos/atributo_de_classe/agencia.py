class Agencia:
    def __init__(self):
        self._contas = []

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def listar_contas(self):
        print('Contas Ativas')
        inativas = []
        for conta in self._contas:
            if conta._ativa:
                print(conta)
            else:
                inativas.append(conta)
        print('Contas Inativas')
        for i in inativas:
            print(i)
    
    def fechar_agencia(self):
        while len(self._contas) > 0:
            conta_retirada = self._contas.pop()
            self.fechar_conta(conta_retirada)
##            while len(conta_retirada._clientes) > 0:
##               associacao = conta_retirada._clientes.pop()
##               while len(associacao._cliente._contas) > 0:
##                   associacao._cliente._contas.pop()
        print('Agência fechada com sucesso')

    def desativar_conta(self, conta):
        conta._ativa = False
        
    def fechar_conta(self, conta):
        while len(conta._clientes) > 0:
            associacao = conta._clientes.pop()
            #associacao._cliente._contas.remove(associacao)
            for i, c in enumerate(conta._clientes):
                if c._conta == associacao._conta:
                    conta._clientes.pop(i)
        self._contas.remove(conta)    
##            while len(associacao._cliente._contas) > 0:
##                associacao._cliente._contas.pop()







            

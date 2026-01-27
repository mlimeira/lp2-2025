class Agencia:
    def __init__(self):
        self._contas = []

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def listar_contas(self):
        for conta in self._contas:
            print(conta)
    
    def fechar_agencia(self):
        while len(self._contas) > 0:
            conta_retirada = self._contas.pop()
            #conta_retirada.fechar_conta()
            while len(conta_retirada._clientes) > 0:
               associacao = conta_retirada._clientes.pop()
               while len(associacao._cliente._contas) > 0:
                   associacao._cliente._contas.pop()
        print('Agência fechada com sucesso')









            

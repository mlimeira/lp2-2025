from conta import Conta

class Emprestimo:
    def __init__(self, conta, valor, parcelas):
        self._conta = conta
        self._valor = valor*1.25
        self._parcelas = parcelas
        self._valor_parcela = self._valor / parcelas
        conta.depositar(valor)
        self._saldo = self._valor
        self._parcelas_restantes = parcelas

    def pagar_parcela(self):
        if self._parcelas_restantes != 0:
            if self._conta.sacar(self._valor_parcela):
                self._saldo -= self._valor_parcela
                self._parcelas_restantes -= 1
                print(f'Parcela paga com sucesso')
        else:
            print('Emprestimo quitado')
                
        

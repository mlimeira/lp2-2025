from cliente import Cliente
from historico import Historico
from cliente_conta import ClienteConta

class SaldoInsuficienteError(Exception):
    pass

class Conta:
    #Método de inicialização dos objetos do tipo Conta
    #Características de identificação da conta
    #Classe Conta encapsulada
    #A classe Conta tem um relacionamento com a Classe Cliente
    def __init__(self, numero:int, saldo, limite):
        self._numero = numero
        #self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self._clientes = []
        self._historico = Historico() #É uma referência da classe Historico
        
    def get_listar_clientes(self):
        print(f'Clientes da conta {self}:')
        print('-----------------------------------')
        for associacao in self._clientes:
            print(f'{associacao._tipo} | {associacao._cliente}')

    def associar_cliente(self, cliente, tipo):
        associacao = ClienteConta(cliente, self, tipo)
        self._clientes.append(associacao)
        cliente._contas.append(associacao)

    

    #Métodos de controle de acesso
    def get_titular(self):
        return self._titular

    def set_titular(self, nome):
        self._titular = nome

    #Método de controle de acesso com anotações
    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valor):
        self._limite = valor

    #Características comportamentais (o que podemos executar: métodos)
    #Exercício: disparar uma exceção específica
    # quando o saque não puder ser realizado
    def sacar(self, valor):
        try:
            if valor > self._saldo + self._limite:
                raise SaldoInsuficienteError('Operação não realizada. Valor '
                                             'maior que saldo + limite.')
                #return False
            else:
                self._saldo -= valor
                self._historico._transacoes.append(f'Saque de {valor} realizado')
                return True
        except SaldoInsuficienteError as sie:
            print(sie)



    def depositar(self, valor):
        self._saldo += valor
        self._historico._transacoes.append(f'Depósito de {valor} realizado')

    def ver_saldo(self):
        if self._saldo < 0:
            print(f'Conta número: {self._numero} saldo negativo: {self._saldo}, '
                  f'usando limite de'
                  f' {self._limite} ainda pode utilizar'
                  f' {self._limite + self._saldo}')
        else:
            print(f'Conta número: {self._numero}, saldo: {self._saldo}')

    #Tranferir
    def transferir(self, conta_destino, valor):
        if valor <= self._saldo + self._limite:
            self._saldo -= valor
            self._historico._transacoes.append(f'Transf {valor} p/ conta {conta_destino}')
            conta_destino._saldo += valor
            conta_destino._historico._transacoes.append(f'Transf {valor} da conta {self}')
        else:
            print('Transferência não realizada')
##        if self.sacar(valor):
##            conta_destino.depositar(valor)
##            self._historico._transacoes.append(f'Transferência de {valor} realizada')
##            return True
##        else:
##            return False

    def __str__(self):
        return f'Conta número: {self._numero}'

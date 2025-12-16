class SaldoInsuficienteError(Exception):
    pass

class Conta:
    #Método de inicialização dos objetos do tipo Conta
    #Características de identificação da conta
    #Classe Conta encapsulada
    def __init__(self, numero:int, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

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
                return True
        except SaldoInsuficienteError as sie:
            print(sie)



    def depositar(self, valor):
        self._saldo += valor

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
        if self.sacar(valor):
            conta_destino.depositar(valor)
            return True
        else:
            return False

    def __str__(self):
        return f'Conta número: {self._numero}, Titular: {self._titular}'
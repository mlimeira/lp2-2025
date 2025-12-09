class Conta:
    #Método de inicialização dos objetos do tipo Conta
    #Características de identificação da conta
    def __init__(self, numero:int, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    #Características comportamentais (o que podemos executar)
    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            return False
        else:
            self.saldo -= valor
            return True

    def depositar(self, valor):
        self.saldo += valor

    def ver_saldo(self):
        if self.saldo < 0:
            print(f'Conta número: {self.numero} saldo negativo: {self.saldo}, '
                  f'usando limite de'
                  f' {self.limite} ainda pode utilizar'
                  f' {self.limite + self.saldo}')
        else:
            print(f'Conta número: {self.numero}, saldo: {self.saldo}')

    #Tranferir
    def transferir(self, conta_destino, valor):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            return True
        else:
            return False

    def __str__(self):
        return f'Conta número: {self.numero}, Titular: {self.titular}'
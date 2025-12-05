class Conta:
    #Método de inicialização dos objetos do tipo Conta
    def __init__(self, numero:int, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
from gerente import Gerente
from mixins_interfaces.autenticavel import Autenticavel


class Diretor(Gerente, Autenticavel):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)

    def autenticar(self, senha):
        if senha == '123':
            return True
        else:
            return False
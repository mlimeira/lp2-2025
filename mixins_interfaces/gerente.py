from funcionario import Funcionario
from autenticavel import Autenticavel
#Classe filha de Funcionario
class Gerente(Funcionario, Autenticavel):
    def __init__(self, nome, cpf, salario, senha, qtde):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtde = qtde

    def get_bonificacao(self):
        return super().get_bonificacao() + 5000#self._salario * 0.2

    def autenticar(self, senha):
        if senha == '1234':
            return True
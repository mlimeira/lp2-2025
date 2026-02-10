from funcionario import Funcionario
#Classe filha de Funcionario
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtde):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtde = qtde

    def get_bonificacao(self):
        return super().get_bonificacao() + 5000#self._salario * 0.2


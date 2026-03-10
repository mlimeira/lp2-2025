#Não preciso criar objetos da classe Funcionario
import abc
class Funcionario(abc.ABC):
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
    
    def redefinir_salario(self):
        self._salario += 1000 

    @abc.abstractmethod
    def get_bonificacao(self):
        pass

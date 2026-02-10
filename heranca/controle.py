from funcionario import Funcionario

class Controle:
    _total = 0
    def __init__(self, total = 0):
        self._total = total
        
    @classmethod
    def update_total(cls, funcionario): #Todo gerente é um funcionario
        #if hasattr(funcionario, 'get_bonificacao'):
        #if isinstance(funcionario, Funcionario):
        try:
            cls._total += funcionario.get_bonificacao()
        except AttributeError as ae:
            print(f'O objeto não implementa get_bonificacao')

    @classmethod
    def get_total(cls):
        return cls._total

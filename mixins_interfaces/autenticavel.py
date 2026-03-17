import abc
from abc import abstractmethod

class Autenticavel(abc.ABC):
    '''
    Esta interface define a regra para autenticação do sistema
    '''
    @abstractmethod
    def autenticar(self, senha):
        '''
        Este método deve verificar a senha dos usuários
        '''
        pass
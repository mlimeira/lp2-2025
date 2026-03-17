from autenticavel import Autenticavel
class Cliente(Autenticavel):
    def autenticar(self, senha):
        if senha == '123456':
            return True
        else:
            return False
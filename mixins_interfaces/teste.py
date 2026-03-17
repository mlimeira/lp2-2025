from gerente import Gerente
from presidente import Presidente
from cliente import Cliente
from sistema import Sistema

p = Presidente('Ronaldo', '1234567890', 90000)
g = Gerente('Zidane', '987654321', 80000, '123', 12)
c = Cliente()

sistema = Sistema()
if sistema.logar(c):
    print('Login realizado com sucesso')

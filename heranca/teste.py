from funcionario import Funcionario
from gerente import Gerente
from controle import Controle

f1 = Funcionario('Fulano', '111111111111', 10000)
g1 = Gerente('Beltrano', '99999999999', 20000, '123', 10)
print(f1._nome)
print(g1._nome)
f1.redefinir_salario()
g1.redefinir_salario()
print(f1.get_bonificacao())
print(g1.get_bonificacao())
#Controle de todas as bonificações
Controle.update_total(f1)
Controle.update_total(g1)
Controle.update_total('Presidente')
print(Controle.get_total())


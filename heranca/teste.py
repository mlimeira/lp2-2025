from funcionario import Funcionario
from gerente import Gerente

f1 = Funcionario('Fulano', '111111111111', 10000)
g1 = Gerente('Beltrano', '99999999999', 20000, '123', 10)
print(f1._nome)
print(g1._nome)
f1.redefinir_salario()
g1.redefinir_salario()

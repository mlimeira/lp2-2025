from cliente import Cliente
from conta import Conta

samuel = Cliente('Samuel', '99999999999')
marcos = Cliente('Maria', '11111111111')

conta_1 = Conta(1, 1000, 200)
conta_2 = Conta(2, 2000, 400)

conta_1.associar_cliente(samuel, 'titular')
conta_2.associar_cliente(samuel, 'dependente')
conta_2.associar_cliente(marcos, 'titular')
samuel.get_listar_contas()
conta_2.get_listar_clientes()



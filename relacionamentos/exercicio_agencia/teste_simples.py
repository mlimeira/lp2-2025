from cliente import Cliente
from conta import Conta
from agencia import Agencia

samuel = Cliente('Samuel', '99999999999')
marcos = Cliente('Maria', '11111111111')

conta_1 = Conta(1, 1000, 200)
conta_2 = Conta(2, 2000, 400)

conta_1.associar_cliente(samuel, 'titular')
conta_2.associar_cliente(marcos, 'titular')
conta_1.transferir(conta_2, 1000)
#conta_1._historico.ver_extrato()
#conta_2._historico.ver_extrato()

ag_centro = Agencia()
ag_centro.adicionar_conta(conta_1)
ag_centro.adicionar_conta(conta_2)
ag_centro.listar_contas()
ag_centro.fechar_agencia()
ag_centro.listar_contas()












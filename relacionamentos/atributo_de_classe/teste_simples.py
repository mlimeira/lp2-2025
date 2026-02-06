from cliente import Cliente
from conta import Conta
from agencia import Agencia
from emprestimo import Emprestimo

samuel = Cliente('Samuel', '99999999999')
marcos = Cliente('Maria', '11111111111')

conta_1 = Conta(1, 0, 250)
conta_2 = Conta(2, 2000, 400)
conta_3 = Conta(3, 3000, 300)

conta_1.associar_cliente(samuel, 'titular')
conta_2.associar_cliente(marcos, 'titular')
conta_3.associar_cliente(samuel, 'dependente')
conta_1.transferir(conta_2, 1000)
#conta_1._historico.ver_extrato()
#conta_2._historico.ver_extrato()

ag_centro = Agencia()
ag_centro.adicionar_conta(conta_1)
ag_centro.adicionar_conta(conta_2)
ag_centro.adicionar_conta(conta_3)
ag_centro.listar_contas()
#ag_centro.fechar_agencia()
print('-----------')
ag_centro.desativar_conta(conta_3)
ag_centro.listar_contas()

##emp_a = Emprestimo(conta_1, 1000, 4)
##emp.pagar_parcela()
##emp.pagar_parcela()
##emp.pagar_parcela()
##emp.pagar_parcela()
##emp.pagar_parcela()
##emp_b = Emprestimo(conta_1, 2000, 5)
##conta_1.listar_emprestimos()
#Pelo conceito de encapsulamento
#Temos que criar um método para acessar o atributo de classe

##print(Conta._total_contas)
##print(conta_1._total_contas)
##print(conta_2._total_contas)
#print(Conta.get_total_contas(conta_1))
print(conta_1.get_total_contas())
print(Conta.get_total_contas())
conta_1.chave_pix = '6899125003'
print(conta_1.chave_pix)













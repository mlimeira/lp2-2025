from conta import Conta

conta1 = Conta('1','Limeira',150.5, 0)
print(type(conta1))
print(id(conta1))
conta2 = Conta(2,'Kaua',5678, 1000)
print(id(conta2))
#definir características em tempo de execução não é correto
# conta1.titular = 'Limeira'
# conta1.saldo = 150.5
# conta1.numero = 1
print(conta1.titular)
print(conta1.saldo)
# conta2.titular = 'Kaua'
# conta2.saldo = 5678
# conta2.numero = 2
#conta2.limite = 1000
print(conta2.limite)
from conta import Conta

conta1 = Conta('1','Limeira',150.5, 10)
print(type(conta1))
print(id(conta1))
conta2 = Conta(2,'Kaua',5678, 1000)
print(id(conta2))
conta3 = conta1
print(id(conta3))
#definir características em tempo de execução não é correto
# conta1.titular = 'Limeira'
# conta1.saldo = 150.5
# conta1.numero = 1
#Acessar diretamente o atributo é incorreto
#print(conta1._Conta__titular)
conta1.set_titular('Limeira Júinor')
print(conta1.get_titular())
#print(conta1.saldo)
# conta2.titular = 'Kaua'
# conta2.saldo = 5678
# conta2.numero = 2
#conta2.limite = 1000
#print(conta2.limite)
conta1.ver_saldo()
conta1.depositar(500)
conta1.ver_saldo()
if conta1.sacar(661):
    print('Saque efetuado com sucesso')
else:
    print('Saldo insuficiente')

teste = conta1.ver_saldo()
print(teste)
conta3.depositar(100)
conta1.ver_saldo()
if conta1.transferir(conta2, 760.5):
    print('Transferência realizada com sucesso')
else:
    print('Saldo insuficiente')
conta2.ver_saldo()
print(conta2.__dict__)
print(dir(Conta))
print(conta2)
print(conta2.get_titular())
conta2.limite = 2000
print(conta2.limite)
conta2.sacar(10000)
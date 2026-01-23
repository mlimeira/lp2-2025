from endereco import Endereco
from cliente import Cliente
from conta import Conta

end1 = Endereco('69918-822', 'Rua Fonte Nova', 'Rio Branco')
end2 = Endereco('69900-000', 'Av Ceará', 'Rio Branco')
end3 = Endereco('69918-553', 'Av Getúlio Vargas', 'Rio Branco')

samuel = Cliente('Samuel', '99999999999', end1)
marcos = Cliente('Marcos', '11111111111', end1)
#print(end1)
#print(samuel)

conta_samuel = Conta(1, samuel, 1000, 200)
conta_marcos = Conta(2, marcos, 0, 500)
conta_teste = Conta(3, 'Teste', 0, 1000)#Teste não é uma referência de Cliente
conta_maria = Conta(4, samuel, 1000, 500)
#print(conta_samuel)
#print(conta_marcos)
#print(conta_teste)
conta_samuel.depositar(100)
conta_samuel.sacar(500)
conta_samuel.transferir(conta_marcos, 100)
conta_samuel._historico.ver_extrato()


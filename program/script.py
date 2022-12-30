
from Saque import Saque
from Deposito import Deposito

#variavel global 
valor_saldo = 3000
valor_saque = 1000
valor_deposito = 300

#saque
sacarDinheiro = Saque(valor_saldo, valor_saque)
print(sacarDinheiro.sacar())

#deposito
deposito = Deposito(valor_deposito, valor_saldo) 
print(deposito.depositar())


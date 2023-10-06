'''Classe Conta Corrente: Crie uma classe para implementar 
uma conta corrente. A classe deve possuir os seguintes 
atributos: número da conta, nome do correntista e saldo. 
Os métodos são os seguintes: alterarNome, depósito e saque; 
No construtor, saldo é opcional, com valor default zero 
e os demais atributos são obrigatórios.'''

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0.0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, nome_novo):
        self.nome_correntista = nome_novo

    def deposito(self, valor_depositado):
        self.saldo += valor_depositado

    def saque (self, valor_sacado):
        self.saldo -= valor_sacado
        
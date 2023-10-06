'''Classe Conta de Investimento: Faça uma classe contaInvestimento 
que seja semelhante a classe contaBancaria, com a diferença de que 
se adicione um atributo taxaJuros. Forneça um construtor que configure 
tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros 
(sem parâmetro explícito) que adicione juros à conta. Escreva um programa 
que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de 
juros de 10%. Depois aplique o método adicioneJuros() cinco vezes 
e imprime o saldo resultante. '''

class ContaInvestimento:
    def __init__(self, numero_conta, nome_correntista, taxa_juros, saldo=0.0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
        self.taxa_juros = taxa_juros

    def alterarNome(self, nome_novo):
        self.nome_correntista = nome_novo

    def deposito(self, valor_depositado):
        self.saldo += valor_depositado

    def saque (self, valor_sacado):
        self.saldo -= valor_sacado  

    def adicioneJuros(self):
        self.saldo = self.saldo*(1+self.taxa_juros)

poupanca = ContaInvestimento(123,'Alanna',0.1,1000)
for i in range(5):
    poupanca.adicioneJuros()

print(poupanca.saldo)
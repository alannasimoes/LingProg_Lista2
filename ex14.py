'''Aprimore a classe do exercício anterior para 
adicionar o método aumentarSalario (porcentualDeAumento) 
que aumente o salário do funcionário em uma certa porcentagem. '''

class Funcionario:
    def __init__(self, nome:str, salario:float):
        self.nome = nome 
        self.salario = salario

    def retornaNome(self):
        return self.nome
    
    def retornaSalario(self):
        return self.salario
    
    def aumentarSalario(self, percentualDeAumento):
        self.salario = self.salario*(1+percentualDeAumento)
    
funcionario = Funcionario('João', 10000)
print(funcionario.retornaNome())
print(funcionario.retornaSalario())
funcionario.aumentarSalario(0.06)
print(funcionario.retornaSalario())
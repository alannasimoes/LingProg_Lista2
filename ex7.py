'''Classe Bichinho Virtual:Crie uma classe que modele um 
Tamagushi (Bichinho Eletrônico):

    Atributos: Nome, Fome, Saúde e Idade 
    Métodos: Alterar Nome, Fome, Saúde e Idade; 
    Retornar Nome, Fome, Saúde e Idade 
    Obs: Existe mais uma informação que devemos levar em 
    consideração, o Humor do nosso tamagushi, este humor 
    é uma combinação entre os atributos Fome e Saúde, ou seja,
    um campo calculado, então não devemos criar um atributo 
    para armazenar esta informação por que ela pode ser 
    calculada a qualquer momento.'''

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 100
        self.saude = 100
        self.idade = 0

    def alterarNome(self, nome_novo):
        self.nome = nome_novo

    def alterarFome(self, fome_nova):
        if fome_nova > 100 or fome_nova < 0:
            print('Valor inválido')
        else:
            self.fome = fome_nova

    def alterarSaude(self, saude_nova):
        if saude_nova > 100 or saude_nova < 0:
            print('Valor inválido')
        else:
            self.saude = saude_nova

    def alterarIdade(self, idade_nova):
        if idade_nova < 0:
            print('Valor inválido')
        else:
            self.idade = idade_nova

    def retornaNome(self):
        return self.nome
    
    def retornaFome(self):
        return self.fome
    
    def retornaSaude(self):
        return self.saude
    
    def retornaIdade(self):
        return self.idade
    
    def humor(self):
        valor_humor = self.fome + self.saude
        if valor_humor > 150:
            return 'Feliz'
        elif valor_humor > 100:
            return 'Normal'
        elif valor_humor > 50:
            return 'Triste'
        else:
            return 'Morrendo'
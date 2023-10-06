'''Classe Pessoa: Crie uma classe que modele uma pessoa:

    Atributos: nome, idade, peso e altura
    Métodos: Envelhercer, engordar, emagrecer, crescer. 
    Obs: Por padrão, a cada ano que nossa pessoa envelhece, 
    sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.'''

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.5

    def engordar(self, peso_extra):
        self.peso += peso_extra

    def emagrecer(self, peso_perdido):
        self.peso -= peso_perdido

    def crescer(self, altura_extra):
        self.altura += altura_extra
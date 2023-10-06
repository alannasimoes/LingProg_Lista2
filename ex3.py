'''Classe Retangulo: Crie uma classe que modele um retangulo:

    Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base 
    e Altura, a escolher)
    Métodos: Mudar valor dos lados, Retornar valor dos lados, 
    calcular Área e calcular Perímetro;
    Crie um programa que utilize esta classe. 
    Ele deve pedir ao usuário que informe as medidas de 
    de um local. Depois, deve criar um objeto com 
    as medidas e calcular a quantidade de pisos e 
    de rodapés necessários para o local.'''

class Retangulo:
    def __init__(self,comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
    
    def mudarComprimento(self, comprimento_novo):
        self.comprimento = comprimento_novo

    def mudarLargura(self, largura_nova):
        self.largura = largura_nova

    def retornaLargura(self):
        return self.largura
    
    def retornaComprimento(self):
        return self.comprimento

    def area(self):
        return self.comprimento*self.largura
    
    def perimetro(self):
        return 2*self.comprimento + 2*self.largura
    

def quantidades():
    print('Informe as medidas do local')
    comprimento = float(input('Comprimento: '))
    largura = float(input('Largura: '))

    local = Retangulo(comprimento, largura)

    print(f'Você vai precisar de {local.perimetro()} rodapés')
    print(f'Você vai precisar de {local.area()} pisos')

quantidades()

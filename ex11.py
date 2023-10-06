'''Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

    Um veículo tem um certo consumo de combustível (medidos em km / litro) 
    e uma certa quantidade de combustível no tanque.
    O consumo é especificado no construtor e o nível de combustível inicial é 0.
    Forneça um método andar( ) que simule o ato de dirigir o veículo 
    por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
    Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
    Forneça um método adicionarGasolina( ), para abastecer o tanque.'''

class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def andar(self, distancia):
        if self.combustivel-(distancia/self.consumo) < 0:
            print('Não há combustível suficiente')
        else:
            self.combustivel -= distancia/self.consumo

    def obterGasolina(self):
        print(f'Gasolina: {self.combustivel}L')
    
    def adicionarGasolina(self, quantidade_abastecida):
        self.combustivel += quantidade_abastecida


fusca = Carro(15)
fusca.adicionarGasolina(20)
fusca.andar(100)
fusca.obterGasolina()
